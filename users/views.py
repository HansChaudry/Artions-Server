from django.http import JsonResponse, HttpRequest, HttpResponse
import json
from .forms import CustomUserCreationForm
from django.db.models import QuerySet
from .models import CustomUser
from django.contrib.auth import login, logout, authenticate
from django.forms.models import model_to_dict
from http import HTTPStatus


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the users index.")


def create_message(msg: str):
    return json.dumps({"message": msg})


def user_register(request: HttpRequest) -> HttpResponse:
    if request.method != "POST":
        return HttpResponse(create_message("Invalid Method"), status=HTTPStatus.METHOD_NOT_ALLOWED)
    user_info: dict = request.POST.dict()
    form = CustomUserCreationForm(user_info)
    if form.is_valid():
        form.save()
        users_query: QuerySet = CustomUser.objects.get(username=user_info.get("username"))
        user = model_to_dict(users_query)

        return HttpResponse(create_message("User Created"), status=HTTPStatus.OK)
    return HttpResponse(json.dumps(form.errors.get_json_data()))


def user_sign_in(request: HttpRequest) -> HttpResponse:
    if request.method != "POST":
        return HttpResponse(create_message("Invalid Method"), status=HTTPStatus.METHOD_NOT_ALLOWED)
    user_info: dict = request.POST.dict()
    user = authenticate(
        username=user_info["username"],
        password=user_info["password"])
    if user is not None:
        login(request, user)
        return HttpResponse(json.dumps({"user_id": user.id}), status=HTTPStatus.OK)
    return HttpResponse(json.dumps({'message': "Please enter a correct username and password.\n\nNote that both "
                                               "fields may be case-sensitive."}), status=HTTPStatus.BAD_REQUEST)


def user_sign_out(request: HttpRequest) -> HttpResponse:
    logout(request)
    return HttpResponse(json.dumps({'message': 'User logged out'}), status=HTTPStatus.OK)
