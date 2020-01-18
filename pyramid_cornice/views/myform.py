
from pyramid.view import view_config


@view_config(route_name='form', renderer='../templates/form.jinja2')
def my_form(request):
    return {}
