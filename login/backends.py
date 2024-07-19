# login/backends.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from bodega.models import Usuario

class CustomBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Usuario.objects.get(userMail=username)
        except Usuario.DoesNotExist:
            try:
                user = Usuario.objects.get(userMote=username)
            except Usuario.DoesNotExist:
                return None
        
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None
