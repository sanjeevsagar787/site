from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key= True)
    tilte = models.CharField(max_length=50)
    tilte_post = models.TextField()
    heading2 = models.CharField(max_length=50)
    post2 = models.TextField()
    About = models.TextField()
    slug = models.CharField(max_length=130)
    pub_date = models.DateField(null=True, blank=True)



    def __str__(self):
        return  self.tilte
class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)