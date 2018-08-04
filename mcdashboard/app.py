from flask import Flask
from mcdashboard.views.index import bp as index_bp
from mcdashboard.views.server import bp as server_bp


app = Flask(__name__)

app.config.update(
    SECRET_KEY='abc123',
    TEMPLATES_AUTO_RELOAD=True
)

app.register_blueprint(index_bp)
app.register_blueprint(server_bp)
