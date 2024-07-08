import logs
from executive_functions.basic import basic
from API.create_a_folder import create_a_folder
from Config.config_file import interval


if __name__ == '__main__':
    logs.logs.logs_message()
    create_a_folder()
    while True:
        basic(int(interval))
