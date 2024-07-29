from enum import Enum

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse

__author__ = 'dpepper'
__version__ = '0.1.0'

__all__ = ["encoder", "middleware"]

encoder = DjangoJSONEncoder


def middleware(get_response):
    def middleware(request):
        response = get_response(request)

        if isinstance(response, HttpResponse):
            return response

        opts = {}

        if isinstance(response, tuple):
            if len(response) > 3:
                raise ValueError(
                    f"expected value and status code, found: {response}",
                )

            # extend to full length and unpack
            response += (None,) * (3 - len(response))
            response, status, headers = response

            # sanity checks
            if status:
                if not isinstance(status, (int, Enum)):
                    raise ValueError(
                        f"expected status code, found: {status}",
                    )

                opts["status"] = status

            if headers:
                if not isinstance(headers, dict):
                    raise ValueError(
                        f"expected headers dict, found: {response[-1]}",
                    )
                opts["headers"] = headers

        if isinstance(response, str):
            return HttpResponse(response, **opts)

        if isinstance(response, dict):
            return JsonResponse(response, encoder=encoder, **opts)

        return response

    return middleware
