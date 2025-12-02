from app.extensions import ma
from app.models import Orders

class OrderSchema(ma.SQLAlchemySchema):
  class Meta:
    model = Orders
    id = ma.auto_field()
    include_fk = True

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)