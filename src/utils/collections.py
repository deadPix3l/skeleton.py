from collections.abc import Iterable, Generator, Callable

# returns a generator, if you would prefer list,
# you can convert it manually: `list(flatten(x))`,
# or pass a function in: `flatten(x, func=list)`
def flatten[T](
        lst: Iterable[T | Iterable[T]],
        *,
        func: Callable[[Iterable], Iterable] = lambda x: x,
) -> Iterable[T]:
    def _gen(lst) -> Generator[T, None, None]:
        for i in lst:
            if isinstance(i, Iterable) and not isinstance(i, str):
                yield from flatten(i)
            else:
                yield i
    return func(_gen(lst))

