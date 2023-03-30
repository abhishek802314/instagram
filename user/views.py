from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import User, UserImage
from .permissions import IsOwner, IsOwnerUser
from .serializers import UserSerializerList, UserImageSerializer, UserSerializer, MySerializerList


class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializerList

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destory']:
            return (IsOwnerUser(),)
        
        else:
            return (permissions.AllowAny(),)
        

    def get_serializer_class(self):
        if self.action == 'list':
            return UserSerializerList
        elif self.action in ['update', 'partial_update', 'destroy']:
            return MySerializerList
        return UserSerializer
    
class UserProfilePhotoApiView(viewsets.ModelViewSet):
    queryset = UserImage.objects.all()
    serializer_class = UserImageSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destory']:
            return (IsOwnerUser(),)
        else:
            return (permissions.AllowAny(),)
        
    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)