__author__ = 'haukurk'

from flask import request, jsonify
from technicalapiclient.apiclient import ITTechnicalAPI, ITTechnicalAPIError
from config import API_KEY

itapi = ITTechnicalAPI(API_KEY)


def apicall(path, fields={}):
    """
    Proxy Route for IT API.
    """

    if request.form:
        fields["jql"] = request.form['jql']

    if request.method == "GET":
        return api_call_get(path)
    elif request.method == "POST":
        return api_call_post(path, fields)


def api_interpret(response, response_code=200):
    """
    Interpret the response from the API
    """
    if response is None:
        return jsonify({"status": "error", "message": "no response"}), 404
    else:
        return jsonify(response), response_code


def api_call_get(path):
    """
    Create a get call to IT API.
    """
    try:
        return api_interpret(itapi.call(path))
    except ITTechnicalAPIError as e:
        return api_interpret(e.response, e.status)


def api_call_post(path, fields):
    """
    Create a post call to IT API.
    """
    try:
        return api_interpret(itapi.post(path, fields))
    except ITTechnicalAPIError as e:
        return api_interpret(e.response, e.status)