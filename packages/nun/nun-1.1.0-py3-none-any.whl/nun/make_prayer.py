import logging
import random

logger = logging.getLogger(__file__)


def pray() -> None:
    prayers = ["Hallelujah!", "Amen!", "Praise the Lord!", "God bless you!"]
    chosen_prayer = random.choice(prayers)
    print(chosen_prayer)
