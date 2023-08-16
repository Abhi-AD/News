from django.contrib.auth.models import User, Group
from rest_framework import serializers
from news_app.models import Tag, Category, Post, Newsletter,Contact,Comment


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
        extra_kwargs = {
            "author":{"read_only":True},
            "views_count":{"read_only":True},
            "published_at":{"read_only":True}
        }
        
    def validate(self, data):
        data["author"]= self.context["request"].user
        return data
    

class PostPublishSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    
class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        field = "_all_"
        

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        field = "_all_"
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        field = "_all_"