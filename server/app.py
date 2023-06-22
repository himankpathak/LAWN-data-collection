from flask import Flask, request
from base64 import b85decode
import json, os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route("/image", methods=["POST"])
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

        with open(
             os.environ.get("IMAGE_COLLECT_PATH") + "imageToSave.jpg", "wb"
        ) as im:
            im.write(b85decode(img_data))

        return {}, 200

    except Exception as e:
        app.logger.error(e)
        return {}, 500


if __name__ == "__main__":
    app.run(debug=True)
