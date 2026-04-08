from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
SECRET = "weaksecret"  # intentionally weak

@app.route("/login")
def login():
    user = request.args.get("user", "guest")

    token = jwt.encode({
        "user": user,
        "role": "user",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
    }, SECRET, algorithm="HS256")

    return jsonify({"token": token})


# 🔴 VULN 1: Accepts 'none' algorithm
@app.route("/admin_none")
def admin_none():
    token = request.headers.get("Authorization")

    try:
        decoded = jwt.decode(token, options={"verify_signature": False})
        
        if decoded.get("role") == "admin":
            return "Admin Access via NONE 🔥"
        else:
            return "Access Denied"

    except Exception as e:
        return str(e)


# 🔴 VULN 2: Weak secret
@app.route("/admin")
def admin():
    token = request.headers.get("Authorization")

    try:
        decoded = jwt.decode(token, SECRET, algorithms=["HS256"])

        if decoded.get("role") == "admin":
            return "Welcome Admin 🔥"
        else:
            return "Access Denied"

    except Exception as e:
        return str(e)


# 🔴 VULN 3: No expiry validation
@app.route("/admin_no_exp")
def admin_no_exp():
    token = request.headers.get("Authorization")

    try:
        decoded = jwt.decode(token, SECRET, options={"verify_exp": False})

        if decoded.get("role") == "admin":
            return "Admin (Expired Token Bypass) 🔥"
        else:
            return "Access Denied"

    except Exception as e:
        return str(e)


app.run(port=5000)
