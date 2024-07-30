"""NEOS-HMAC signing implementation."""

from __future__ import annotations

import logging
import typing

logger = logging.getLogger(__name__)


class KeyPair(typing.NamedTuple):
    """User access key pair representation."""

    access_key_id: str
    secret_access_key: str
    partition: str
