from django.urls import path
from basicapp import views

app_name = "basic_app"

urlpatterns = [
    path('',views.index, name='index'),
    path('service', views.service, name='service'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('work', views.work, name='work'),
]