def has_hex_prefix(hex_string: str) -> bool:
    return hex_string.startswith("0x")


def add_hex_prefix(hex_string: str) -> str:
    if not has_hex_prefix(hex_string):
        return "0x" + hex_string
    return hex_string


def remove_hex_prefix(hex_string: str) -> str:
    if has_hex_prefix(hex_string):
        return hex_string[len("0x"):]

    return hex_string


def to_hex(b: bytes) -> str:
    return add_hex_prefix(b.hex())


def hex_to_bytes(hex_string: str) -> bytes:
    return bytes.fromhex(remove_hex_prefix(hex_string))


def compare_bytes(a: bytes, b: bytes) -> int:
    n = min(len(a), len(b))
    for i in range(n):
        if a[i] != b[i]:
            return a[i] - b[i]

    return len(a) - len(b)


def equals_bytes(a: bytes, b: bytes) -> bool:
    if len(a) != len(b):
        return False
    for i, e in enumerate(a):
        if e != b[i]:
            return False
    return True


def concat_bytes(a: bytes, b: bytes) -> bytes:
    return a+b
