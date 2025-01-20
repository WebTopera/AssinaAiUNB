from flask import Flask
from routes.home import home_route
from routes.comentarios import comentarios_route
from routes.professor import professor_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(comentarios_route, url_prefix="/comentarios")
app.register_blueprint(professor_route, url_prefix="/professores")

app.run(debug=True, host='0.0.0.0', port=5000)