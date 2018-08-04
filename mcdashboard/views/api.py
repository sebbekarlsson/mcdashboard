from flask import Blueprint, jsonify
from bson.objectid import ObjectId
from mcdashboard.facades.ServerFacade import ServerFacade


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/api'
)


@bp.route('/server/<server_id>/logs', methods=['GET'])
def show(server_id):
    server = ServerFacade.get(query=dict(id=ObjectId(server_id)), single=True)

    return jsonify(server.get_container().logs())
