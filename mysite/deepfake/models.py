from django.db import models
from .validators import file_size
from django.contrib.auth.models import User
# Create your models here.

class Video(models.Model):
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y", validators=[file_size])
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    pred_class = models.CharField(max_length=100, default="Default")

    def __str__(self):
        return self.caption