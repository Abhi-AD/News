from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from API.serializers import (
    UserSerializer,
    GroupSerializer,
    TagSerializer,
    CategorySerializer,
    PostSerializer,
    PostPublishSerializer,
    # NewsletterSerializer,
)
from news_app.models import Tag, Category, Post, Newsletter
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
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
        if self.action in ["list", "retrieve"]:
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
        if self.action == ["list", "retrieve"]:
            return [permissions.AllowAny()]
        return super().get_permissions()


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Posts to be viewed or edited.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        querset = super().get_queryset()
        if self.action in ["list", "retrieve"]:
            querset = querset.filter(status="active", published_at__isnull=False)
        return querset

    def get_permissions(self):
        if self.action == ["list", "retrieve"]:
            return [permissions.AllowAny()]
        return super().get_permissions()


class DraftListViewSet(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        queryset =  super().get_queryset()
        queryset = queryset.filter(published_at__isnull=True)
        return queryset
        
    

class PostListByCategoryViewSet(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = super().get_querset()
        queryset = queryset.filter(
            status="active",
            published_at__isnull=False,
            category=self.kwargs["category_id"],
        )
        return queryset


class PostListByTagViewSet(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = super().get_querset()
        queryset = queryset.filter(
            status="active",
            published_at__isnull=False,
            tag=self.kwargs["tag_id"],
        )
        return queryset


class PostPublishViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostPublishSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.data

            # published the post
            post = Post.objects.get(pk=data["post"])
            post.published_at = timezone.now()
            post.save()

            serialized_data = PostSerializer(post).data
            return Response(serialized_data, status=status.HTTP_200_OK)


# class NewsletterViewSet(viewsets.ModelViewSet):
#     queryset = Newsletter.objects.all()
#     serializer_class = NewsletterSerializer
#     permission_classes=[permissions.AllowAny]
    
    
#     def get_permissions(self):
#         if self.action in ["list","retrieve"]:
#             return[permissions.IsAuthenticated]
#         return super().get_permissions()
    
#     def update(self, request, *args, **kwargs):
#         raise Exception.MethodNotAllowed(request.method)
