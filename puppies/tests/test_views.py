from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from puppies.models import Puppy
from puppies.serializers import PuppySerializer
from puppies.tests.factories import PuppyFactory


class GetAllPuppiesTest(TestCase):
    def setUp(self):
        PuppyFactory.create_batch(4)

    def test_get_all_puppies(self):
        # get API response
        response = self.client.get(reverse('get_post_puppies'))
        # get data from db
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSinglePuppyTest(TestCase):
    def setUp(self):
        PuppyFactory.create_batch(4)

    def test_get_valid_single_puppy(self):
        puppy = Puppy.objects.all().first()
        url = reverse('get_delete_update_puppy', kwargs={'pk': puppy.pk})
        response = self.client.get(url)
        serializer = PuppySerializer(puppy)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_puppy(self):
        puppy = Puppy.objects.all().latest('id')
        url = reverse('get_delete_update_puppy', kwargs={'pk': puppy.pk + 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
