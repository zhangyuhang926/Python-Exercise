class S:
    instance = None

    def __new__(cls, *args, **kwargs):
        if S.instance is None:
            S.instance = super().__new__(cls)

    def __init__(self):
        pass

s1 = S()
print(id(s1))
s2 = S()
print(id(s2))