# survey/views.py

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import PermissionDenied
#from django.contrib.auth.models import User
#from django.core.exceptions import ValidationError
from .models import Survey, SurveyAssignment


from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View

class RegisterView(View):
    def get(self, request):
        return render(request, 'survey/register.html', { 'form': UserCreationForm() })

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            _user = form.save()
            return redirect(reverse('login'))

        return render(request, 'survey/register.html', { 'form': form })


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        surveys = Survey.objects.filter(created_by=request.user).all()
        assigned_surveys = SurveyAssignment.objects.filter(assigned_to=request.user).all()

        context = {
          'surveys': surveys,
          'assigned_surveys': assigned_surveys
        }

        return render(request, 'survey/profile.html', context)