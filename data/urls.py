from django.urls import path,include
from . import views

urlpatterns = [
    path('banners', views.GetBanners.as_view()),
    path('form', views.NewForm.as_view()),
    path('courses', views.GetCourses.as_view()),
    path('sales', views.GetSales.as_view()),




]
