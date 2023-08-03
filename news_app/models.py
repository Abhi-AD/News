from django.db import models

# Create your models here.
class TimesStampModel(models.Model):
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     
     class Meta:
          abstract = True #Don't create table in DB
     
class Category(models.Model):
     name = models.CharField(max_length=100)
     def __str__(self):
          return self.name
     
class Tag(models.Model):
     name = models.CharField(max_length=100)     
     def __str__(self):
          return self.name
     





class Post(models.Model):
     STATUS_CHOICES = [
          ("active", "Active"),
          ("in_active", "Inactive"),
     ]
     title = models.CharField(max_length=255)
     content = models.TextField()
     feature_image = models.ImageField(upload_to="post_images/%Y/%m/%d", blank=False)
     author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
     views_count = models.PositiveBigIntegerField(default=0)
     published_at = models.DateField(null=True, blank=True)
     category = models.ForeignKey(Category, on_delete=models.CASCADE)
     tag = models.ManyToManyField(Tag)
     
     def __str__(self):
          return self.title
     
class Contact(TimesStampModel):
     message = models.TextField()
     name = models.CharField(max_length=100)
     email = models.EmailField()
     subject = models.CharField(max_length=200)
     
     def __str__(self):
          return self.name
     
     
class UserProfile(models.Model):
     user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
     image = models.ImageField(upload_to="user_images/%Y/%m/%d", blank=False)
     address = models.CharField(max_length=255)
     biography = models.TextField()
     
     def __str__(self):
          return self.user
     
class Comment(TimesStampModel):
     post = models.ForeignKey(Post, on_delete=models.CASCADE)
     comment = models.TextField()
     name = models.CharField(max_length=255)
     email = models.EmailField()
     
     def __str__(self):
          return f"{self.email} | {self.comment[:70]}"
     
     
     
class Newsletter(TimesStampModel):
     email = models.EmailField(unique=True)
     
     def __str__(self):
          return f"{self.email}"