from django.db.models import Model, CharField


class Category(Model):
    name = CharField(max_length=256)
    def __str__(self):
        return f"{self.name}"
