from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def sign(request):
    if request.method == "POST":

        name = request.data.get('name')
        user = request.data.get('username')
        passwords = request.data.get('password')

        user_created = User.objects.create_user(user, "", passwords, first_name=name)
        refresh = RefreshToken.for_user(user_created)
        if(user_created):
            a = {'status' : 201,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                    }
            return Response(a)


@api_view(['POST'])
def login_view(request):

    if request.method == "POST":

            user = authenticate(username=request.data["username"], password=request.data["password"])

            if user is not None:
                login(request, user)
                username = user.username
                ownerno = user.id
                refresh = RefreshToken.for_user(user)
                a = {'status': 201,
                     'refresh': str(refresh),
                     'access': str(refresh.access_token),
                     'user': username,
                     'ownerno': ownerno,
                     }
                return Response(a)
            else:
                return Response("User doesn`t exist!")

            return Response("")


@api_view(['GET'])
def logout_view(request):
    logout(request)
    return Response("You are logged out!")

