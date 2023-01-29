from django.db.models import Model, CharField


class Author(Model):
    first_name = CharField(max_length=256, default="", blank=True)
    middle_name = CharField(max_length=256, default="", blank=True)
    last_name = CharField(max_length=256)

    def __str__(self):
            return f"{self.first_name} {self.middle_name} {self.last_name}"