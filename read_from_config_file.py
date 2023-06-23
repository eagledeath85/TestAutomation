from configparser import ConfigParser

# Creation of ConfigParser object
config = ConfigParser()


# Read data from config file. "./" says to look into the current project the file at the path specified
config.read("./InputFiles/Config.cfg")

# Print the parameter username from the section section1
print(config.get('APIAutomation', 'base_url'))   # passing section, parameter to the get method