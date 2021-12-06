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
    file_type = FileType.VEHICULES
    raw_file = get_raw_file(file_type, 2020)
    source_file = get_source_file(file_type, 2020)

    # read csv
    raw_df = wr.s3.read_csv(raw_file, sep=';')

    # rename columns

    # map values

    # to parquet
