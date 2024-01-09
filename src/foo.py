from src.exceptions import CustomError

class Foo(object):
    def __init__(self, value: int) -> None:
        self.value = value

    def bar(self):
        raise CustomError('error!')


def bar() -> str:
    return "bar"
