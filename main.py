import logging
from executive_functions.function import function
from API.create_a_folder import create_a_folder


if __name__ == '__main__':
    logging.info('Программма синхронизации запущена')
    create_a_folder()
    while True:
        function(10)
