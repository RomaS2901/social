from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.views import LoginView, LogoutView


class SignUp(View):

  def get(self, request):
    pass

  def post(self, request):
    pass


class MyLoginView(LoginView):
  template_name = 'accounts/login.html'
