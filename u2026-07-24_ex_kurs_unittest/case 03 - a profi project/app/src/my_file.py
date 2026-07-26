# einfach so, dein Code, wie du magst.

def my_complicated_function(a: int) -> int:
    """ increments a by one """

    if not isinstance(a, int):
        raise ValueError("a must be an integer")

    return a+1
