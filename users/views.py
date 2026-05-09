from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from users.forms import CustomUserRegisterForm
from django.core.mail import send_mail
from django.contrib.auth import login
from users.models import CustomUser
from config.settings import EMAIL_HOST_USER

# import secrets
# from smtplib import SMTPAuthenticationError
# from django.shortcuts import get_object_or_404, redirect, reverse


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
        # user.is_active = False
        # token = secrets.token_hex(16)
        # user.token = token
        # user.save()
        # host = self.request.get_host()
        # url = f"https://{host}/users/email-confirm/{token}/"
        # send_mail(
        #         subject="Подтверждение почты",
        #         message=f"Подтвердите почту по ссылке {url}",
        #         from_email=EMAIL_HOST_USER,
        #         recipient_list=[user.email],
        #     )

    def send_welcome_email(self, user_email, host):
        subject = "Добро пожаловать на сайт"
        message = f"Спасибо, что зарегистрировались на сайте {host}!"
        from_email = EMAIL_HOST_USER
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)


# def email_verification(request, token):
#
#     user = get_object_or_404(CustomUser, token=token)
#     user.is_active = True
#     user.save()
#     return redirect(reverse("users:login"))
