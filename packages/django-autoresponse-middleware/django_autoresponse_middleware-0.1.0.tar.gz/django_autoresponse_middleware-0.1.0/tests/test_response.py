import json

from django.http import HttpResponse, JsonResponse
from django.test import RequestFactory

from django_autoresponse_middleware import middleware


def call_middleware(response):
    req = RequestFactory().get("/")

    return middleware(lambda x: response)(req)


def test_basic():
    data = "123"
    response = HttpResponse(data)

    res = call_middleware(response)

    assert isinstance(res, HttpResponse)
    assert res == response
    assert res.content.decode() == data
    assert res.status_code == 200


def test_json():
    data = {"a": 1, "b": 2}

    res = call_middleware(data)

    assert isinstance(res, HttpResponse)
    assert isinstance(res, JsonResponse)
    assert json.loads(res.content) == data
    assert res.status_code == 200


def test_basic_400():
    data = "unauthorized"
    response = HttpResponse(data, status=400)

    res = call_middleware((response, 400))

    assert isinstance(res, HttpResponse)
    assert res == response
    assert res.status_code == 400


def test_json_500():
    data = {"error": "server error"}
    res = call_middleware((data, 500))

    assert isinstance(res, JsonResponse)
    assert json.loads(res.content) == data
    assert res.status_code == 500


def test_headers():
    data = "123"
    status = 201
    headers = {"X-Test": "test"}
    response = HttpResponse(data, status=status, headers=headers)

    res = call_middleware((response, status, headers))

    assert isinstance(res, HttpResponse)
    assert res == response
    assert res.status_code == status
    assert res["X-Test"] == "test"
