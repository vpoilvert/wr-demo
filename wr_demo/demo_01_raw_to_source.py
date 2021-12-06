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


def get_raw_file(file_type: FileType, year: int = 2020) -> Path:
    return RAW_DIR / file_type.value / f'year={year}' / f'{file_type.value}.csv.gz'


def get_source_file(file_type: FileType, year: int = 2020) -> Path:
    return SRC_DIR / file_type.value / f'year={year}' / f'{file_type.value}.snappy.parquet'


if __name__ == '__main__':
    file_type = FileType.VEHICULES
    raw_file = get_raw_file(file_type, 2020)
    source_file = get_source_file(file_type, 2020)

    # read csv

    # rename columns

    # map values

    # to parquet
