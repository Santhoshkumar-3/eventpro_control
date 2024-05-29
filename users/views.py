from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserProfileSerializer,
    ChangePasswordSerializer,
    CustomUserSerializer,
)
from rest_framework.exceptions import PermissionDenied

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

class UserLoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)

        return Response({
            'id': user.id,  
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'role': user.role,
        })

class UserProfileView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        if request.user.id != int(kwargs['pk']):  
            raise PermissionDenied("You do not have permission to access this resource.")

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class ChangePasswordView(APIView):
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        if not user.check_password(serializer.validated_data['old_password']):
            return Response({'error': 'Incorrect old password'}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        return Response({'success': 'Password changed successfully'}, status=status.HTTP_200_OK)


class StudentUserList(generics.ListAPIView):
    queryset = CustomUser.objects.filter(role='student')
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    

class StaffUserList(generics.ListAPIView):
    queryset = CustomUser.objects.filter(role='staff')
    serializer_class = CustomUserSerializer
