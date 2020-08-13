import os
import xml.etree.ElementTree as ET


this_folder = os.path.dirname(os.path.abspath(__file__))
parameters = os.path.join(this_folder, 'data/resource/parameters.xml')
tree = ET.parse(parameters)
root = tree.getroot()


def get_profile():
    """
    Retrieves and returns the <profile> value

    :return: str
    """
    return root[0].text


def get_from_city():
    """
    Retrieves and returns the <from_city> value

    :return: str
    """
    return root[1][0].text


def get_from_airport():
    """
    Retrieves and returns the <from_airport> value

    :return: str
    """
    return root[1][1].text


def get_to_city():
    """
    Retrieves and returns the <to_city> value

    :return: str
    """
    return root[1][2].text


def get_to_airport():
    """
    Retrieves and returns the <to_airport> value

    :return: str
    """
    return root[1][3].text


def get_adults():
    """
    Retrieves and returns the <adults> value

    :return: str
    """
    return root[2][0].text


def get_children():
    """
    Retrieves and returns the <children> value

    :return: str
    """
    return root[2][1].text


def get_infants():
    """
    Retrieves and returns the <infants> value

    :return: str
    """
    return root[2][2].text


def get_assertion_price():
    """
    Retrieves and returns the <flight_cost> value

    :return: str
    """
    return root[3][0].text
