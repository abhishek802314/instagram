from django.shortcuts import render
from django.utils import timezone
from rest_framework import viewsets, permissions, generics

from .serializers import PostSerializer, PostImageSerializer, PostLikeSerializer
from .models import Post, PostImage, PostsLike, UserReadTime
from user.models import User
from user.permissions import IsOwner, IsPostOwner

class PostApiViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsOwner(), )
        else:
            return (permissions.IsAuthenticated(),)
        
    def get_queryset(self):
        return Post.objects.filter(user__is_private=False)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    

class PostImageApiViewSet(viewsets.ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsOwner(), )
        else:
            return (permissions.IsAuthenticated(),)
        

class PostLikeApiViewSet(viewsets.ModelViewSet):
    queryset = PostsLike.objects.all()
    serializer_class = PostLikeSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsOwner(), )
        else:
            return (permissions.IsAuthenticated(),)
        
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
# class InstagramFeedApiView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticated]


#     def get(self, request, *args, **kwargs):
#         user = request.user
#         readed_post = []
#         users = []
