from __future__ import annotations

from typing import Any

import ormsgpack
from eventiq.exceptions import DecodeError
from eventiq.types import RawData, T
from pydantic import TypeAdapter

AnyType: TypeAdapter = TypeAdapter(Any)


class MsgPackDecoder:
    def __init__(self, **options):
        self.options = options

    def decode(self, data: RawData, as_type: type[T] | None = None) -> T | Any:
        try:
            unpacked = ormsgpack.unpackb(data)
            if as_type:
                return as_type.model_validate_json(unpacked, **self.options)
            return AnyType.validate_json(unpacked, **self.options)

        except ormsgpack.MsgpackDecodeError as e:
            raise DecodeError from e
