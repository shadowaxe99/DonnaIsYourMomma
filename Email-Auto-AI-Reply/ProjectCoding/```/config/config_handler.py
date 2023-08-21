
import configparser
import os

class ConfigHandler:
    def __init__(self, config_file='config.ini'):
        self.config_file = config_file
        self.config = configparser.ConfigParser()

    def create_config(self, section, key, value):
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, key, value)
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)

    def read_config(self, section, key):
        self.config.read(self.config_file)
        return self.config.get(section, key)

    def update_config(self, section, key, value):
        self.config.read(self.config_file)
        self.config.set(section, key, value)
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)

    def delete_config(self, section, key):
        self.config.read(self.config_file)
        self.config.remove_option(section, key)
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)
