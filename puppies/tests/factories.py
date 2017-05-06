import factory
from factory import lazy_attribute


from puppies.models import Puppy


class PuppyFactory(factory.DjangoModelFactory):
    name = factory.Faker('first_name')
    age = factory.Faker('random_int', min=0, max=20)
    breed = factory.Faker('word')
    color = factory.Faker('color_name')
    created_at = factory.Faker('date_time')
    updated_at = factory.Faker('date_time')


    class Meta:
        model = Puppy
