# from django.shortcuts import render, get_object_or_404
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import *
# from .serializers import *

# # Create your views here.

# def get_user(request, pk):
#     user_information = get_object_or_404(User, pk=pk)
#     serializer = UserSerializer(user_information)
#     return Response(serializer.data, status=404)