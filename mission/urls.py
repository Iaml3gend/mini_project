from django.urls import path
from . import views

from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('news', views.news, name='news'),
    path('training', views.training, name='training'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('campus', views.campus, name='campus'),

]
