from datetime import date

import pytest
from eventiq import CloudEvent


@pytest.fixture()
def cloudevent() -> CloudEvent:
    return CloudEvent.new(
        {"today": date.today().isoformat(), "arr": [1, "2", 3.0]},
        type="TestEvent",
        topic="test_topic",
    )
