# -*- coding: utf-8 -*-

from flask import request
from flask.ext.restful import Resource
from app import db

# -*- API LIST -*-
#
# POST /api/login {username, password}
#

class Login(Resource):
    def post(self):
        data = request.get_json() or request.form
        username = data['username']
        password = data['password']

        res = db.getOne(
            """
            select password from User where school_id=%s;
            """, (username,)
        )

        if !res:
            return {
                "state": False,
                "reason": "User Not Found."
            }
        elif password == res['password']:
            return {
                "state": True,
                "reason": "Success!"
            }
        else:
            return {
                "state": False,
                "reason": "Wrong User/Password."
            }
