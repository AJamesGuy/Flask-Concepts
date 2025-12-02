from datetime import datetime, timedelta, timezone
from functools import wraps
from jose import jwt, exceptions
from flask import request, jsonify

SECRET_KEY = 'your_secret_key_here'

def encode_token(user_id, role="user"):
    payload = {
        "exp": datetime.now(timezone.utc) + timedelta(days=0, hours=1),
        "iat": datetime.now(timezone.utc),
        "sub": str(user_id), # VERY IMPORTANT SET USER_ID TO STR
        "role": role
    }


    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def token_required(f): # f stand for the function that is being wrapped
    @wraps(f)
    def decoration(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1] # Bearer <token>
        if not token:
            return jsonify({"error": "Token is missing!"}), 401
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            print(data)
        except jose.exceptions.ExpiredSignatureError:
            return jsonify({'message': 'token is expired'}), 403
        except jose.exceptions.JWTError:
            return jsonify({"message": 'invalid token'}), 401
        return f(*args, **kwargs)
    return decoration
