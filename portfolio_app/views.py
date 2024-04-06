from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Skill

class SkillList(LoginRequiredMixin, ListView):
    model = Skill
    context_object_name = 'skills'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = context['skills'].filter(user=self.request.user)
        context['count'] = context['skills'].filter(complete=False).count()
        return context

class SkillDetail(LoginRequiredMixin, DetailView):
    model = Skill
    context_obect_name = 'skill'

class SkillCreate(LoginRequiredMixin, CreateView):
    model = Skill
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy("skills")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SkillCreate, self).form_valid(form)

class SkillUpdate(LoginRequiredMixin, UpdateView):
    model = Skill
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('skills')

class SkillDelete(LoginRequiredMixin, DeleteView):
    model = Skill
    context_object_name = 'skill'
    success_url = reverse_lazy('skills')
    template_name = 'portfolio_app/delete_skill.html'

class SkillLogin(LoginView):
    template_name = 'portfolio_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('skills')
    
class SkillSignUp(FormView):
    template_name = 'portfolio_app/signup.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('skills')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SkillSignUp, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('skills')
        return super(SkillSignUp, self).get(*args, **kwargs)