"""
URL configuration for Agency project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,  re_path, include
from django.conf import settings
from main import views
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='home'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/', views.api_page),
    path('news/<int:id>/', views.article_detail_view, name='article_detail'),
    re_path(r'^news/', views.news, name='news'),
    re_path(r'^private-policy/', views.privatepolicy, name='news'),
    re_path(r'^faq/', views.faq),
    re_path(r'^vacancies/', views.vacancies, name='vacancies'),
    re_path(r'^about/', views.about, name='about'),
    re_path(r'^coupons/', views.coupons, name='coupons'),
    re_path(r'^reviews/', views.reviews, name='reviews'),
    path('contacts/<int:contact_id>/', views.contact_detail, name='contact_detail'),
    re_path(r'^contacts/add/', views.add_contact, name='add_contact'),
    path('add_property/', views.add_property, name='add_property'),
    path('edit_property/<int:property_id>/', views.edit_property, name='edit_property'),
    path('delete_property/<int:property_id>/', views.delete_property, name='delete_property'),
    re_path(r'^contacts/', views.contacts, name='contacts'),
    path('edit_contact/<int:contact_id>/', views.edit_contact, name='edit_contact'),
    path('delete_contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    re_path(r'^account/', views.account, name='account'),
    re_path(r'^changeinfo/', views.changeinfo),
    re_path(r'^login/', views.login_user, name='login'),
    re_path(r'^register/', views.register, name='register'),
    re_path(r'^logout/', views.logout_view, name='logout'),
    path('property/<int:property_id>/', views.property_detail, name='property_detail'),
    path('purchase/<int:property_id>/', views.purchase_property, name='purchase_property'),
    path('add_to_cart/<int:property_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('add_to_cart/<int:property_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_cart_item/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('process_payment/', views.process_payment, name='process_payment'),
    path('success/', TemplateView.as_view(template_name='main/success.html'), name='success_page'),
    path('poligon/', TemplateView.as_view(template_name='main/poligon.html'), name='poligon_page'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
