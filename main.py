import logging
import socket
import database
import selector


def read_port():
    with open('myoirt,info', 'r') as my_port:
        return my_port.read()


def main():
    port = '0000'
    try:
        port = int(read_port())
    except:
        logging.info(f'Error in port casting to int {read_port()}')
    data = database
    server = selector.Selector(port)
    server.run_server()


if __name__ == '__main__':
    main()
