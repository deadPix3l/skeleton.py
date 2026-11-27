from collections.abc import Iterable, Generator, Callable

# returns a generator, if you would prefer list,
# you can convert it manually: `list(flatten(x))`,
# or pass a function in: `flatten(x, func=list)`
def flatten[T](
        lst: Iterable[T | Iterable[T]],
        *,
        func: Callable[[Iterable], Iterable] = lambda x: x,
        max_depth: int = -1,
) -> Iterable[T]:
    def _gen(lst) -> Generator[T, None, None]:
        for i in lst:
            if isinstance(i, Iterable) and not isinstance(i, str):
                if max_depth == 0:
                    yield i
                else:
                    yield from flatten(i, max_depth=max_depth-1)
            else:
                yield i
    return func(_gen(lst))

