from django.db import models
from django.conf import settings
from django.db.models import Func, BinaryField, TextField, CharField
from .get_schema import get_current_schema

class AesEncrypt(Func):
    template = "%(function)s(%(expressions)s::text, '%(key)s'::text, 'cipher-algo=aes256'::text)"
    output_field = BinaryField()

    def __init__(self, expression, key, **extra):
        super().__init__(expression, **extra)
        self.extra['key'] = key
        self.function = f"{get_current_schema()}.pgp_sym_encrypt"

class AesDecrypt(Func):
    template = "%(function)s(%(expressions)s::text, '%(key)s'::text)"
    output_field = CharField()

    def __init__(self, expression, key, **extra):
        super().__init__(expression, **extra)
        self.extra['key'] = key
        self.function = f"{get_current_schema()}.pgp_sym_decrypt"


#from django.db.models import F

# # Encrypting a field
# MyModel.objects.update(encrypted_field=AesEncrypt(F('plain_text_field'), 'my_secret_key'))

# # Decrypting a field in a query
# decrypted_values = MyModel.objects.annotate(decrypted_field=AesDecrypt(F('encrypted_field'), 'my_secret_key')).values('decrypted_field')