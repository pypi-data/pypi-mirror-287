from decimal import Decimal
from typing import Any
from django.db import models, connection
from django.conf import settings
from django.db.models import Func, Value
from .get_schema import get_current_schema

class EncryptedTextField(models.BinaryField):
    def __init__(self, *args, **kwargs):
        self.encrypt_key = settings.PGCRYPTO_KEY
        self.schema = get_current_schema()
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if value is not None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {self.schema}.pgp_sym_encrypt(%s::text, %s::text)", [value, self.encrypt_key])
                return cursor.fetchone()[0]
        return value

    def from_db_value(self, value, expression, connection):
        if value is not None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {self.schema}.pgp_sym_decrypt(%s::bytea, %s::text)", [value, self.encrypt_key])
                return cursor.fetchone()[0]
        return value    

class EncryptedCharField(models.BinaryField):
    def __init__(self, *args, **kwargs):
        self.encrypt_key = settings.PGCRYPTO_KEY
        self.schema = get_current_schema()
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if value is not None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {self.schema}.pgp_sym_encrypt(%s::text, %s::text)", [value, self.encrypt_key])
                return cursor.fetchone()[0]
        return value

    def from_db_value(self, value, expression, connection):
        if value is not None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {self.schema}.pgp_sym_decrypt(%s::bytea, %s::text)", [value, self.encrypt_key])
                return cursor.fetchone()[0]
        return value  

class EncryptedEmailField(models.BinaryField):
    def __init__(self, *args, **kwargs):
        self.encrypt_key = settings.PGCRYPTO_KEY
        self.schema = get_current_schema()
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if value is not None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {self.schema}.pgp_sym_encrypt(%s::text, %s::text)", [value, self.encrypt_key])
                return cursor.fetchone()[0]
        return value

    def from_db_value(self, value, expression, connection):
        if value is not None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {self.schema}.pgp_sym_decrypt(%s::bytea, %s::text)", [value, self.encrypt_key])
                return cursor.fetchone()[0]
        return value 

class EncryptedIntegerField(models.BinaryField):
    def __init__(self, *args, **kwargs):
        self.encrypt_key = settings.PGCRYPTO_KEY
        self.schema = get_current_schema()
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if value is not None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {self.schema}.pgp_sym_encrypt(%s::text, %s::text)", [value, self.encrypt_key])
                return cursor.fetchone()[0]
        return value

    def from_db_value(self, value, expression, connection):
        if value is not None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {self.schema}.pgp_sym_decrypt(%s::bytea, %s::text)", [value, self.encrypt_key])
                return cursor.fetchone()[0]
        return value  

class EncryptedFloatField(models.BinaryField):
    def __init__(self, *args, **kwargs):
        self.encrypt_key = settings.PGCRYPTO_KEY
        self.schema = get_current_schema()
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if value is not None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {self.schema}.pgp_sym_encrypt(%s::text, %s::text)", [value, self.encrypt_key])
                return cursor.fetchone()[0]
        return value

    def from_db_value(self, value, expression, connection):
        if value is not None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {self.schema}.pgp_sym_decrypt(%s::bytea, %s::text)", [value, self.encrypt_key])
                return cursor.fetchone()[0]
        return value 

class EncryptedDecimalField(models.BinaryField):
    def __init__(self, *args, **kwargs):
        self.encrypt_key = settings.PGCRYPTO_KEY
        self.schema = get_current_schema()
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if value is not None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {self.schema}.pgp_sym_encrypt(%s::text, %s::text)", [value, self.encrypt_key])
                return cursor.fetchone()[0]
        return value

    def from_db_value(self, value, expression, connection):
        if value is not None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {self.schema}.pgp_sym_decrypt(%s::bytea, %s::text)", [value, self.encrypt_key])
                return cursor.fetchone()[0]
        return value 

    def from_db_value(self, value, expression, connection):
        if value is not None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {self.schema}.pgp_sym_decrypt(%s::bytea, %s::text)", [value, self.encrypt_key])
                return Decimal(cursor.fetchone()[0])
        return value  

class EncryptedBooleanField(models.BinaryField):
    def __init__(self, *args, **kwargs):
        self.encrypt_key = settings.PGCRYPTO_KEY
        self.schema = get_current_schema()
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if value is not None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {self.schema}.pgp_sym_encrypt(%s::text, %s::text)", [value, self.encrypt_key])
                return cursor.fetchone()[0]
        return value

    def from_db_value(self, value, expression, connection):
        if value is not None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {self.schema}.pgp_sym_decrypt(%s::bytea, %s::text)", [value, self.encrypt_key])
                return cursor.fetchone()[0]
        return value 

class EncryptedGenericIPAddressField(models.BinaryField):
    def __init__(self, *args, **kwargs):
        self.encrypt_key = settings.PGCRYPTO_KEY
        self.schema = get_current_schema()
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if value is not None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {self.schema}.pgp_sym_encrypt(%s::text, %s::text)", [value, self.encrypt_key])
                return cursor.fetchone()[0]
        return value

    def from_db_value(self, value, expression, connection):
        if value is not None:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT {self.schema}.pgp_sym_decrypt(%s::bytea, %s::text)", [value, self.encrypt_key])
                return cursor.fetchone()[0]
        return value 
    
