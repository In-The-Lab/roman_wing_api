from flask import Flask

app = Flask(__name__)

'''
	This here is how you create a route.
	This specific route is "http://localhost:5000/".
	You can see that this route only accepts GET requests.
	In order to accept POST requests, you would add "POST"
	to the list specified below.
'''
@app.route("/", methods=["GET"])
def do_nothing():
	return "<h1>Hello, world!</h1>"

# This just runs the API at port 5000.
if __name__ == "__main__":
	app.run(debug=True)