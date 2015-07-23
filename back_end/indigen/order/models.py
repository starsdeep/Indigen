from django.db import models

CREATE = 'CR'
CONFIRM = 'CF'
SUCCESS = 'SC'
AUTO_CANCEL = 'AC'
REJECT = 'RJ'

STATUS_CHOICES = (
    (CREATE, 'create'),
    (CONFIRM, 'confirm'),
    (SUCCESS, 'success'),
    (AUTO_CANCEL, 'auto cancel by system'),
    (REJECT, 'reject by seller')
)


class OrderStatus(models.Model):
    class Meta:
        unique_together = ["order", 'status']

    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    change_at = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey('AdviceOrder')


class Order(models.Model):
    display_id = models.CharField(unique=True, max_length=50, null=False)

    buyer = models.ForeignKey('authentication.User')
    seller = models.ForeignKey('authentication.User')

    seller_reply_average_second = models.IntegerField(null=True)
    buyer_reply_average_second = models.IntegerField(null=True)

    buyer_to_seller_comment = models.CharField(max_length=300,null=True)
    buyer_to_seller_star = models.IntegerField(null=True)

    seller_to_buyer_comment = models.CharField(max_length=300,null=True)
    seller_to_buyer_star = models.IntegerField(null=True)

    create_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField()

    price = models.DecimalField(max_digits=10, decimal_places=2)



