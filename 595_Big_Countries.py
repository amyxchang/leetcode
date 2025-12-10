"""
(blank python file for LeetCode problem 595 - Big Countries)
"""
# completed 12/10/2025

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:

    df = world[(world["area"] >= 3000000) | (world["population"] >= 25000000)]
    df = df[["name","population","area"]]
    return df
