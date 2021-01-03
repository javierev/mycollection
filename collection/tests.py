from django.test import TestCase
from django.urls import reverse
from .models import Console

# Create your tests here.
def create_console(name, short_name, year):
    """
    Create a console
    :param name: full name of the console
    :param short_name: short name of the console
    :param year: year of manufacture
    :return: console
    """
    return Console.objects.create(short_name=short_name, name=name, year=year)

class ConsolesDetailViewTests(TestCase):

    def test_get_unknown_console(self):
        """
        The detail view of a non existent console returns a 404 not found.
        """
        url = reverse('collection:console-detail', args=(99,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_get_console(self):
        """
        The detail view of a console returns the console.
        """
        console = create_console("Nombre de la consola", "nombre corto", 2015)
        url = reverse('collection:console-detail', args=(console.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, console.name)
