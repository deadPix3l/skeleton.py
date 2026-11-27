def normalize_string(
    s: str,
    prefix: str = "",
    suffix: str = "",
) -> str:
    return prefix + s.removeprefix(prefix).removesuffix(suffix) + suffix

