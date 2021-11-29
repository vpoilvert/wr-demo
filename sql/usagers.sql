CREATE EXTERNAL TABLE IF NOT EXISTS `demo`.`usagers_raw` (
    `Num_Acc` string,
    `id_vehicule` string,
    `num_veh` string,
    `place` string,
    `catu` string,
    `grav` string,
    `sexe` string,
    `an_nais` string,
    `trajet` string,
    `secu1` string,
    `secu2` string,
    `secu3` string,
    `locp` string,
    `actp` string,
    `etatp` string
) PARTITIONED BY (
    year int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    "separatorChar" = ";"
) LOCATION 's3://wescale-pandas-demo/raw/usagers'
TBLPROPERTIES (
    'has_encrypted_data'='false',
    "skip.header.line.count"="1"
)
;

CREATE EXTERNAL TABLE IF NOT EXISTS `demo`.`usagers` (
    `id_accident` bigint,
    `id_vehicule` string,
    `num_vehicule` string,
    `place` int,
    `categorie_usager` string,
    `gravite_blessure` string,
    `sexe` string,
    `annee_naissance` int,
    `motif_deplacement` string,
    `equipement_securite_1` string,
    `equipement_securite_2` string,
    `equipement_securite_3` string,
    `locp` int,
    `actp` string,
    `etatp` int
) PARTITIONED BY (
    year int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
WITH SERDEPROPERTIES (
    'serialization.format' = '1'
) LOCATION 's3://wescale-pandas-demo/source/usagers'
TBLPROPERTIES ('has_encrypted_data'='false')
;
