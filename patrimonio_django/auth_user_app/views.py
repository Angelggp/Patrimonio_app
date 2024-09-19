from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer, RegisterSerializer
# from .models import User



class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']  # Obtiene el usuario autenticado
        refresh = RefreshToken.for_user(user)
        
        tokens = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'username': user.username,  # Agrega el campo username
            'role': user.role,
        }

        return Response(tokens, status=200)


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "username": user.username,
                "role": user.role,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()  # Obtiene todos los usuarios
#     serializer_class = UserSerializer  # Serializador para los usuarios
#     permission_classes = [IsAuthenticated]  # Asegúrate de que solo los usuarios autenticados puedan acceder

#     def get(self, request, *args, **kwargs):
#         users = self.get_queryset()
#         serializer = self.get_serializer(users, many=True)
#         return Response(serializer.data, status=200)