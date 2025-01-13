from flask import Flask, redirect, request
from routes.home import home_route
from routes.comentarios import comentarios_route
from routes.professor import professor_route

app = Flask(__name__)

@app.before_request
def redirect_to_https():
    if not request.is_secure:
        return redirect(request.url.replace("http://", "https://"), code=301)

app.register_blueprint(home_route)
app.register_blueprint(comentarios_route, url_prefix="/comentarios")
app.register_blueprint(professor_route, url_prefix="/professores")


if __name__ == "__main__":
    app.run(debug=True, ssl_context=('cert.pem', 'key.pem'), port=443)