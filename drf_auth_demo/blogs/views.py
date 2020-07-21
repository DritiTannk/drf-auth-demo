from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from rest_framework import viewsets, serializers

from .models import Blogs
from .serializers import BlogSerializer



class BlogsView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer
