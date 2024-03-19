"""Make user-level data."""
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

U = pd.concat([
    Metrics(df).dump(mode="user")
    for df in tqdm(dloader)
], ignore_index=True)

U.to_csv(DATA/"users.tsv", sep="\t", index=False)
