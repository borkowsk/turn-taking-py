"""Make group-level data."""
from pathlib import Path
import pandas as pd
from tqdm import tqdm
from tt.dataloader import Dataloader
from tt.metrics import Metrics
from tt.uniseq import Uniseq

HERE = Path(__file__).parent
DATA = HERE/"data"
RAWD = DATA/"raw"

config = dict(
    header=0,
    usecols=("Tier", "Begin time [ss.ms]", "End time [ss.ms]", "content"),
    dtfmt="%Y.%m.%d_%H.%M"
)

dloader = Dataloader(RAWD, **config)
df = list(dloader)[0]

D = pd.concat(list(dloader), axis=0)
M = pd.DataFrame(
    Metrics(df).dump()
    for df in tqdm(dloader, total=dloader.n_paths)
)
S = pd.concat([
    Metrics(df).sdata
    for df in tqdm(dloader, total=dloader.n_paths)
])
U = pd.concat([
    Uniseq(df).dump()
    for df in tqdm(dloader, total=dloader.n_paths)
], axis=0)

D.to_csv(DATA/"groups-raw.tsv", sep="\t", index=False)
M.to_csv(DATA/"groups.tsv", sep="\t", index=False)
S.to_csv(DATA/"sequences.tsv", sep="\t", index=False)
U.to_csv(DATA/"uniseq.tsv", sep="\t", index=False)
