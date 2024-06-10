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

urlpatterns = [
    path('', views.index, name='home'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/', views.api_page),
    re_path(r'^news/', views.news, name='news'),
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
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
