from django.urls import path

from . import views

# app_name is needed for templates i.e. polls:detail if there is more than one
# detail in django project
app_name = 'polls'
urlpatterns = [

    # question_id had to be changed to pk since generic views expect pk
    # path('index', views.index, name='index'),
    # path('<int:question_id>/vote', views.vote, name='vote'),
    # path('<int:question_id>/results', views.results, name='results'),
    # path('<int:question_id>/', views.detail, name='detail'),

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]
