from django.urls import path

from . import views

app_name = 'worksheet'
urlpatterns = [
    # worksheet/
    path('', views.index, name='index'),
    # worksheet/N1/2/
    path('<str:worksheet_internal_name>/<int:page_num>/', views.detail, name='detail'),
]