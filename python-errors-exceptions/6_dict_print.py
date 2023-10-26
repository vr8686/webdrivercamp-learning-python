#!/usr/bin/python3
def raise_message(message=""):
    raise NameError("NameError message")


if __name__ == "__main__":
    try:
        raise_message()
    except NameError as e:
        print(e)
