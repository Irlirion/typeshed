from _typeshed import Incomplete

import pandas as pd

pd_version: Incomplete

class PandasPdb:
    pdb_text: str
    header: str
    code: str
    pdb_path: str
    def __init__(self) -> None: ...
    @property
    def df(self): ...
    @df.setter
    def df(self, value) -> None: ...
    def read_pdb(self, path): ...
    def read_pdb_from_list(self, pdb_lines): ...
    def fetch_pdb(self, pdb_code: str | None = None, uniprot_id: str | None = None, source: str = "pdb"): ...
    def get(self, s, df: Incomplete | None = None, invert: bool = False, records=("ATOM", "HETATM")): ...
    def impute_element(self, records=("ATOM", "HETATM"), inplace: bool = False): ...
    @staticmethod
    def rmsd(df1, df2, s: Incomplete | None = None, invert: bool = False): ...
    def amino3to1(self, record: str = "ATOM", residue_col: str = "residue_name", fillna: str = "?"): ...
    def distance(self, xyz=(0.0, 0.0, 0.0), records=("ATOM", "HETATM")): ...
    @staticmethod
    def distance_df(df, xyz=(0.0, 0.0, 0.0)): ...
    def to_pdb(self, path, records: Incomplete | None = None, gz: bool = False, append_newline: bool = True) -> None: ...
    def parse_sse(self) -> None: ...
    def get_model_start_end(self) -> pd.DataFrame: ...
    def label_models(self): ...
    def get_model(self, model_index: int) -> PandasPdb: ...
    def get_models(self, model_indices: list[int]) -> PandasPdb: ...