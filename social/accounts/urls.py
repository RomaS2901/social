from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
  path('login/', views.MyLoginView.as_view(), name='login-view')
]
