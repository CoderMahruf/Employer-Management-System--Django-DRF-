from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .serializers import SignupSerializer, LoginSerializer, UserProfileSerializer
from .models import User
from .utils import custom_response

class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return custom_response(True, "User registered successfully")
        return custom_response(False, "Validation error", serializer.errors)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return custom_response(True, "Login successful", {
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            })
        return custom_response(False, "Invalid credentials", serializer.errors)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return custom_response(True, "Profile fetched", serializer.data)
