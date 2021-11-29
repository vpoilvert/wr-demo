CREATE EXTERNAL TABLE IF NOT EXISTS `demo`.`caracteristiques` (
    `id_accident` bigint,
    `hrmn` string,
    `lumiere` string,
    `departement` string,
    `commune` string,
    `localisation` string,
    `intersection` string,
    `conditions_atmospheriques` string,
    `type_collision` string,
    `addresse` string,
    `latitude` string,
    `longitude` string,
    `date_accident` date
) PARTITIONED BY (
    year int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
WITH SERDEPROPERTIES (
    'serialization.format' = '1'
) LOCATION 's3://wescale-pandas-demo/source/caracteristiques'
TBLPROPERTIES ('has_encrypted_data'='false')
;
