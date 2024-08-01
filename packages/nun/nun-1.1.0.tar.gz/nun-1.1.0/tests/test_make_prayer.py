import logging

import nun

logger = logging.getLogger("make_prayer")


class TestPrayers:
    def test_pray(self):
        assert nun.pray() is None
