from django.db import models


# Create your models here.

class Blogs(models.Model):

    title = models.CharField(max_length=50)
    blog_content = models.CharField(max_length=200, verbose_name='content', error_messages ={
                    "max-length":"The Blog content Exceeds the Maximum Length '200'"})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"


