from typing import Any

"""
Pure label-generation logic for supervised tuning tasks.
"""

LabelType: Any
def forward_return_labels(prices: pd.Series[float], horizon: int) -> pd.Series[float]: ...
def sign_labels(prices: pd.Series[float], horizon: int) -> pd.Series[float]: ...
def excess_return_labels(prices: pd.Series[float], benchmark: pd.Series[float], horizon: int) -> pd.Series[float]: ...
