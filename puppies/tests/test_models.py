from django.test import TestCase

from puppies.models import Puppy
from puppies.tests.factories import PuppyFactory


class PuppyTest(TestCase):
    def setUp(self):
        self.puppies = PuppyFactory.create_batch(2)

    def test_puppy_breed(self):
        pass