# -*- coding: utf-8 -*-
'''
Idem demo 1 mais en full s3 avec aws data wrangler.
'''
from typing import cast

import awswrangler as wr
import pandas as pd

from wr_demo.raw_mapping import *


def get_raw_file(file_type: FileType, year: int) -> str:
    return f's3://{BUCKET_NAME}/raw/{file_type.value}/year={year}/{file_type.value}.csv.gz'


def get_source_file(file_type: FileType, year: int) -> str:
    return f's3://{BUCKET_NAME}/source/{file_type.value}/year={year}/{file_type.value}.snappy.parquet'


if __name__ == '__main__':
    for file_type in FileType:
        raw_file = get_raw_file(file_type, 2020)
        raw_df = wr.s3.read_csv(raw_file, sep=';')

        source_df = transform_dataframe(file_type, cast(pd.DataFrame, raw_df))

        source_file = get_source_file(file_type, 2020)
        wr.s3.to_parquet(source_df, source_file, compression='snappy')
