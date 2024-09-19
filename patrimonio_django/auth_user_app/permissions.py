from rest_framework.permissions import BasePermission
from rest_framework.views import APIView


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == User.ADMIN

class IsGestor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [User.ADMIN, User.GESTOR]

class IsUsuario(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [User.ADMIN, User.GESTOR, User.USUARIO]
    

class SomeAdminView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        """
        Lógica para administradores.
        Retorna datos específicos para administradores.
        """
        try:
            # Implementa la lógica para administradores
            data = {"message": "Datos para administradores."}
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SomeGestorView(APIView):
    permission_classes = [IsGestor]

    def get(self, request):
        """
        Lógica para gestores.
        Retorna datos específicos para gestores.
        """
        try:
            # Implementa la lógica para gestores
            data = {"message": "Datos para gestores."}
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SomeUsuarioView(APIView):
    permission_classes = [IsUsuario]

    def get(self, request):
        """
        Lógica para usuarios comunes.
        Retorna datos específicos para usuarios comunes.
        """
        try:
            # Implementa la lógica para usuarios comunes
            data = {"message": "Datos para usuarios comunes."}
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)