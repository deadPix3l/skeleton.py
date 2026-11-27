from collections.abc import Iterable, Generator, Callable

# foss-alt: boltons.iterutils.flatten
# the following alternatives technically work, but dont support deeply nested or inconsistent iterables:
# foss-alt: itertools.chain
# oneliner: [item for sublist in nested for item in sublist]
def flatten[T](
        lst: Iterable[T | Iterable[T]],
        *,
        func: Callable[[Iterable], Iterable] = lambda x: x,
        max_depth: int = -1,
) -> Iterable[T]:
    """
    Take a nested iterable and collapse inner iterables, up to max_depth

    Params:
        lst: an iterable to flatten
        func: a final processing function (default: no-op - passes through final generator)
        max_depth: stop flattening after N levels (default: -1 = any value <0 is no maximum)

    Returns:
        A generator of values, or func(generator)
    """
    def _gen(lst) -> Generator[T, None, None]:
        for i in lst:
            if isinstance(i, Iterable) and not isinstance(i, (str, bytes)):
                if max_depth == 0:
                    yield i
                else:
                    yield from flatten(i, max_depth=max_depth-1)
            else:
                yield i
    return func(_gen(lst))

