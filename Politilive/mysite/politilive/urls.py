from django.urls import path

from . import views

app_name = 'politilive'
urlpatterns = [
    # ex: /politilive/
    path('', views.index, name='index'),
    path('reset/', views.reset, name='reset'),
    # ex: /politilive/5/
    path('<int:question_id>/', views.vote, name='vote'),
    path('<int:question_id>/', views.detail, name='detail'),
]
