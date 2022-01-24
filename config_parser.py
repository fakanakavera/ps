from configparser import ConfigParser

parser = ConfigParser()

parser.read('./cfg/conf.ini')

print(type(parser['owner']['name']))
parser.set('owner', 'name', 'FakaNaKavera')

print(parser['owner']['name'])

with open('./cfg/conf.ini', 'w+') as configfile:
    parser.write(configfile)