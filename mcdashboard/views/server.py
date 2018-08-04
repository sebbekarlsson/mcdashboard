from flask import Blueprint, render_template, request
from mcdashboard.forms.ServerForm import ServerForm


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/server'
)


@bp.route('/<server_id>')
@bp.route('/', defaults={'server_id': None})
def show(server_id):
    form = ServerForm(request.form)

    return render_template('server.html', form=form)
