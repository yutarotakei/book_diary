from django.urls import path

from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('book-list/', views.BookListView.as_view(), name='book_list'),
    path('book-create/', views.bookcreate, name='book_create'),
    path('book-delete/<int:pk>/', views.BookDeleteView.as_view(), name='book_delete'),
    path('plot/', views.get_svg, name='plot'),
]