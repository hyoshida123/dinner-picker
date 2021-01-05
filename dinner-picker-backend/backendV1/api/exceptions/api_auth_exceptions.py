"""
API exceptions that can occur while authorization is processing.

@author: SangBin Cho
"""

from rest_framework.exceptions import APIException
from rest_framework import status

class APIInvalidateAccessTokenException(APIException):
    #TODO change this code to 401: Frank said 401 causes an error
    status_code = 404
    default_code = 'invalid access token provided'