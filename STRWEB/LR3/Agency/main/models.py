from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='properties/', default=None)
    price = models.DecimalField(max_digits=10, default=0, decimal_places=2)

    def __str__(self):
        return self.title

class Employee(models.Model):
    user = models.OneToOneField(User, default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Sale(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.property} - {self.employee}"

class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255) 
    content = models.TextField()  
    image = models.ImageField(upload_to='articles/')

    def __str__(self):
        return self.title
class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question

class Contact(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='contacts/')
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    text = models.TextField(default='')

    def __str__(self):
        return f"{self.user.username} - {self.date}"

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00) 
    expiration_date = models.DateField(null=True, blank=True)  

    def __str__(self):
        return self.code

class MyUser(models.Model):
    user = models.OneToOneField(User, blank=False, default=None, on_delete=models.CASCADE, related_name='profile', null=True)
    phone_number = models.CharField(max_length=13, blank=False, default=None)
    my_coupons = models.ManyToManyField(Coupon, related_name='user_coupons', blank=True, default=None)
    my_sales = models.ManyToManyField(Sale, related_name='sales', blank=True)

    def __str__(self):
        return self.user.get_username
    
class PartnerCompany(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='partners/', default=None)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Корзина пользователя {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.property.title}"
    
class CompanyInfo(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logo/')
    video_url = models.URLField(blank=True, null=True)
    history = models.TextField()
    details = models.TextField()
    certificate = models.ImageField()

    def __str__(self):
        return self.name