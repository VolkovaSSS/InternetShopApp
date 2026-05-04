from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from users.forms import UserCreationForm


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('users:login')
