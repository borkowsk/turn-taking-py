"""Make pairwise data."""
from pathlib import Path
import pandas as pd
from tqdm import tqdm
from tt.dataloader import Dataloader
from tt.metrics import Metrics

HERE = Path(__file__).parent
DATA = HERE/"data"
RAWD = DATA/"raw"
META = DATA/"meta"

configd = dict(header=None)
dloader = Dataloader(RAWD, META/"propmap-groups.csv", **configd)

P = pd.concat([
    Metrics(df).dump(mode="pairwise")
    for df in tqdm(dloader)
], ignore_index=True)

P.to_csv(DATA/"pairwise.tsv", sep="\t", index=False)
