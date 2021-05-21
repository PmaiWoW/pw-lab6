from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home', views.home_page_view, name='home'),
    path('about', views.about_page_view, name='about'),
    path('contacts', views.contacts_page_view, name='contacts')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)