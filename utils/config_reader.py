# utils/config_reader.py
import configparser

def read_locator(page, element):
    config = configparser.ConfigParser()
    config.read('config/locators.ini')
    return config.get(page, element)