from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article
from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import *
from django.contrib.auth.models import User
import django.shortcuts
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import logging
from django.db.models import Sum
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from Agency.forms import *
import requests
import numpy as np

logging.basicConfig(level=logging.INFO, filename="D:\codes\Course 2\IGI\\253503_Kudosh_13\STRWEB\LR1\Agency\main\py_log.log", filemode="a+", format="%(asctime)s %(levelname)s %(message)s")

def index(request):
    logging.info('Rendering index page')
    properties = Property.objects.all()
    categories = Category.objects.all()
    latest_article = Article.objects.last() 
    partners = PartnerCompany.objects.all()
    sort_price = request.GET.get('sort_price')
    if sort_price == 'asc':
        properties = properties.order_by('price')
    elif sort_price == 'desc':
        properties = properties.order_by('-price')

    sort_category = request.GET.get('sort_category')
    if sort_category:
        properties = properties.filter(category__name=sort_category)

    
    context = {
        'properties': properties,
        'categories': categories,
        'sort_price': sort_price,
        'sort_category': sort_category,
        'latest_article': latest_article,
        'partners' : partners,
    }
    return render(request, 'main/index.html', context)

@login_required
def add_property(request):
    logging.info('Adding property')
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PropertyForm()
    
    context = {'property_form': form}
    return render(request, 'main/index.html', context)

def about(request):
    logging.info('Rendering about page')
    company = CompanyInfo.objects.first()  
    return render(request, 'main/about.html', {'company': company})

def news(request):
    logging.info('Rendering news page')
    articles = Article.objects.all()
    return render(request, 'main/news.html', {'articles': articles})

def article_detail_view(request, id):
    print('asddas')
    article = get_object_or_404(Article, id=id)  
    return render(request, 'main/article_detail.html', {'article': article})

def faq(request):
    logging.info('Rendering faq page')
    faqs = FAQ.objects.all()
    return render(request, 'main/faq.html', {'faqs': faqs})

def contacts(request):
    logging.info('Rendering contacts page')
    contacts = Contact.objects.all()
    print('asdsda')
    return render(request, 'main/contacts.html', {'contacts': contacts})

def contact_detail(request, contact_id):
    logging.info('Rendering contacts detail page')
    contact = get_object_or_404(Contact, id=contact_id)
    return render(request, 'main/contact_detail.html', {'contact': contact})

@login_required
def edit_contact(request, contact_id):
    logging.info('Editing contacts ')
    contact = get_object_or_404(Contact, id=contact_id)
    
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_detail', contact_id=contact.id)
    else:
        form = ContactForm(instance=contact)
    
    context = {'form': form}
    return render(request, 'main/edit_contact.html', context)

@login_required
def delete_contact(request, contact_id):
    logging.info('Deleting contacts ')
    contact = get_object_or_404(Contact, id=contact_id)
    
    if request.method == 'POST':
        contact.delete()
        return redirect('home')  # Replace 'home' with the appropriate URL name for your home page
    
    context = {'contact': contact}
    return render(request, 'main/delete_contact.html', context)

@login_required
def add_contact(request):
    logging.info('Adding contacts ')
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contacts')
    else:
        form = ContactForm()
    
    context = {'form': form}
    return render(request, 'main/add_contact.html', context)

def privatepolicy(request):
    logging.info('Rendering privatepolicy page')
    return render(request, 'main/privatepolicy.html')

def vacancies(request):
    logging.info('Rendering vacancies page')
    vacancies = Vacancy.objects.all()
    context = {'vacancies': vacancies}
    return render(request, 'main/vacancies.html', context)

def reviews(request):
    logging.info('Rendering reviews page')
    if request.method == 'POST':
        rating = int(request.POST.get('rating'))
        text = request.POST.get('text')
        user = request.user

        review = Review.objects.create(user=user, rating=rating, text=text)
        review.save()

    reviews = Review.objects.all()

    context = {'reviews': reviews}
    return render(request, 'main/reviews.html', context)

def coupons(request):
    logging.info('Rendering coupons page')
    coupons = Coupon.objects.all()
    context = {'coupons': coupons}
    return render(request, 'main/coupons.html', context)

def property_detail(request, property_id):
    logging.info('Rendering property detail page')
    property = get_object_or_404(Property, id=property_id)
    context = {'property': property}
    return render(request, 'main/property_detail.html', context)

def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'main/cart.html', {'cart': cart})

def add_to_cart(request, property_id):
    if request.method == 'POST':
        cart, created = Cart.objects.get_or_create(user=request.user)
        property = get_object_or_404(Property, id=property_id)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, property=property)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect('cart_view')

def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item.quantity = quantity
        cart_item.save()
    return redirect('cart_view')

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart_view')

@login_required
def purchase_property(request, property_id):
    logging.info('Purchase')
    property = get_object_or_404(Property, id=property_id)
    user = request.user
    sale = Sale(property=property, buyer=user)
    sale.save()
    user.profile.my_sales.add(sale)
    return redirect('property_detail', property_id=property_id)

@login_required
def edit_property(request, property_id):
    logging.info('edit_property page')
    property = get_object_or_404(Property, id=property_id)
    
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property_detail', property_id=property.id)
    else:
        form = PropertyForm(instance=property)
    
    context = {'form': form}
    return render(request, 'main/edit_property.html', context)

