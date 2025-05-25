from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.home, name='base'),
    path('manga/', views.manga_list, name='manga_list'),  # Thêm dòng này
    path('manga/<int:manga_id>/', views.detail, name='detail'),
    path('chapter/<int:chapter_id>/', views.chapter, name='chapter'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
