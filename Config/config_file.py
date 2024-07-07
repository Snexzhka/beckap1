import configparser

config = configparser.ConfigParser()

config.add_section('Keys')
config.set('Keys', 'TOKEN', 'y0_AgAAAAB2xH3PAADLWwAAAAEHzJX3AADjH8uX2w9E6LT-9Y4ULbB-gAuWNQ')
config.set("Keys", 'disk_path', 'backup')
config.set('Keys', 'local_file', r'D:\test')
config.set('Keys', 'interval', '20')
with open('config.ini', 'w') as config_file:
    config.write(config_file)


with open('config.ini', 'r')as file:
    config.read(file)
    TOKEN = config.get('Keys', 'TOKEN')
    disk_path = config.get('Keys', 'disk_path')
    local_file = config.get('Keys', 'local_file')
    interval = config.get('Keys', 'interval')
