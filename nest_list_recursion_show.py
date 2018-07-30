__author__ = 'lenovo'


# input ['foo',['bar',[1,[5,7],2,3],['baz']]]
# output ['foo','bar',1,5,7,2,3,'baz']


def flatten(nested):
    try:
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sub_list in nested:
            for element in flatten(sub_list):
                yield element
    except TypeError:
        yield nested


def repeater(value):
    while True:
        new = (yield value)
        if new is not None: value = new
