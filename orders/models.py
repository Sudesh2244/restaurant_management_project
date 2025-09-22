from django.db import models

# Create your models here.
from django.db import modelsfrom .order_status import OrderStatus
 class Order(model.Models):
    status = models.ForeignKey(
        OrderStatus,
        on_delete = models.SET_NULL,
        null = True,
        blank = True

    )

    def __str__(self):
        return F"Order #{self.id} - {self.stutus}"