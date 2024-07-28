# Write configurations into .ini

This project leverages `configureparser` module to write your configurations into an .ini file at ease. It's designed for simplicity and ease of use, allowing you to manage .ini files.

## Features

- **Write**: Write and store your configurations.
- **Read**: Read the only configuration you need.
- **Modify**: Modify the configuration.
- **Store with sections**: Store your configuration based on its type as a section.

## Prerequisites

- `configparser`

## Usage

To use the functionality, import the `Configuration` function from `ArtexConfigure`.

```python

from ArtexConfig import Configuration

settings_file = 'app_settings.ini'
app_settings = AppSettings(settings_file)

# Store settings
initial_settings = {
    'theme': 'dark',
    'language': 'en',
    'notifications': 'True'
}
app_settings.store_settings('General', initial_settings)

# Modify a setting
app_settings.modify_setting('General', 'language', 'es')

# Verify the modification
print(app_settings.get_setting('General', 'language'))  # Output: es

```

**This project is managed by Artex AI. Soon an improved and stable version will roll out**