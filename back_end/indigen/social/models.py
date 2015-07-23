from django.db import models

# Create your models here.
class Visit(models.Model):
    from_user = models.ForeignKey('authentication.User', null=True)
    to_user = models.ForeignKey('authentication.User', null=False)
    ip = models.IPAddressField(null=True)
    visit_length_second = models.IntegerField(null=True)

class FriendRequest(models.Model):
    from_user = models.ForeignKey('authentication.User')
    to_user = models.ForeignKey('authentication.User')

    request_at = models.DateTimeField(auto_now_add=True)
    is_dealt = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)
    deal_at = models.DateTimeField(null=True)


class Friend(models.Model):

    class Meta:
        unique_together = ('user_1', 'user_2')
    user_1 = models.ForeignKey('authentication.User', db_index=False)
    user_2 = models.ForeignKey('authentication.User', db_index=False)
    become_at = models.DateTimeField(auto_now=True)


