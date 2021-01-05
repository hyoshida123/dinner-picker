"""
API Exceptions that can occur when database task is processing

@author: SangBin Cho
"""

from rest_framework.exceptions import APIException
from rest_framework import status

class APIDatabaseSaveFailedException(APIException):
    status_code = 400
    default_code = 'fail to save data into database'

class APIDatabaseRetrieveFailedException(APIException):
    status_code = 400
    default_code = 'fail to get data from database'

class APIDatabaseUpdateFailedException(APIException):
    status_code = 400
    default_code = 'fail to update data from database'

class APIDatabaseDeleteFailedException(APIException):
    status_code = 400
    default_code = 'fail to delete data from database'