from flask import Blueprint, render_template, request, redirect
from bson.objectid import ObjectId
from mcdashboard.forms.ServerForm import ServerForm
from mcdashboard.facades.ServerFacade import ServerFacade
from mcdashboard.docker_utils import get_free_tcp_port


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/server'
)


@bp.route('/<server_id>', methods=['POST', 'GET'])
@bp.route('/', defaults={'server_id': None}, methods=['POST', 'GET'])
def show(server_id):
    form = ServerForm(request.form)
    server = ServerFacade.get(query=dict(id=ObjectId(server_id)), single=True)\
        if server_id else None

    if request.method == 'POST' and form.validate():
        if not server_id:
            server = ServerFacade.create(
                port=get_free_tcp_port(),
                name=form.name.data
            )

            return redirect('/server/{}'.format(server.id))
        else:
            server.update(
                name=form.name.data
            )

            server = ServerFacade.get(
                query=dict(id=ObjectId(server_id)), single=True)\
                if server_id else None

    elif server:
        form.name.data = server.name

    return render_template('server.html', form=form, server=server)
