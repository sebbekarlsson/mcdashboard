from flask import Blueprint, render_template
from mcdashboard.facades.ServerFacade import ServerFacade


bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/')
def show():
    servers = ServerFacade.get()

    return render_template('index.html', servers=servers)
