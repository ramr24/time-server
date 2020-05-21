# main.py for time-server

import os
from time import time  #
from flask import Flask

app = Flask(__name__)

epoch_time = str(int(time()))

@app.route('/<time>/')
def get_current_epoch_time(time):
	"""
	Webpage: http://localhost:6738/time/
	Returns the current epoch time (10 digits)
	"""
	return f"Current epoch time: {epoch_time}"


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 6738))
	app.run(host='0.0.0.0', port=port)
