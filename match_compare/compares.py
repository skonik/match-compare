class Compare:

    __match_args__ = ('value',)

    def __init__(self, value):
        self.value = value


class Less(Compare):
    pass


class Greater(Compare):
    pass


class Equal(Compare):
    pass


def compare(left, right) -> Compare:
    if left > right:
        return Greater(value=right)
    if left < right:
        return Less(value=right)
    if left == right:
        return Equal(value=right)


