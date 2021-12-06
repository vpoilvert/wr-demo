# -*- coding: utf-8 -*-
'''
Le but de cette seconde demo est de monter comment faire des stats avec Pandas.

On calcule le nombre cumulé d'accidents de bicyclette par type d'obstable fixe.
'''
from pathlib import Path

import pandas as pd

from wr_demo.raw_mapping import *


def get_source_file(file_type: FileType, year: int) -> Path:
    return SRC_DIR / file_type.value / f'year={year}' / f'{file_type.value}.snappy.parquet'


if __name__ == '__main__':
    source_file = get_source_file(FileType.VEHICULES, 2020)
    df = pd.read_parquet(source_file, engine='pyarrow')

    df = df[df['categorie'] == 'bicyclette']
    df = df[df['obstacle_fixe_heurte'] != 'non renseigné']
    df = df[['id_accident', 'obstacle_fixe_heurte']]
    result = df.groupby('obstacle_fixe_heurte').count(
    ).sort_values(by='id_accident', ascending=False)

    print(result.head(20))
