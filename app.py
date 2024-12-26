def hello_world():  # put application's code here
    """ my doc remark. """
    return 'Hello World!'


def void_method():
    print("method")


def lambda_method():
    return lambda: 1 + 2


def annotation_method(arg1: str, arg2) -> str:
    print(arg1, arg2)
    return "ok"


if __name__ == '__main__':
    print(hello_world())
    print(void_method())
    m = lambda_method()
    print(m())
    print(annotation_method("1", 2))
