# -*- coding: utf-8 -*-
'''
Dans cette première démo le but est de :
* Lire les fichiers CSV téléchargés
* Faire du mapping de colonnes/valeurs
* Sauvegarder le résultat au format parquet
'''
from pathlib import Path

import pandas as pd

from wr_demo.raw_mapping import *


def get_raw_file(file_type: FileType, year: int) -> Path:
    return RAW_DIR / file_type.value / f'year={year}' / f'{file_type.value}.csv.gz'


def get_source_file(file_type: FileType, year: int) -> Path:
    return SRC_DIR / file_type.value / f'year={year}' / f'{file_type.value}.snappy.parquet'


if __name__ == '__main__':
    for file_type in FileType:
        raw_file = get_raw_file(file_type, 2020)
        raw_df = pd.read_csv(raw_file, sep=';')

        source_df = transform_dataframe(file_type, raw_df)
        source_file = get_source_file(file_type, 2020)
        source_file.parent.mkdir(parents=True)

        source_df.to_parquet(source_file,
                             engine='pyarrow',
                             compression='snappy',
                             )
