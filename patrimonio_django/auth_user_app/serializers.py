from django.contrib.auth import authenticate
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user is None:
            raise serializers.ValidationError('Credenciales inválidas')
        attrs['user'] = user  # Guarda el usuario en validated_data
        return attrs
    
from django.contrib.auth import get_user_model 
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=[User.ADMIN, User.GESTOR, User.USUARIO], required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'role']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            role=validated_data.get('role', User.USUARIO)  # Asignar rol por defecto
        )
        user.set_password(validated_data['password'])  # Asegurarse de que la contraseña esté encriptada
        user.save()
        return user