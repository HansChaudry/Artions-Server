from functools import wraps
from django.http import JsonResponse
from http import HTTPStatus

def require_http_method(method):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.method != method:
                return JsonResponse({'message': 'Invalid Method'}, status=HTTPStatus.METHOD_NOT_ALLOWED)
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator

require_PUT = require_http_method("PUT")
require_POST = require_http_method("POST")
require_GET = require_http_method("GET")
require_DELETE = require_http_method("DELETE")
require_HEAD = require_http_method("HEAD")
require_CONNECT = require_http_method("CONNECT")
require_TRACE = require_http_method("TRACE")
require_PATCH = require_http_method("PATCH")
