from functools import wraps
from django.http import JsonResponse
from http import HTTPStatus


def require_PUT(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.method != "PUT":
            return JsonResponse({'message': 'Invalid Method'}, status=HTTPStatus.METHOD_NOT_ALLOWED)
        return view_func(request, *args, **kwargs)

    return _wrapped_view


def require_POST(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.method != "POST":
            return JsonResponse({'message': 'Invalid Method'}, status=HTTPStatus.METHOD_NOT_ALLOWED)
        return view_func(request, *args, **kwargs)

    return _wrapped_view


def require_GET(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.method != "GET":
            return JsonResponse({'message': 'Invalid Method'}, status=HTTPStatus.METHOD_NOT_ALLOWED)
        return view_func(request, *args, **kwargs)

    return _wrapped_view


def require_DELETE(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.method != "DELETE":
            return JsonResponse({'message': 'Invalid Method'}, status=HTTPStatus.METHOD_NOT_ALLOWED)
        return view_func(request, *args, **kwargs)

    return _wrapped_view


def require_HEAD(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.method != "HEAD":
            return JsonResponse({'message': 'Invalid Method'}, status=HTTPStatus.METHOD_NOT_ALLOWED)
        return view_func(request, *args, **kwargs)

    return _wrapped_view


def require_CONNECT(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.method != "CONNECT":
            return JsonResponse({'message': 'Invalid Method'}, status=HTTPStatus.METHOD_NOT_ALLOWED)
        return view_func(request, *args, **kwargs)

    return _wrapped_view


def require_TRACE(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.method != "TRACE":
            return JsonResponse({'message': 'Invalid Method'}, status=HTTPStatus.METHOD_NOT_ALLOWED)
        return view_func(request, *args, **kwargs)

    return _wrapped_view


def require_PATCH(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.method != "PATCH":
            return JsonResponse({'message': 'Invalid Method'}, status=HTTPStatus.METHOD_NOT_ALLOWED)
        return view_func(request, *args, **kwargs)

    return _wrapped_view
