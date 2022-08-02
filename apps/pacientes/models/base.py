from django.db.models import BooleanField, DateTimeField, Model


class BaseModel(Model):
    creado = DateTimeField(auto_now_add=True)
    modificado = DateTimeField(auto_now=True)
    activo = BooleanField(default=True, editable=False)

    class Meta:
        abstract = True

