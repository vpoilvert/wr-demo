CREATE EXTERNAL TABLE IF NOT EXISTS `demo`.`lieux` (
	`id_accident` bigint,
	`int` int,
	`categorie_route` string,
	`numero_route` string,
	`v1` int,
	`v2` string,
	`regime_circulation` string,
	`nombre_voies_circulation` int,
	`presence_voie_reservee` string,
	`profil_route` string,
	`numero_point_routier` string,
	`distance_point_routier` string,
	`trace_en_plan` string,
	`largeur_terre_plein_central` string,
	`largeur_chaussee` string,
	`etat_surface` string,
	`amenagement_infrastringucture` string,
	`situation_accident` string,
    `vitesse_max_autorisee` int
) PARTITIONED BY (
    year int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
WITH SERDEPROPERTIES (
    'serialization.format' = '1'
) LOCATION 's3://wescale-pandas-demo/source/lieux'
TBLPROPERTIES ('has_encrypted_data'='false')
;
