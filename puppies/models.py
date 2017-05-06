from django.db.models import Model, CharField, IntegerField, DateTimeField


class Puppy(Model):
    """
    Puppy model
    Defines the attributes of a puppy
    """
    name = CharField(max_length=255)
    age = IntegerField()
    breed = CharField(max_length=255)
    color = CharField(max_length=255)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def get_breed(self):
        return self.name + ' belongs to ' + self.breed + ' breed.'

    def __str__(self):
        return self.name + ' is added.'