@login_required
def delete_property(request, property_id):
    logging.info('delete_property page')
    property = get_object_or_404(Property, id=property_id)
    
    if request.method == 'POST':
        property.delete()
        return redirect('home') 
    
    context = {'property': property}
    return render(request, 'main/delete_property.html', context)

def account(request):
    logging.info('account page')
    if request.COOKIES.get("username") is not None:
        user = User.objects.get(username = request.COOKIES["username"])

        myuser = MyUser.objects.select_related('user').prefetch_related('my_coupons', 'my_sales').get(user=user)
        user_timezone = timezone.get_current_timezone()

        is_admin = request.COOKIES.get("admin") == "True"
        graph_file = "D:/graph.png"
        if is_admin:
            user_purchases = Sale.objects.values('buyer').annotate(total_purchases=Sum('property__price'))

            print(user_purchases)
            usernames = [purchase['buyer'] for purchase in user_purchases]
            total_purchases = [purchase['total_purchases'] for purchase in user_purchases]

            x_ticks = np.arange(len(usernames))
            plt.bar(x_ticks, total_purchases)
            plt.xlabel('Пользователи')
            plt.ylabel('Сумма покупок')
            plt.title('График сумм покупок пользователей')
            plt.xticks(x_ticks, usernames, rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig(graph_file)
        else:
            pass

        return TemplateResponse(
            request,
            "main/account.html",
            {"user": myuser, "time_zone": user_timezone, "is_admin": is_admin,}
        )
    else:
        return redirect('/')

def login_user(request):
    logging.info('login page')
    if(request.method == "POST"):
        form = LoginForm(request.POST)
        
        if form.is_valid():
            password = form.cleaned_data["password"]
            username = form.cleaned_data["username"]

            user = authenticate(username=username, password=password)
            login(request, user)

            response = django.shortcuts.redirect('/')
            response.set_cookie('username', username, max_age=3600)
            if user.is_superuser == True:
                response.set_cookie('role', True, max_age=3600)
            else:
                response.set_cookie('role', user.is_staff, max_age=3600) 

            response.set_cookie('admin', user.is_superuser, max_age=3600) 

            logging.info("sign in complited")

            return response
        else:
            logging.error("sign in error")
            return TemplateResponse(request, "main/login.html", {"form": form, "errors": form.errors.values()})
        
    return TemplateResponse(request, "main/login.html", {"form": LoginForm})

def register(request):
    logging.info('register page')
    if(request.method == "POST"):
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            phone_num = form.cleaned_data["phone_number"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            username = form.cleaned_data["username"]

            user = User.objects.create_user(email=email, password=password, username=username)

            MyUser.objects.create(user=user, phone_number = phone_num)

            logging.info("registration complited")

            return django.shortcuts.redirect('login')
        else:
            logging.error("registration failed")
            return TemplateResponse(request, "main/register.html", {"form":form, "errors":form.errors.values()})
    return TemplateResponse(request, "main/register.html", {"form": RegisterForm})

def changeinfo(request):
    logging.info('changeinfo page')

    if(request.method == "POST"):
        form = ChangeForm(request.POST)
        
        if form.is_valid():
            phone_num = form.cleaned_data["phone_number"]
            email = form.cleaned_data["email"]
            username = form.cleaned_data["username"]

            user = User.objects.get(username = request.COOKIES["username"])

            myuser = MyUser.objects.select_related('user').prefetch_related('my_coupons', 'my_sales').get(user=user)

            if phone_num != "+37529":
                myuser.phone_number = phone_num
            
            if email != "":
                user.email = email
            
            if username != "":
                user.username = username
            
            user.save()

            myuser.save()

            response = django.shortcuts.redirect('/account')
                
            response.delete_cookie("username")
            response.set_cookie('username', user.username, max_age=3600)
            response.delete_cookie("role")
            response.set_cookie('role', user.is_staff, max_age=3600) 

            logging.info("change account information")

            return response
        else:
            logging.error("change account information error")
            return TemplateResponse(request, "main/changeinfo.html", {"form":form, "errors":form.errors.values()})
        
    return TemplateResponse(request, "main/changeinfo.html", {"form": ChangeForm})

def logout_view(request):
    logging.info('logout')
    logout(request)
    return redirect('home')

def create_property(request):
    logging.info('create_property')
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    
    return render(request, 'properties/create_property.html', {'form': form})

@login_required
def api_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            # Make requests to genderize.io and nationalize.io APIs
            genderize_url = f"https://api.genderize.io/?name={name}"
            nationalize_url = f"https://api.nationalize.io/?name={name}"

            gender_response = requests.get(genderize_url)
            national_response = requests.get(nationalize_url)

            if gender_response.status_code == 200 and national_response.status_code == 200:
                gender_data = gender_response.json()
                national_data = national_response.json()

                context = {
                    'name': name,
                    'gender': gender_data.get('gender'),
                    'probability': gender_data.get('probability'),
                    'country': national_data.get('country')[0].get('country_id'),
                    'probability_country': national_data.get('country')[0].get('probability')
                }

                return render(request, 'main/api.html', context)

    return render(request, 'main/api.html')

def checkout_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    total_price = sum(item.property.price * item.quantity for item in cart.items.all())
    return render(request, 'checkout.html', {'cart': cart, 'total_price': total_price})

def process_payment(request):
    if request.method == 'POST':
        cart = Cart.objects.get(user=request.user)
        cart.items.all().delete()  
        return redirect('success_page') 