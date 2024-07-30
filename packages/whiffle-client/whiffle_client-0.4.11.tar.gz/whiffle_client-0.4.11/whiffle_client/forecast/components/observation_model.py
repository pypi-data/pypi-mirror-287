from dataclasses import dataclass, field

import pandas as pd

from whiffle_client.common.components.base import BaseComponent


# pylint: disable=duplicate-code
@dataclass
class ObservationModel(BaseComponent):
    """Observation model"""

    time: pd.Timestamp = field(default=None)
    quantity: str = field(default=None)
    value: float = field(default=None)
    asset_name: int = field(default=None)
