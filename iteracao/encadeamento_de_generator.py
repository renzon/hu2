def dobro(iteravel):
    for i in iteravel:
        yield i * 2


def soma_1(iteravel):
    for i in iteravel:
        yield i + 1


print(list(
    map(
        lambda n: n + 1,
        map(
            lambda i: i * 2, range(10)
        )
    )
))
