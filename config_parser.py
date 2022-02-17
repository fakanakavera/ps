from configparser import ConfigParser

parser = ConfigParser()

parser.read('constants.toml')

print(parser['6-max']['player']['table'])