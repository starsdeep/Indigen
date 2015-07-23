from django.db import models

# Create your models here.
class Notification(models.Model):
    to_user = models.ForeignKey('authentication.User')
    content = models.CharField(max_length=500)
    send_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
