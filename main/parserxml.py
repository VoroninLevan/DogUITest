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


def get_full_screen():
    """
    Retrieves and returns the <fullscreen> value

    :return: str
    """
    return root[1].text


def get_width():
    """
    Retrieves and returns the <width> value

    :return: str
    """
    return root[2].text


def get_height():
    """
    Retrieves and returns the <height> value

    :return: str
    """
    return root[3].text
