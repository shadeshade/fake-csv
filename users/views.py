from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView


class Login(UserPassesTestMixin, LoginView):
    template_name = 'users/login.html'

    def test_func(self):
        return self.request.user.is_anonymous


class Logout(LogoutView):
    pass
