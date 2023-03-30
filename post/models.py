from django.db import models
from django.utils import timezone
from user.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}---{self.user.username}"
    
    class Meta:
        ordering = ['create_at']


class UserReadTime(models.Model):
    post = models.ForeignKey(Post, related_name='post_is_read', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_rt', on_delete=models.CASCADE)
    read_time = models.DateTimeField(timezone.now)

    def __str__(self):
        return f'{self.user}:{self.read_time}'
    
    
class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='post_images', on_delete=models.CASCADE)
    image = models.ImageField()


    def __str__(self):
        return f"{self.post.title}---{self.post.user.username}"
    
    class Meta:
        ordering = ['id']


class PostsLike(models.Model):
    post = models.ForeignKey(Post, related_name='post_for_like', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_like', on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user}: {self.post}: {self.like}'
    