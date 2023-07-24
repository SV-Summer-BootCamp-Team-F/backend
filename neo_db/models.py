# neo_db/models.py
from neomodel import StructuredNode, StringProperty, BooleanProperty, DateProperty, UniqueIdProperty, RelationshipTo, \
    RelationshipFrom, DateTimeProperty, StructuredRel

class HAVE(StructuredRel):
    uid = UniqueIdProperty()
    created_at = DateTimeProperty(default_now=True)
    updated_at = DateTimeProperty(default_now=True)

class RELATION(StructuredRel):
    uid = UniqueIdProperty()
    relation_name = StringProperty(required=True)
    memo = StringProperty()
    created_at = DateTimeProperty(default_now=True)
    updated_at = DateTimeProperty(default_now=True)
class USER(StructuredNode):
    #uid = UniqueIdProperty()
    user_name = StringProperty(unique_index=True, required=True)
    user_email = StringProperty(unique_index=True, required=True)
    password = StringProperty(required=True)
    phone_num = StringProperty(unique_index=True,required=True)
    user_photo = StringProperty()
    is_user = BooleanProperty(default=True)
    created_at = DateProperty(auto_now_add=True)
    update_at = DateProperty(default_now=True)
    cards = RelationshipTo('CARD', 'HAVE', model=HAVE)
    users = RelationshipTo('USER', 'RELATION', model=RELATION)

class CARD(StructuredNode):
    #uid = UniqueIdProperty()
    card_name = StringProperty(unique_index=True, required=True)
    card_email = StringProperty(unique_index=True, required=True)
    card_intro = StringProperty()
    card_phone_num = StringProperty(required=True, unique_index=True)
    card_photo = StringProperty(required=True)
    created_at = DateProperty(auto_now_add=True)
    update_at = DateProperty(default_now=True)
    owners = RelationshipFrom('USER', 'HAVE', model=HAVE)

