from django.http import JsonResponse, HttpRequest, HttpResponse
import json
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
from http import HTTPStatus
from utils.decorators import require_PUT, require_POST
from .models import CustomUser


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
    # TODO: check if the user authorized
    # TODO: update only the the first name, last name, email, or username. Based on what is include in the form data
    user = request.user
    user.save()
    return JsonResponse({'message': 'Update User is active'}, status=HTTPStatus.OK)
