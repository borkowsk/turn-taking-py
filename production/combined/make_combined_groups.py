"""Make combined (structured+free form) groups data."""
from pathlib import Path
import numpy as np
import pandas as pd

HERE = Path(__file__).parent
PROD = HERE.parent
DATA = HERE/"data"

sdf = pd.read_csv(PROD/"structured"/"data"/"groups.tsv", sep="\t")
fdf = pd.read_csv(PROD/"freeform"/"data"/"groups.tsv", sep="\t")

cdf = pd.concat([sdf, fdf]) \
    .drop(columns="idx") \
    .assign(condition=lambda df: pd.Categorical(
        df["condition"].fillna("free"),
        categories=["creative", "math", "controv", "free"]
    )) \
    .groupby("ts") \
    .filter(lambda gdf: len(gdf) == 2) \
    .sort_values(by=["ts", "condition"], ascending=True) \
    .reset_index(drop=True)

keys = ("fname", "ts", "condition")
diffcols = ("time_average", *tuple(
    c for c in cdf.columns
    if not c.startswith("time_") and not c.startswith("n_")
    and c not in keys
))

ddf = cdf.loc[:, [*keys, *diffcols]].copy() \
    .groupby("ts").apply(lambda df: pd.Series({
        **{ k: df[k].to_numpy()[0] for k in keys },
        **{ c: np.diff(df[c].to_numpy())[0] for c in diffcols }
    })) \
    .assign(condition=lambda df: pd.Categorical(
        df["condition"].fillna("free"),
        categories=["creative", "math", "controv"]
    )) \
    .sort_values(by="condition", ascending=True) \
    .reset_index(drop=True)

cdf.to_csv(DATA/"combined.tsv", sep="\t", index=False)
ddf.to_csv(DATA/"diff.tsv", sep="\t", index=False)
