from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from API.serializers import UserSerializer, GroupSerializer,TagSerializer,CategorySerializer,PostSerializer
from news_app.models import Tag,Category,Post


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tags to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_permissions(self):
        if self.action in ["list","retrieve"]:
            return [permissions.AllowAny()]
        return super().get_permissions()
    
class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tag to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_permissions(self):
        if self.action == ["list","retrieve"]:
            return [permissions.AllowAny()]
        return super().get_permissions()
    
class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tag to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        querset= super().get_queryset()
        if self.action in ["list","retrieve"]:
            querset = querset.filter(status="active", published_at__isnull = False)
        return querset

    
    def get_permissions(self):
        if self.action == ["list","retrieve"]:
            return [permissions.AllowAny()]
        return super().get_permissions()