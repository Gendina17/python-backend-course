""" Implementation of a custom list with overriding addition, subtraction and comparison """


class CustomList(list):
    def __add__(self, other):
        other = CustomList(other)
        return [self[i] + other[i] for i in range(max(len(self), len(other)))]

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        other = CustomList(other)
        return [self[i] - other[i] for i in range(max(len(self), len(other)))]

    def __rsub__(self, other):
        other = CustomList(other)
        return other - self

    def __getitem__(self, item):
        if item < len(self):
            return super().__getitem__(item)
        return 0

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)
