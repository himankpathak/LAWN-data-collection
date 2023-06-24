from flask import Flask, request, jsonify
from base64 import b85decode
import json, os
from dotenv import load_dotenv
from functools import wraps

load_dotenv()
app = Flask(__name__)


def check_auth(username, password):
    return username == os.environ.get("USER_NAME") and password == os.environ.get(
        "SECRET_KEY"
    )


def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            print("Error: Authentication failed")
            return jsonify({"message": "Authentication failed"}), 401
        return f(*args, **kwargs)

    return decorated_function


@app.route("/image", methods=["POST"])
@auth_required
def store_image():
    try:
        data = json.loads(request.data)
        img_data = data["img"]

        folder = os.environ.get("IMAGE_COLLECT_PATH")
        # check whether the path exists
        if not os.path.exists(folder):
            # create the new directory
            os.makedirs(folder)
            print("IMAGE_COLLECT_PATH directory created!")

        with open(os.environ.get("IMAGE_COLLECT_PATH") + "imageToSave.jpg", "wb") as im:
            im.write(b85decode(img_data))

        return {}, 200

    except Exception as e:
        app.logger.error(e)
        return {}, 500


if __name__ == "__main__":
    app.run(debug=True)
