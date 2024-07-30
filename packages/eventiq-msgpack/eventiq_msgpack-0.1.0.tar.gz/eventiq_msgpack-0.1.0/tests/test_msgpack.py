from eventiq import CloudEvent

from eventiq_msgpack import MsgPackDecoder, MsgPackEncoder


def test_msgpack_decoder(cloudevent):
    encoder = MsgPackEncoder()
    decoder = MsgPackDecoder()
    encoded = encoder.encode(cloudevent)
    assert isinstance(encoded, bytes)
    decoded = decoder.decode(encoded, as_type=CloudEvent)
    assert decoded == cloudevent
