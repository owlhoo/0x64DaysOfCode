from django.urls import path

from . import views

# app_name is needed for templates i.e. polls:detail if there is more than one
# detail in django project
app_name = 'polls'
urlpatterns = [
    path('index', views.index, name='index'),
    path('<int:question_id>/vote', views.vote, name='vote'),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/', views.detail, name='detail'),
]
