# -*- coding: utf-8 -*-
'''
Utilisation de data wrangler pour récupérer les résultats d'une requète Athena.
'''
import awswrangler as wr

from wr_demo.raw_mapping import *

QUERY = '''SELECT gravite_blessure, count(*) as count_usagers
FROM usagers, vehicules
WHERE usagers.id_accident = vehicules.id_accident
AND usagers.id_vehicule = vehicules.id_vehicule
AND vehicules.categorie = 'bicyclette'
GROUP BY 1
ORDER BY 2 DESC
;
'''

if __name__ == '__main__':
    df = wr.athena.read_sql_query(QUERY, database='demo')

    print(df)
