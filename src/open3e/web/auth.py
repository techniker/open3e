"""Simple password hashing/verification using hashlib.scrypt."""

from __future__ import annotations

import hashlib
import os


def hash_password(password: str) -> str:
    """Hash *password* with scrypt. Returns 'salt_hex:hash_hex'."""
    salt = os.urandom(16)
    hashed = hashlib.scrypt(
        password.encode(),
        salt=salt,
        n=16384,
        r=8,
        p=1,
        dklen=32,
    )
    return f"{salt.hex()}:{hashed.hex()}"


def verify_password(password: str, stored_hash: str) -> bool:
    """Verify *password* against a stored 'salt_hex:hash_hex' string."""
    try:
        salt_hex, hash_hex = stored_hash.split(":", 1)
    except ValueError:
        return False
    salt = bytes.fromhex(salt_hex)
    expected = bytes.fromhex(hash_hex)
    actual = hashlib.scrypt(
        password.encode(),
        salt=salt,
        n=16384,
        r=8,
        p=1,
        dklen=32,
    )
    return actual == expected
