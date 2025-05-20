from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Employer
from .serializers import EmployerSerializer
from django.shortcuts import get_object_or_404
from .utils import custom_response
# Create your views here.

class EmployerListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employers = Employer.objects.filter(user=request.user)
        serializer = EmployerSerializer(employers, many=True)
        return custom_response(True, "Employers fetched", serializer.data)

    def post(self, request):
        serializer = EmployerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return custom_response(True, "Employer created", serializer.data)
        return custom_response(False, "Validation error", serializer.errors)

class EmployerDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        return get_object_or_404(Employer, pk=pk, user=user)

    def get(self, request, pk):
        employer = self.get_object(pk, request.user)
        serializer = EmployerSerializer(employer)
        return custom_response(True, "Employer details fetched", serializer.data)

    def put(self, request, pk):
        employer = self.get_object(pk, request.user)
        serializer = EmployerSerializer(employer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return custom_response(True, "Employer updated", serializer.data)
        return custom_response(False, "Validation error", serializer.errors)

    def delete(self, request, pk):
        employer = self.get_object(pk, request.user)
        employer.delete()
        return custom_response(True, "Employer deleted")
