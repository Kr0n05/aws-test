import time

from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
	return "Hello There!"

if __name__ == "__main__":
	time.sleep(15)
	application.run(host='0.0.0.0')