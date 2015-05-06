"""
API client for the IT Technical API.

This API client expects to follow JSend specification for responses of the API.

api = ITTechnialAPI(key)
r = api.call("/api/v1.1/jira/get/top/10")

"""

from .base import APIClient_SharedSecret
from urllib import urlencode
from config import API_VERSION


class ITTechnicalAPIError(Exception):
    """Exceptions for Technical API"""

    # For reference.
    STATUS_MAP = {
        200: "200 OK: Success",
        202: "202 Accepted: Your request was accepted and the user was queued for processing.",
        401: "401 Not Authorized: either you need to provide authentication credentials, or the credentials "
             "provided aren't valid.",
        403: "403 Bad Request: your request is invalid, and we'll return an error message that tells you why. "
             "This is the status code returned if you've exceeded the rate limit (see below).",
        404: "404 Not Found: either you're requesting an invalid URI or the resource in question doesn't "
             "exist (ex: no such user in our system).",
        500: "500 Internal Server Error: we did something wrong.",
        501: "501 Not implemented.",
        502: "502 Bad Gateway: returned if ITAPI is down or being upgraded.",
        503: "503 Service Unavailable: the ITAPI servers are up, but are overloaded with requests. Try again later.",
    }

    def __init__(self, type, message, status, response=None):
        self.type = type
        self.message = message
        self.response = response
        self.status = status

    def __str__(self):
        return "%s (%s)" % (self.message, self.STATUS_MAP[self.status])

    def __repr__(self):
        return "%s (status=%s)" % (self.message, self.STATUS_MAP[self.status])


class ITTechnicalAPI(APIClient_SharedSecret):
    BASE_URL = "https://itapi.samskip.com/api/"+API_VERSION+"/"

    def _compose_url(self, path, params=None):
        p = dict(key=self.api_key, **(params or {}))

        if params:
            p.update(params)

        return self.BASE_URL + path + "?" + urlencode(p)

    def _handle_response(self, response):

        try:
            r = super(ITTechnicalAPI, self)._handle_response(response)
        except ValueError:
            r = dict(status="error", message="malformed JSON")

        has_error = r.get('status') == "error"
        if not has_error:
            return r

        raise ITTechnicalAPIError(r.get('type'), r.get('message'), status=response.status, response=r)