def days(a, b, *args, **kwargs):
    print(a)  # 4
    print(b)  # 5
    print(args)  # (4, 7, 7)
    print(kwargs)  # {'mod': 'Monday', 'mod1': 5, 'sunday': 'Sunday'}


# days(1="Monday") #SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
days(4, 5, 4, 7, 7, mod="Monday", mod1=5, sunday="Sunday")
