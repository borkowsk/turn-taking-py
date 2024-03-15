"""Make group-level data."""
from pathlib import Path
import pandas as pd
from tqdm import tqdm
from tt.dataloader import Dataloader
from tt.metrics import Metrics
from tt.uniseq import Uniseq

wb_level = 1  # Level of verbosity

HERE = Path(__file__).parent
DATA = HERE/"data"
RAWD = DATA/"raw"
META = DATA/"meta"

if wb_level > 0:
    print("\nCONFIGURATION:\n\t",DATA,"\n\t",META,"\n\t",RAWD)

if wb_level > 0:
    print("\nLOADING DATA from", META/"propmap-groups.csv")
config  = dict(header=None)
dloader = Dataloader(RAWD, META/"propmap-groups.csv", **config)
df = list(dloader)[0]

if wb_level > 0:
    print("\nMAKING RAW GROUPS in ", DATA/"groups-raw.tsv")
D = pd.concat(list(dloader), axis=0)
D.to_csv(DATA/"groups-raw.tsv", sep="\t", index=False)

if wb_level > 0:
    print("\nMAKING GROUPS in ", DATA/"groups.tsv")
M = pd.DataFrame(
    Metrics(df).dump()
    for df in tqdm(dloader, total=dloader.n_paths)
)
M.to_csv(DATA/"groups.tsv", sep="\t", index=False)

if wb_level > 0:
    print("\nMAKING SEQUENCES in ", DATA/"sequences.tsv")
S = pd.concat([
    Metrics(df).sdata
    for df in tqdm(dloader, total=dloader.n_paths)
])
S.to_csv(DATA/"sequences.tsv", sep="\t", index=False)

if wb_level > 0:
    print("\nMAKING UNI-SEQUENCES in ", DATA/"uniseq.tsv")
U = pd.concat([
    Uniseq(df).dump()
    for df in tqdm(dloader, total=dloader.n_paths)
], axis=0)
U.to_csv(DATA/"uniseq.tsv", sep="\t", index=False)




