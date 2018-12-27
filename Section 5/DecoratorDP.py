# Example of Decorator Design Pattern


class TextTag:

    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class BoldWrapper(TextTag):

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<b>{}</b>".format(self._wrapped.render())


class ItalicWrapper(TextTag):

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<i>{}</i>".format(self._wrapped.render())


if __name__ == '__main__':
    simple_hello = TextTag("hello, world!")
    special_hello = ItalicWrapper(BoldWrapper(simple_hello))
    print("Before: \t {}".format(simple_hello.render()))
    print("After:  \t {}".format(special_hello.render()))
