from dataclasses import dataclass, field

import pandas as pd


from whiffle_client.common.components.base import BaseComponent


# pylint: disable=duplicate-code
@dataclass
class ForecastModel(BaseComponent):
    """Forecast model"""

    reference_time: pd.Timestamp = field(default=None)
    asset_name: int = field(default=None)
    name: str = field(default="blender")
    steps: dict = field(default=None)
