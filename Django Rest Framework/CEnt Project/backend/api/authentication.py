from rest_framework.authentication import TokenAuthentication as BaseTokenAuth
from rest_framework.authtoken.models import Token as Tkn


class TokenAuthentication(BaseTokenAuth):
    keyword = "Bearer"
