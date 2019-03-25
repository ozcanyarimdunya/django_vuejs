import json
from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase

from . import models


class TestAuthenticate(APITestCase):
    def setUp(self):
        self.content_type = 'application/json'

        # User should have admin page access so it may be an active or superuser.
        User.objects.create_user(
            username="admin",
            password="123",
            email="admin@admin.com",
            first_name="Admin",
            last_name="Admin",
        )

    def test_get_token(self):
        path = '/obtain-token/'
        data = json.dumps({'username': 'admin', 'password': '123'})
        response = self.client.post(path=path, data=data, content_type=self.content_type)
        self.assertTrue('token' in response.data)

    def test_refresh_token(self):
        path = '/obtain-token/'
        data_rt = json.dumps({'username': 'admin', 'password': '123'})
        response = self.client.post(path=path, data=data_rt, content_type=self.content_type)

        token = response.data['token']
        path_rt = '/refresh-token/'
        data_rt = json.dumps({'token': token})
        response_rt = self.client.post(path=path_rt, data=data_rt, content_type=self.content_type)

        self.assertEqual(response_rt.data['token'], token)

    def tearDown(self):
        User.objects.all().delete()


class TestTodoApi(APITestCase):

    def setUp(self):
        self.content_type = 'application/json'
        User.objects.create_superuser(
            username="admin", password="123", email="admin@admin.com", first_name="Admin", last_name="Admin"
        )
        data = json.dumps({"username": "admin", "password": "123"})
        response = self.client.post(path="/obtain-token/", data=data, content_type=self.content_type)
        token = response.data['token']

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

    def test_model(self):
        todo = models.Todo.objects.create(name='Todo 1')

        self.assertEqual(todo.__str__(), 'Todo 1')
        self.assertEqual(todo.get_absolute_url(), '/todo/detail/1/')
        self.assertEqual(todo.get_update_url(), '/todo/update/1/')

    def test_list(self):
        path = '/todo/list/'
        models.Todo.objects.create(name='Todo 1')
        models.Todo.objects.create(name='Todo 2')
        models.Todo.objects.create(name='Todo 3')

        response = self.client.get(path=path)
        self.assertEqual(len(response.data), 3)

    def test_create(self):
        path = '/todo/create/'
        data = json.dumps({
            'name': 'Todo 1'
        })
        response = self.client.post(path=path, data=data, content_type=self.content_type)
        self.assertEqual(response.status_code, 201)

    def test_detail(self):
        path = '/todo/detail/1/'
        models.Todo.objects.create(pk=1, name='Todo 1')

        response = self.client.get(path=path)
        self.assertEqual(response.data['name'], 'Todo 1')

    def test_update(self):
        path = '/todo/update/1/'
        models.Todo.objects.create(pk=1, name='Todo 1')

        data = json.dumps({'name': 'Todo 1 updated'})
        self.client.put(path=path, data=data, content_type=self.content_type)
        updated = models.Todo.objects.get(pk=1)
        self.assertEqual(updated.name, 'Todo 1 updated')

    def test_delete(self):
        path = '/todo/delete/1/'
        models.Todo.objects.create(pk=1, name='Todo 1')

        self.client.delete(path=path)
        # noinspection PyTypeChecker
        self.assertRaises(models.Todo.DoesNotExist)
        from django.db import models as md
        self.assertRaises(md.ObjectDoesNotExist)

    def test_toggle(self):
        path = '/todo/toggle/1/'
        models.Todo.objects.create(pk=1, name='Todo 1')

        self.client.patch(path=path, content_type=self.content_type)
        toggled = models.Todo.objects.get(pk=1)
        self.assertTrue(toggled.completed)

        # toggle again
        self.client.patch(path=path, content_type=self.content_type)
        toggled = models.Todo.objects.get(pk=1)
        self.assertFalse(toggled.completed)

    def tearDown(self):
        models.Todo.objects.all().delete()
        User.objects.all().delete()


class TestTodoViewSet(APITestCase):
    def setUp(self):
        self.content_type = 'application/json'
        User.objects.create_superuser(
            username="admin", password="123", email="admin@admin.com", first_name="Admin", last_name="Admin"
        )
        data = json.dumps({"username": "admin", "password": "123"})
        response = self.client.post(path="/obtain-token/", data=data, content_type=self.content_type)
        token = response.data['token']

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

    def test_list(self):
        path = '/todo/vs/'
        models.Todo.objects.create(name='Todo 1')
        models.Todo.objects.create(name='Todo 2')
        models.Todo.objects.create(name='Todo 3')

        response = self.client.get(path=path)
        self.assertEqual(len(response.data), 3)

    def test_create(self):
        path = '/todo/vs/'
        data = json.dumps({
            'name': 'Todo 1'
        })
        response = self.client.post(path=path, data=data, content_type=self.content_type)
        self.assertEqual(response.status_code, 201)

    def test_detail(self):
        path = '/todo/vs/1/'
        models.Todo.objects.create(pk=1, name='Todo 1')

        response = self.client.get(path=path)
        self.assertEqual(response.data['name'], 'Todo 1')

    def test_update(self):
        path = '/todo/vs/1/'
        models.Todo.objects.create(pk=1, name='Todo 1')

        data = json.dumps({'name': 'Todo 1 updated'})
        self.client.put(path=path, data=data, content_type=self.content_type)
        updated = models.Todo.objects.get(pk=1)
        self.assertEqual(updated.name, 'Todo 1 updated')

    def test_delete(self):
        path = '/todo/vs/1/'
        models.Todo.objects.create(pk=1, name='Todo 1')

        self.client.delete(path=path)
        # noinspection PyTypeChecker
        self.assertRaises(models.Todo.DoesNotExist)
        from django.db import models as md
        self.assertRaises(md.ObjectDoesNotExist)

    def test_completed_todos(self):
        path = '/todo/vs/completed-todos/'
        models.Todo.objects.create(name='Todo 1', completed=True)
        models.Todo.objects.create(name='Todo 2', completed=True)
        models.Todo.objects.create(name='Todo 3')

        response = self.client.get(path=path)
        self.assertEqual(len(response.data), 2)

    def test_toggle(self):
        path = '/todo/vs/1/toggle-todo/'
        models.Todo.objects.create(pk=1, name='Todo 1')

        self.client.post(path=path, content_type=self.content_type)
        toggled = models.Todo.objects.get(pk=1)
        self.assertTrue(toggled.completed)

        # toggle again
        self.client.post(path=path, content_type=self.content_type)
        toggled = models.Todo.objects.get(pk=1)
        self.assertFalse(toggled.completed)

    def tearDown(self):
        models.Todo.objects.all().delete()
        User.objects.all().delete()
