def read_port():
    with open('myoirt,info', 'r') as my_port:
        return my_port.read()


def main():
    port = read_port()


if __name__ == '__main__':
    main()
