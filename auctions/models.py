from django.db import models
from users.models import CustomUser
from artworks.models import Artwork

# Create your models here.

class Auction(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    artwork_id = models.ForeignKey(Artwork, on_delete=models.CASCADE, null=True)
    starting_bid = models.IntegerField('starting_bid', blank=True, default=0)
    current_bid = models.IntegerField('current_bid', blank=True, default=0)
    end_time = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=0, null=True)


class Bid(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField('following', blank=True, default=0)
    timestamp = models.DateTimeField(null=True)