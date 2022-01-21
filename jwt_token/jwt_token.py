import jwt.exceptions
import rest_framework_simplejwt.exceptions
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from myplanit.settings import env
from accounts.models import User
import jwt


def get_user(pk):
    return get_object_or_404(User, pk=pk)


def get_token(request):
    try:
        access_token = request.data['access_token']
        payload = jwt.decode(access_token, env('DJANGO_SECRET_KEY'), algorithms=['HS256'])
        pk = payload.get('user_id')
        user = get_user(pk)
        refresh_token = request.data['refresh_token']
        return user, access_token, refresh_token

    # 토큰 만료시 토큰 갱신
    except jwt.exceptions.ExpiredSignatureError:
        try:
            print("access token 만료")
            serializer = TokenRefreshSerializer(data={'refresh': request.data['refresh_token']})

            if serializer.is_valid(raise_exception=True):
                access_token = serializer.validated_data['access']
                refresh_token = request.data['refresh_token']
                payload = jwt.decode(access_token, env('DJANGO_SECRET_KEY'), algorithms=['HS256'])
                pk = payload.get('user_id')
                user = get_user(pk)
                return user, access_token, refresh_token

        except rest_framework_simplejwt.exceptions.TokenError:
            print("refresh 토큰도 만료")
            return None

        raise jwt.exceptions.InvalidTokenError

    except jwt.exceptions.InvalidTokenError:
        return None