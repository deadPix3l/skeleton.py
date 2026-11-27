from pkgutil import resolve_name
import logging

def _no_op(*args, **kwargs) -> None:
    return None

def prefer(*import_strs: str, warn: bool = True):
    """
    decorate shims for optional imports.

    Instead of constantly doing a try-except in your imports,
    just build the shim, and this decorator will swap out the
    official version if available
    """
    def decorator[T](shim: T = _no_op) -> T | Any:
        for import_str in import_strs:
            try:
                return resolve_name(import_str)
            except (ModuleNotFoundError, ImportError, AttributeError):
                continue
        if warn:
            logging.warning(
                "None of %s found, using default shim (%s); some functionality might not be available",
                ", ".join(import_strs),
                shim.__qualname__,
            )
        return shim
    return decorator

"""
Examples:
>>> @prefer("tqdm:tqdm")
... class tqdm:
...     ''' default shim if tqdm not available '''
...     def __init__(*args, **kwargs):
...         pass
...     def __call__(*args, **kwargs):
...         pass

# no shim needed, default shim is _no_op(),
# but json:dumps is stdlib and will always resolve
>>> dumps = prefer("orjson:dumps", "ujson:dumps", "json:dumps", warn=False)
"""
