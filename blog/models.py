from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #manyToOne Relation

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
    
# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     comment = models.TextField(max_length=400)
#     created_on = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['created_on']

#     def __str__(self):
#         return self.comment[:60]
    
    