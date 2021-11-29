CREATE EXTERNAL TABLE IF NOT EXISTS `demo`.`vehicules` (
    `id_accident` bigint,
    `id_vehicule` string,
    `num_vehicule` string,
    `sens_circulation` int,
    `categorie` string,
    `obstacle_fixe_heurte` string,
    `obstacle_mobile_heurte` int,
    `point_choc_initial` int,
    `manoeuvre_avant_accident` int,
    `motorisation` int,
    `occutc` double
) PARTITIONED BY (
    year int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
WITH SERDEPROPERTIES (
    'serialization.format' = '1'
) LOCATION 's3://wescale-pandas-demo/source/vehicules'
TBLPROPERTIES ('has_encrypted_data'='false')
;
