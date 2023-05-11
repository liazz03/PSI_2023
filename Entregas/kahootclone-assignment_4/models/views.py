from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


class SignUpView(CreateView):

    template_name = 'signup.html'
    success_url = reverse_lazy('home')
    form_class = SignUpForm

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return response
