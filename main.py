from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "👋 Hello from your Flask app in Google Cloud!"

def flask_entry(request):
    return app(request.environ, start_response_wrapper)

def start_response_wrapper(status, headers):
    from werkzeug.wrappers import Response
    return Response(status=status, headers=dict(headers))
