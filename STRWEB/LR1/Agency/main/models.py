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
    code = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code
    
class MyUser(models.Model):
    user = models.OneToOneField(User, blank=False, default=None, on_delete=models.CASCADE, related_name='profile', null=True)
    phone_number = models.CharField(max_length=13, blank=False, default=None)
    my_coupons = models.ManyToManyField(Coupon, related_name='user_coupons', blank=True, default=None)
    my_sales = models.ManyToManyField(Sale, related_name='sales', blank=True)

    def __str__(self):
        return self.user.get_username