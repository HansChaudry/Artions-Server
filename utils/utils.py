from users.models import CustomUser
from artworks.models import Artwork
from auctions.models import Auction
from django.db.models.query import QuerySet


def format_user_objects(users: QuerySet[CustomUser]) -> list:
    formatted_objects = []
    for user in users:
        temp = {
            "username": user.username,
            "id": user.id,
            "following": user.following,
            "followers": user.followers,
            "profileIMG": user.profileIMG
        }
        formatted_objects.append(temp)
    return formatted_objects


def format_user_profile(user: CustomUser) -> dict:
    user_profile = {
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "followers": user.followers,
        "following": user.following,
        # "artwork_count": Artwork.objects.filter(user_id=user).count(),
        # "artworks": Artwork.objects.filter(user_id=user)
        # "auctions": Auction.objects.filter(user_id=user)
    }
    return user_profile
