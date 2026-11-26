from functools import wraps
from collections.abc import Callable, Iterable

#foss-alt: from funcy import collecting
def collecting[T](func: Callable[..., Iterable[T]]) -> Callable[..., list[T]]:
    """
    materializes a functions result into a list
    
    This allows you to write a function as a generator,
    while actually returning a list,
    without the mess of:
    ```
    result = []
    for i in items:
        result.append(i)
    return result
    ```

    replace all your `list.append(i)` calls with `yield i`.
    The above example, given it has no additional transformation or decisions in the loop,
    can be further simplified to `yield from items`

    WARNING: this function will attempt to materialize infinite iterators
    It is your responsibility to prevent this.
    If you do not, you WILL run out of memory and crash.
    """
    @wraps(func)
    def wrapped(*args, **kwargs) -> list[T]:
        return list(func(*args, **kwargs))
    return wrapped

#foss-alt: from funcy import joining
def joining(sep: str = "\n"):
    """
    converts a function that returns an iterable to return a string using str.join()
    """
    def decorator(func: Callable[..., Iterable]) -> Callable[..., str]:
        @wraps(func)
        def wrapped(*args, **kwargs) -> str:
            return str(sep).join(func(*args, **kwargs))
        return wrapped
    return decorator

