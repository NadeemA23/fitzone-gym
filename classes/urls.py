from django.urls import path
from . import views


urlpatterns = [
    path('', views.class_list, name='class_list'),
    path('book/<int:class_id>/', views.book_class, name='book_class'),
]