from django.contrib.auth.models import User
from collection.models import Console

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
