from django.contrib.auth.models import User, Group
from rest_framework import serializers
from news_app.models import Tag, Category, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "groups"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "feature_image",
            "views_count",
            "status",
            "published_at",
            "author",
            "category",
            "tag",
        ]
        
    def validate(self, data):
        data["author"]= self.context["request"].user
        return data