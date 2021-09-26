from api import API
from storage import Storage

def main():
    api = API("students.txt")

    status = api.prompt()

    while status > 0:
        status = api.prompt()


if __name__ == '__main__':
    main()