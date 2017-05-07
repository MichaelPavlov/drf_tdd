import json

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


class CreateNewPuppyTest(TestCase):
    def setUp(self):
        self.valid_payload = {
            'name': 'Muffin',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }
        self.invalid_payload = {
            'name': '',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }

    def test_valid_post_request(self):
        url = reverse('get_post_puppies')
        response = self.client.post(url, data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_post_request(self):
        url = reverse('get_post_puppies')
        response = self.client.post(url, data=json.dumps(self.invalid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSinglePuppyTest(TestCase):
    def setUp(self):
        self.puppies = PuppyFactory.create_batch(2)
        self.valid_payload = {
            'name': 'Muffin',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }
        self.invalid_payload = {
            'name': '',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }

    def test_valid_update_request(self):
        puppy = Puppy.objects.all().latest('id')
        url = reverse('get_delete_update_puppy', kwargs={'pk': puppy.pk})
        response = self.client.put(
            url,
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_request(self):
        puppy = Puppy.objects.all().latest('id')
        url = reverse('get_delete_update_puppy', kwargs={'pk': puppy.pk})
        response = self.client.put(
            url,
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSinglePuppyTest(TestCase):
    def setUp(self):
        self.puppies = PuppyFactory.create_batch(2)

    def test_valid_delete_request(self):
        puppy = Puppy.objects.all().latest('id')
        url = reverse('get_delete_update_puppy', kwargs={'pk': puppy.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_request(self):
        puppy = Puppy.objects.all().latest('id')
        url = reverse('get_delete_update_puppy', kwargs={'pk': puppy.pk + 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
