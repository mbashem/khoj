from django.db import models

# Create your models here.
class myblogs(models.Model):
    blog_id = models.AutoField
    blog_name = models.CharField(max_length=25)
    blog_desc = models.CharField(max_length=100)
    publish_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.blog_name