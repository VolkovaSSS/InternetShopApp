from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from users.forms import CustomUserRegisterForm
from django.core.mail import send_mail
from django.contrib.auth import login
from users.models import CustomUser
from config.settings import EMAIL_HOST_USER


class RegisterView(CreateView):
    template_name = "register.html"
    model = CustomUser
    form_class = CustomUserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        host = self.request.get_host()
        self.send_welcome_email(user.email, host)
        return super().form_valid(form)

    def send_welcome_email(self, user_email, host):
        subject = "Добро пожаловать на сайт"
        message = f"Спасибо, что зарегистрировались на сайте {host}!"
        from_email = EMAIL_HOST_USER
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)
