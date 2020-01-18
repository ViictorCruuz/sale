from cornice import Service
from pyramid_cornice.models import Cart, Product
from cornice.validators import marshmallow_body_validator
from pyramid_cornice.views.api.schema import CartSchema
from sqlalchemy.orm.exc import NoResultFound

sale = Service(name='sale',
               description='create news products',
               path='/api/v1/sale')


@sale.post(schema=CartSchema, validators=(marshmallow_body_validator,),
           content_type='application/json')
def create_sale(request):
    cart = Cart()
    for product in request.json['products']:
        cart.products.append(Product(**product))

    try:
        product_exist = request.dbsession.query(Product).filter_by(name=request.validated['products'][0]['name']).one()
        if product_exist:
            return
    except NoResultFound:
        request.dbsession.add(cart)
        request.dbsession.flush()

    schema = CartSchema()
    return schema.dump(cart).data
