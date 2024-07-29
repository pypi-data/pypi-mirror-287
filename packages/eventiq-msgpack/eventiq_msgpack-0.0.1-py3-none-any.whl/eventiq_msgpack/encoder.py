import ormsgpack
from eventiq.exceptions import EncodeError
from pydantic import BaseModel


class MsgPackEncoder:
    CONTENT_TYPE = "application/x-msgpack"

    def __init__(self, **options) -> None:
        self.options = options

    def encode(self, data: BaseModel) -> bytes:
        try:
            return ormsgpack.packb(data, **self.options)
        except ormsgpack.MsgpackEncodeError as e:
            raise EncodeError from e
