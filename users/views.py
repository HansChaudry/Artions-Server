from django.http import JsonResponse, HttpRequest, HttpResponse
import json
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
from http import HTTPStatus
from utils.decorators import require_PUT, require_POST, require_GET
from .models import CustomUser, Follow
from django.forms.models import model_to_dict
from django.http.multipartparser import MultiPartParser


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the users index.")


def create_message(msg: str):
    return json.dumps({"message": msg})


@require_POST
def user_register(request: HttpRequest) -> HttpResponse:
    user_info = request.POST.dict()
    form = CustomUserCreationForm(user_info)

    if form.is_valid():
        user = form.save()
        return JsonResponse({'message': "User Created", 'user_id': user.id}, status=HTTPStatus.OK)

    return JsonResponse({'errors': form.errors.get_json_data()}, status=HTTPStatus.BAD_REQUEST)


@require_POST
def user_sign_in(request: HttpRequest) -> HttpResponse:
    user_info = request.POST.dict()
    username = user_info.get("username")
    password = user_info.get("password")

    if not username or not password:
        return JsonResponse(
            {'message': "Please provide both username and password."},
            status=HTTPStatus.BAD_REQUEST
        )

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({"user_id": user.id}, status=HTTPStatus.OK)

    return JsonResponse(
        {
            'message': "Invalid credentials. Please enter a correct username and password. Note that both fields "
                       "maybe be case-sensitive."},
        status=HTTPStatus.UNAUTHORIZED
    )


@require_POST
def user_sign_out(request: HttpRequest) -> HttpResponse:
    logout(request)
    return JsonResponse({'message': 'User logged out'}, status=HTTPStatus.OK)


@require_PUT
def update_user(request: HttpRequest) -> HttpResponse:
    user = request.user
    if user.is_authenticated:
        new_user_info = MultiPartParser(request.META, request, request.upload_handlers).parse()[0]
        if new_user_info == {}:
            return JsonResponse({'message': 'Missing first name, last name, email, or username fields'},
                                status=HTTPStatus.BAD_REQUEST)

        user.first_name = user.first_name if 'first_name' not in new_user_info else new_user_info.get("first_name")
        user.last_name = user.last_name if 'last_name' not in new_user_info else new_user_info.get("last_name")
        user.email = user.email if 'email' not in new_user_info else new_user_info.get("email")
        user.username = user.username if 'username' not in new_user_info else new_user_info.get("username")
        user.save()
        return JsonResponse({'message': 'User Information Updated'}, status=HTTPStatus.OK)
    else:
        return JsonResponse({'message': 'Unauthenticated user'}, status=HTTPStatus.UNAUTHORIZED)


@require_GET
def get_user_details(request: HttpRequest) -> HttpResponse:
    user = request.user
    if user.is_authenticated:
        selected_keys = ['username', 'email', 'first_name', 'last_name', "followers", "following"]
        new_dict = {key: model_to_dict(user)[key] for key in selected_keys}
        return JsonResponse(new_dict, status=HTTPStatus.OK)
    else:
        return JsonResponse({'message': 'Unauthenticated user'}, status=HTTPStatus.UNAUTHORIZED)


@require_GET
def get_followers(request: HttpRequest) -> HttpResponse:
    user = request.user
    if user.is_authenticated:
        user_followers = Follow.objects.filter(followee_id=user)
        print(user_followers)
        return JsonResponse({'message': 'ok'}, status=HTTPStatus.OK)
    else:
        return JsonResponse({'message': 'Unauthenticated user'}, status=HTTPStatus.UNAUTHORIZED)


@require_GET
def get_following(request: HttpRequest) -> HttpResponse:
    user = request.user
    if user.is_authenticated:
        user_following = Follow.objects.filter(follower_id=user)
        print(user_following)
        return JsonResponse({'message': 'ok'}, status=HTTPStatus.OK)
    else:
        return JsonResponse({'message': 'Unauthenticated user'}, status=HTTPStatus.UNAUTHORIZED)


@require_POST
def follow_user(request: HttpRequest, username: str) -> HttpResponse:
    user = request.user
    if user.is_authenticated:
        try:
            followee = CustomUser.objects.get(username=username)
            follower = CustomUser.objects.get(username=user.username)
            Follow.objects.create(follower_id=user, followee_id=followee)
            follower.following += 1
            follower.save()
            followee.followers += 1
            followee.save()

            return JsonResponse({'message': user.username + ' is now following ' + followee.username},
                                status=HTTPStatus.OK)
        except CustomUser.DoesNotExist:
            return JsonResponse({'message': 'User ' + username + ' not found'}, status=HTTPStatus.BAD_REQUEST)

    else:
        return JsonResponse({'message': 'Unauthenticated user'}, status=HTTPStatus.UNAUTHORIZED)


@require_POST
def unfollow_user(request: HttpRequest, username: str) -> HttpResponse:
    user = request.user
    if user.is_authenticated:
        try:
            followee = CustomUser.objects.get(username=username)
            follower = CustomUser.objects.get(username=user.username)
            Follow.objects.get(follower_id=user, followee_id=followee).delete()
            follower.following -= 1
            follower.save()
            followee.followers -= 1
            followee.save()

            return JsonResponse({'message': user.username + ' is no longer following ' + username},
                                status=HTTPStatus.OK)
        except CustomUser.DoesNotExist:
            return JsonResponse({'message': 'User ' + username + ' not found'}, status=HTTPStatus.BAD_REQUEST)
        except Follow.DoesNotExist:
            return JsonResponse({'message': 'User ' + user.username + ' does not follow' + username},
                                status=HTTPStatus.BAD_REQUEST)

    else:
        return JsonResponse({'message': 'Unauthenticated user'}, status=HTTPStatus.UNAUTHORIZED)


@require_GET
def get_followers(request: HttpRequest) -> HttpResponse:
    user = request.user
    if user.is_authenticated:
        try:
            user_follows = Follow.objects.filter(followee_id=user).select_related("followee_id")
            if len(user_follows) == 0:
                return JsonResponse({'message': "user has no followers"}, status=HTTPStatus.OK)
            followers = []
            for follow in user_follows:
                followers.append({"username": follow.follower_id.username, "profileIMG": follow.follower_id.profileIMG})
            return JsonResponse({'followers': followers}, status=HTTPStatus.OK)
        except CustomUser.DoesNotExist:
            return JsonResponse({'message': user.username + ' not found'}, status=HTTPStatus.BAD_REQUEST)
    else:
        return JsonResponse({'message': 'Unauthenticated user'}, status=HTTPStatus.UNAUTHORIZED)


@require_GET
def get_following(request: HttpRequest) -> HttpResponse:
    user = request.user
    if user.is_authenticated:
        try:
            user_follows = Follow.objects.filter(follower_id=user).select_related("followee_id")
            if len(user_follows) == 0:
                return JsonResponse({'message': "user has no followings"}, status=HTTPStatus.OK)
            following = []
            for follow in user_follows:
                following.append(
                    {"username": follow.followee_id.username, "profileIMG": follow.followee_id.profileIMG})
            return JsonResponse({'followers': following}, status=HTTPStatus.OK)
        except CustomUser.DoesNotExist:
            return JsonResponse({'message': user.username + ' not found'}, status=HTTPStatus.BAD_REQUEST)
    else:
        return JsonResponse({'message': 'Unauthenticated user'}, status=HTTPStatus.UNAUTHORIZED)
