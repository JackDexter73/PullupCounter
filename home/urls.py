from django.urls import path
from . import views
from home.views import thirdtest, addrepstodatabase

urlpatterns = [
path('', views.initialtest, name='home'),
path('booty/', views.BootstrapTestView.as_view(), name='test'),
path('add/', views.addrepstodatabase),
path('form/', views.fifthtest),
path('home/', views.homeView, name='home2'),
path('pullups/', views.pullupsView, name='pullups'),
path('pushups/', views.pushupsView, name='pushups'),
path('rows/', views.rowsView, name='rows'),
path('squats/', views.squatsView, name='squats'),
]
