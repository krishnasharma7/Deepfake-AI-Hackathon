from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Video
from .utils import del_video_file

@receiver(post_delete, sender=Video)
def signal_function(sender, instance, using, **kwargs):
    del_video_file(instance.video)