from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=250)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    # image = models.ImageField(null=False, blank=False, width_field=width, height_field=height)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)




    class Meta:
        ordering = ["-timestamp"]