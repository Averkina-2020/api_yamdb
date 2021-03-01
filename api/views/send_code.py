import os

from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# load_dotenv()
from api.models import TempAuth, User
from api.serializers.userserializer import UserSerializer

# from dotenv import load_dotenv



def send_code(self, request):
    if not request.user.is_authenticated:
        if request.POST:
            # Пользователь отправляет POST-запрос с параметром email
            email = request.POST.get('email', '')
            try:
                temp_object = TempAuth.objects.get(email=email)
                conf_code = temp_object.conf_code
            except TempAuth.DoesNotExist:
                conf_code = get_random_string(length=62)
                # создать данные
                TempAuth.objects.create(email=email, conf_code=conf_code)
            # YaMDB отправляет письмо с кодом подтверждения
            # (confirmation_code) на адрес email .
            send_mail(
                'Email confirmation',
                f'Your confirmation code: {conf_code}',
                from_email=os.environ.get('EMAIL_HOST_USER'),
                recipient_list=[f'{email}'],
                fail_silently=False)


def get_jwt_token(self, request):
    username = request.data.get('username')

    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
    else:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
        else:
            return Response(serializer.errors)

    token = Token.objects.get_or_create(user=user)
    return Response(str(token))
