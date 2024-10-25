from django.test import TestCase, Client
from django.urls import reverse
from .models import Category, Property, Employee, Sale, Article, FAQ, Contact, Vacancy, Review, Coupon, MyUser
from django.contrib.auth.models import User


class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_category_model(self):
        category = Category.objects.create(name='Test Category')
        self.assertEqual(category.name, 'Test Category')

    def test_property_model(self):
        category = Category.objects.create(name='Test Category')
        property = Property.objects.create(title='Test Property', description='Test Description', category=category)
        self.assertEqual(property.title, 'Test Property')
        self.assertEqual(property.description, 'Test Description')
        self.assertEqual(property.category, category)

    def test_employee_model(self):
        employee = Employee.objects.create(user=self.user)
        self.assertEqual(employee.user, self.user)

    def test_sale_model(self):
        category = Category.objects.create(name='Test Category')
        property = Property.objects.create(title='Test Property', description='Test Description', category=category)
        sale = Sale.objects.create(property=property, buyer=self.user)
        self.assertEqual(sale.property, property)
        self.assertEqual(sale.buyer, self.user)

    def test_article_model(self):
        article = Article.objects.create(title='Test Article', content='Test Content')
        self.assertEqual(article.title, 'Test Article')
        self.assertEqual(article.content, 'Test Content')

    def test_faq_model(self):
        faq = FAQ.objects.create(question='Test Question', answer='Test Answer')
        self.assertEqual(faq.question, 'Test Question')
        self.assertEqual(faq.answer, 'Test Answer')

    def test_contact_model(self):
        contact = Contact.objects.create(name='Test Contact', description='Test Description', phone='1234567890', email='test@test.com')
        self.assertEqual(contact.name, 'Test Contact')
        self.assertEqual(contact.description, 'Test Description')
        self.assertEqual(contact.phone, '1234567890')
        self.assertEqual(contact.email, 'test@test.com')

    def test_vacancy_model(self):
        vacancy = Vacancy.objects.create(title='Test Vacancy', description='Test Description')
        self.assertEqual(vacancy.title, 'Test Vacancy')
        self.assertEqual(vacancy.description, 'Test Description')

    def test_review_model(self):
        review = Review.objects.create(user=self.user, rating=5, text='Test Review')
        self.assertEqual(review.user, self.user)
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.text, 'Test Review')

    def test_coupon_model(self):
        coupon = Coupon.objects.create(code='TESTCODE')
        self.assertEqual(coupon.code, 'TESTCODE')
        self.assertTrue(coupon.is_active)

    def test_myuser_model(self):
        myuser = MyUser.objects.create(user=self.user, phone_number='1234567890')
        self.assertEqual(myuser.user, self.user)
        self.assertEqual(myuser.phone_number, '1234567890')
        self.assertEqual(myuser.my_coupons.count(), 0)
        self.assertEqual(myuser.my_sales.count(), 0)

    def test_category_model(self):
        category = Category.objects.create(name='Test Category')
        self.assertEqual(category.name, 'Test Category')

    def test_property_model(self):
        category = Category.objects.create(name='Test Category')
        property = Property.objects.create(title='Test Property', description='Test Description', category=category)
        self.assertEqual(property.title, 'Test Property')
        self.assertEqual(property.description, 'Test Description')
        self.assertEqual(property.category, category)

    def test_employee_model(self):
        employee = Employee.objects.create(user=self.user)
        self.assertEqual(employee.user, self.user)

    def test_sale_model(self):
        category = Category.objects.create(name='Test Category')
        property = Property.objects.create(title='Test Property', description='Test Description', category=category)
        sale = Sale.objects.create(property=property, buyer=self.user)
        self.assertEqual(sale.property, property)
        self.assertEqual(sale.buyer, self.user)

    def test_article_model(self):
        article = Article.objects.create(title='Test Article', content='Test Content')
        self.assertEqual(article.title, 'Test Article')
        self.assertEqual(article.content, 'Test Content')

    def test_faq_model(self):
        faq = FAQ.objects.create(question='Test Question', answer='Test Answer')
        self.assertEqual(faq.question, 'Test Question')
        self.assertEqual(faq.answer, 'Test Answer')

    def test_contact_model(self):
        contact = Contact.objects.create(name='Test Contact', description='Test Description', phone='1234567890', email='test@test.com')
        self.assertEqual(contact.name, 'Test Contact')
        self.assertEqual(contact.description, 'Test Description')
        self.assertEqual(contact.phone, '1234567890')
        self.assertEqual(contact.email, 'test@test.com')

    def test_vacancy_model(self):
        vacancy = Vacancy.objects.create(title='Test Vacancy', description='Test Description')
        self.assertEqual(vacancy.title, 'Test Vacancy')
        self.assertEqual(vacancy.description, 'Test Description')

    def test_review_model(self):
        review = Review.objects.create(user=self.user, rating=5, text='Test Review')
        self.assertEqual(review.user, self.user)
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.text, 'Test Review')

    def test_coupon_model(self):
        coupon = Coupon.objects.create(code='TESTCODE')
        self.assertEqual(coupon.code, 'TESTCODE')
        self.assertTrue(coupon.is_active)

    def test_myuser_model(self):
        myuser = MyUser.objects.create(user=self.user, phone_number='1234567890')
        self.assertEqual(myuser.user, self.user)
        self.assertEqual(myuser.phone_number, '1234567890')
        self.assertEqual(myuser.my_coupons.count(), 0)
        self.assertEqual(myuser.my_sales.count(), 0)

class UrlTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_news_url(self):
        response = self.client.get(reverse('news'))
        self.assertEqual(response.status_code, 200)

    def test_vacancies_url(self):
        response = self.client.get(reverse('vacancies'))
        self.assertEqual(response.status_code, 200)

    def test_about_url(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_coupons_url(self):
        response = self.client.get(reverse('coupons'))
        self.assertEqual(response.status_code, 200)

    def test_reviews_url(self):
        response = self.client.get(reverse('reviews'))
        self.assertEqual(response.status_code, 200)

