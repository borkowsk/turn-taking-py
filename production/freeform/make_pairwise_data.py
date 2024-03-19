"""Make pairwise data."""
from pathlib import Path
import pandas as pd
from tqdm import tqdm
from tt.dataloader import Dataloader
from tt.metrics import Metrics

HERE = Path(__file__).parent
DATA = HERE/"data"
RAWD = DATA/"raw"

config = dict(
    header=0,
    usecols=("Tier", "Begin time [ss.ms]", "End time [ss.ms]", "content"),
    dtfmt="%Y.%m.%d_%H.%M"
)

dloader = Dataloader(RAWD, **config)

P = pd.concat([
    Metrics(df).dump(mode="pairwise")
    for df in tqdm(dloader)
], ignore_index=True)

P.to_csv(DATA/"pairwise.tsv", sep="\t", index=False)
