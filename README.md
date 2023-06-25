# LAWN Data Collection
Author: Himank Pathak

### Instructions
- Clone this repository
- Create venv with `virtualenv venv`
- Activate venv with `source venv/bin/activate`
- Install the required packages with `pip install -r requirements.txt`
- Create a `.env` file with following vars
```
IMAGE_COLLECT_PATH=images/
USER_NAME=user_name
SECRET_KEY=SECRET_KEY
SENDGRID_API_KEY=API_KEY
```
- Run server with `python server/app.py`
- Run client with `python client/app.py`
