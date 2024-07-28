import configparser
import os

class Configuration:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = configparser.ConfigParser()
        self.load_settings()

    def load_settings(self):
        """Load settings from the INI file."""
        if os.path.exists(self.file_path):
            self.config.read(self.file_path)

    def store_settings(self, section, settings):
        """Store settings to the INI file."""
        if not self.config.has_section(section):
            self.config.add_section(section)
        for key, value in settings.items():
            self.config.set(section, key, str(value))
        with open(self.file_path, 'w') as file:
            self.config.write(file)

    def modify_setting(self, section, key, value):
        """Modify a specific setting in the INI file."""
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, key, str(value))
        with open(self.file_path, 'w') as file:
            self.config.write(file)

    def get_setting(self, section, key, default=None):
        """Get a specific setting from the INI file."""
        if self.config.has_section(section) and self.config.has_option(section, key):
            return self.config.get(section, key)
        return default