from django.db import models
from django.conf import settings
from django.db.models import Func, Value
from .get_schema import get_current_schema

class AesEncrypt(Func):
    template = "%(function)s(%(expressions)s::text, '%(key)s'::text, 'cipher-algo=aes256'::text)"

    def __init__(self, expression, key, **extra):
        super().__init__(expression, **extra)
        self.extra['key'] = key
        self.function = f"{get_current_schema()}.pgp_sym_encrypt"

class AesDecrypt(Func):
    template = "%(function)s(%(expressions)s::text, '%(key)s'::text)"

    def __init__(self, expression, key, **extra):
        super().__init__(expression, **extra)
        self.extra['key'] = key
        self.function = f"{get_current_schema()}.pgp_sym_encrypt"
