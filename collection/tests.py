from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Console
from rest_framework.parsers import JSONParser
import io

# Create your tests here.
def create_console(name, short_name, year, user=None):
    """
    Create a console
    :param name: full name of the console
    :param short_name: short name of the console
    :param year: year of manufacture
    :param user: owner of the console
    :return: console
    """
    return Console.objects.create(short_name=short_name, name=name, year=year, owner=user)

def create_user(username, email, password):
    """
    Create a user
    :param username: username
    :param email: email
    :param password: password (clear)
    :return: User
    """
    return User.objects.create_user(username=username, email=email, password=password)

class ConsolesDetailViewTests(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def __set_credentials_with_token(self, username, password):
        url = reverse('collection:token_obtain_pair')
        data = { 'username': username, 'password': password }
        response = self.client.post(path=url, data=data)
        tokens = JSONParser().parse(io.BytesIO(response.content))
        self.client.credentials(HTTP_AUTHORIZATION='Bearer %s' % tokens['access'])



    def test_get_unknown_console(self):
        """
        The detail view of a non existent console returns a 404 not found.
        """
        url = reverse('collection:console-detail', args=(99,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_get_console_without_permission(self):
        """
        The detail view of an existent console from other user returns a 401 error (forbidden).
        """
        owner = create_user(username='freddie', email='fmercury@queen.com', password='the great pretender')
        other = create_user(username='brian', email='bmay@queen.com', password='hammer to fall')
        console = create_console(name='PlayStation 5', short_name='PS5', year=2020, user=owner)
        url = reverse('collection:console-detail', args=(console.pk,))
        self.__set_credentials_with_token(username='brian', password='hammer to fall')
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 403)


    def test_get_console(self):
        """
        The detail view of a console returns the console.
        """
        owner = create_user(username='freddie', email='fmercury@queen.com', password='the great pretender')
        console = create_console(name="PlayStation 5", short_name="PS5", year=2020, user=owner)
        url = reverse('collection:console-detail', args=(console.pk,))
        self.__set_credentials_with_token(username='freddie', password='the great pretender')
        response = self.client.get(path=url, args=(console.pk,))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, console.name)

    def test_post_console(self):
        """
        Save a console saves the console.
        """
        owner = create_user(username='john', email='jdeacon@queen.com', password="You're so self satisfied I don't need you")
        console = create_console(name="PlayStation 5", short_name="PS5", year=2020, user=owner)
        self.__set_credentials_with_token(username='john', password="You're so self satisfied I don't need you")
        url = reverse('collection:console-detail', args=(console.pk,))
        response = self.client.post(path=url,
                                    data={'name' : 'PlayStation 55', 'short_name':'PS55', 'year': 2055},
                                    format='json')
        saved_console = Console.objects.get(pk=console.pk)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PlayStation 55')
        self.assertEqual(saved_console.name, 'PlayStation 55')
        self.assertEqual(saved_console.short_name, 'PS55')
        self.assertEqual(saved_console.year, 2055)


    def test_post_console_without_permission(self):
        """
        Error 401 (forbidden) when a user tries to save another user's console.
        """
        owner = create_user(username='john', email='jdeacon@queen.com', password="You're so self satisfied I don't need you")
        other = create_user(username='roger', email='rtaylor@queen.com', password="One golden glance of what should be")
        console = create_console(name="PlayStation 5", short_name="PS5", year=2020, user=owner)
        self.__set_credentials_with_token(username='roger', password="One golden glance of what should be")
        url = reverse('collection:console-detail', args=(console.pk,))
        response = self.client.post(path=url,
                                    data={'id' : console.pk, 'name' : 'PlayStation 55', 'short_name':'PS55', 'year': 2055},
                                    format='json')
        saved_console = Console.objects.get(pk=console.pk)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(saved_console.name, 'PlayStation 5')
        self.assertEqual(saved_console.short_name, 'PS5')
        self.assertEqual(saved_console.year, 2020)

    def test_post_console_anonymous(self):
        """
        Error 403 (unauthorized) when an anonymous user tries to save a console.
        """
        owner = create_user(username='john', email='jdeacon@queen.com', password="You're so self satisfied I don't need you")
        console = create_console(name="PlayStation 5", short_name="PS5", year=2020, user=owner)
        url = reverse('collection:console-detail', args=(console.pk,))
        response = self.client.post(path=url,
                                    data={'id' : console.pk, 'name' : 'PlayStation 55', 'short_name':'PS55', 'year': 2055},
                                    format='json')
        saved_console = Console.objects.get(pk=console.pk)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(saved_console.name, 'PlayStation 5')
        self.assertEqual(saved_console.short_name, 'PS5')
        self.assertEqual(saved_console.year, 2020)