from flask import Flask, redirect, request
from routes.professor import Professor
from routes.comentarios import Comentarios

app = Flask(__name__)

@app.before_request
def redirect_to_https():
    if not request.is_secure:
        return redirect(request.url.replace("http://", "https://"), code=301)

app.register_blueprint()
app.register_blueprint()
app.register_blueprint()


if __name__ == "__main__":
    app.run(debug=True, ssl_context=('cert.pem', 'key.pem'), port=443)