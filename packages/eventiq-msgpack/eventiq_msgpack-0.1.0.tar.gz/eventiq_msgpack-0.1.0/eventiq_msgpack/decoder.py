from __future__ import annotations

from typing import Any

import ormsgpack
from eventiq.exceptions import DecodeError
from eventiq.types import RawData, T


class MsgPackDecoder:
    def __init__(self, **options):
        self.options = options

    def decode(self, data: RawData, as_type: type[T] | None = None) -> T | Any:
        try:
            unpacked = ormsgpack.unpackb(data)
            if as_type is None:
                return unpacked
            return as_type.model_validate(unpacked, **self.options)

        except ormsgpack.MsgpackDecodeError as e:
            raise DecodeError from e
