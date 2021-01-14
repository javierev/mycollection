from collection.models import *

def create_country(name, iso_code):
    """
    Create a country in DB for testing purposes.
    :param name: name of the country
    :param iso_code: ISO code of the country
    """
    return Country.objects.create(name=name, iso_code=iso_code)

def create_company(name, country):
    """
    Create a country in DB for testing purposes.
    :param name: name of the company
    :param country: country where it is based
    """
    return Company.objects.create(name=name, country=country)

def create_console(name, short_name, year, user=None):
    """
    Create a console in DB for testing purposes.
    :param name: full name of the console
    :param short_name: short name of the console
    :param year: year of manufacture
    :param user: owner of the console
    :return: console
    """
    return Console.objects.create(short_name=short_name, name=name, year=year, owner=user)

def create_user(username, email, password):
    """
    Create a user in DB for testing purposes.
    :param username: username
    :param email: email
    :param password: password (clear)
    :return: User
    """
    return User.objects.create_user(username=username, email=email, password=password)
