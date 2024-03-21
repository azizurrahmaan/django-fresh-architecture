from django.views.generic import TemplateView, FormView, CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin


class DashBoardView(TemplateView):
    template_name = 'users/dashboard.html'


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('dashboard')
        return super(SignUpView, self).get(request, *args, **kwargs)