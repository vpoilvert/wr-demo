# -*- coding: utf-8 -*-
from enum import Enum
from pathlib import Path

import pandas as pd

WR_DEMO_DIR = Path(__file__).parent.parent
RAW_DIR = WR_DEMO_DIR / 'raw'
SRC_DIR = WR_DEMO_DIR / 'source'
BUCKET_NAME = 'wescale-pandas-demo'


class FileType(Enum):
    CARACTERISTIQUES = 'caracteristiques'
    LIEUX = 'lieux'
    USAGERS = 'usagers'
    VEHICULES = 'vehicules'


CARACTERISTIQUES_CSV_TYPES = {
    'Num_Acc': 'int64',
    'jour':    'uint8',
    'mois':    'uint8',
    'an':      'uint16',
    'hrmn':    'object',
    'lum':     'uint8',
    'dep':     'object',
    'com':     'object',
    'agg':     'uint8',
    'int':     'int8',
    'atm':     'int8',
    'col':     'int8',
    'adr':     'object',
    'lat':     'object',
    'long':    'object',

}

CARACTERISTIQUES_MAPPING_COLUMNS = {
    'Num_Acc': 'id_accident',
    'num_veh': 'num_vehicule',
    'lum': 'lumiere',
    'dep': 'departement',
    'com': 'commune',
    'agg': 'localisation',
    'int': 'intersection',
    'atm': 'conditions_atmospheriques',
    'col': 'type_collision',
    'adr': 'addresse',
    'lat': 'latitude',
    'long': 'longitude',
}

CARACTERISTIQUES_MAPPING_VALUES = {
    'lumiere': {
        1: 'plein jour',
        2: 'crépuscule ou aube',
        3: 'nuit sans éclairage public',
        4: 'nuit avec éclairage public non allumé',
        5: 'nuit avec éclairage public allumé',
    },
    'localisation': {
        1: 'hors agglomération',
        2: 'en agglomération',
    },
    'intersection': {
        1: 'hors intersection',
        2: 'intersection en x',
        3: 'intersection en t',
        4: 'intersection en y',
        5: 'intersection à plus de 4 branches',
        6: 'giratoire',
        7: 'place',
        8: 'passage à niveau',
        9: 'autre intersection',
    },
    'conditions_atmospheriques': {
        -1: 'non renseigné',
        1: 'normale',
        2: 'pluie légère',
        3: 'pluie forte',
        4: 'neige - grêle',
        5: 'brouillard - fumée',
        6: 'vent fort - tempête',
        7: 'temps éblouissant',
        8: 'temps couvert',
        9: 'autre',
    },
    'type_collision': {
        1: 'non renseigné',
        1: 'deux véhicules - frontale',
        2: 'deux véhicules - par l’arrière',
        3: 'deux véhicules - par le coté',
        4: 'trois véhicules et plus - en chaîne',
        5: 'trois véhicules et plus - collisions multiples',
        6: 'autre collision',
        7: 'sans collision',
    },
}

LIEUX_CSV_TYPES = {
    'Num_Acc': 'int64',
    'catr': 'uint8',
    'voie': 'str',
    'v1': 'int8',
    'v2': 'str',
    'circ': 'int8',
    'nbv': 'int8',
    'vosp': 'int8',
    'prof': 'int8',
    'pr': 'str',
    'pr1': 'str',
    'plan': 'int8',
    'lartpc': 'str',
    'larrout': 'str',
    'surf': 'int8',
    'infra': 'int8',
    'situ': 'int8',
    'vma': 'int16',
}

LIEUX_MAPPING_COLUMNS = {
    'Num_Acc': 'id_accident',
    'catr': 'categorie_route',
    'voie': 'numero_route',
    'circ': 'regime_circulation',
    'nbv': 'nombre_voies_circulation',
    'vosp': 'presence_voie_reservee',
    'prof': 'profil_route',
    'pr': 'numero_point_routier',
    'pr1': 'distance_point_routier',
    'plan': 'trace_en_plan',
    'lartpc': 'largeur_terre_plein_central',
    'larrout': 'largeur_chaussee',
    'surf': 'etat_surface',
    'infra': 'amenagement_infrastructure',
    'situ': 'situation_accident',
    'vma': 'vitesse_max_autorisee',
}

LIEUX_MAPPING_VALUES = {
    'categorie_route': {
        1: 'autoroute',
        2: 'route nationale',
        3: 'route départementale',
        4: 'voie communales',
        5: 'hors réseau public',
        6: 'parc de stationnement ouvert à la circulation publique',
        7: 'routes de métropole urbaine',
        9: 'autre',
    },
    'regime_circulation': {
        -1: 'non renseigné',
        1: 'a sens unique',
        2: 'bidirectionnelle',
        3: 'a chaussées séparées',
        4: 'avec voies d’affectation variable',
    },
    'presence_voie_reservee': {
        -1: 'non renseigné',
        0: 'sans objet',
        1: 'piste cyclable',
        2: 'bande cyclable',
        3: 'voie réservée',
    },
    'profil_route': {
        -1: 'non renseigné',
        1: 'plat',
        2: 'pente',
        3: 'sommet de côte',
        4: 'bas de côte',
    },
    'trace_en_plan': {
        -1: 'non renseigné',
        1: 'partie rectiligne',
        2: 'en courbe à gauche',
        3: 'en courbe à droite',
        4: 'en « s »',
    },
    'etat_surface': {
        -1: 'non renseigné',
        1: 'normale',
        2: 'mouillée',
        3: 'flaques',
        4: 'inondée',
        5: 'enneigée',
        6: 'boue',
        7: 'verglacée',
        8: 'corps gras – huile',
        9: 'autre',
    },
    'amenagement_infrastructure': {
        -1: 'non renseigné',
        0: 'aucun',
        1: 'souterrain - tunnel',
        2: 'pont - autopont',
        3: 'bretelle d’échangeur ou de raccordement',
        4: 'voie ferrée',
        5: 'carrefour aménagé',
        6: 'zone piétonne',
        7: 'zone de péage',
        8: 'chantier',
        9: 'autres',
    },
    'situation_accident': {
        -1: 'non renseigné',
        0: 'aucun',
        1: 'sur chaussée',
        2: 'sur bande d’arrêt d’urgence',
        3: 'sur accotement',
        4: 'sur trottoir',
        5: 'sur piste cyclable',
        6: 'sur autre voie spéciale',
        8: 'autres',
    },
}

USAGERS_CSV_TYPES = {
    'Num_Acc': 'int64',
    'id_vehicule': 'string',
    'num_veh': 'string',
    'place': 'uint8',
    'catu': 'uint8',
    'grav': 'uint8',
    'sexe': 'uint8',
    'an_nais': 'uint16',
    'trajet': 'int8',
    'secu1': 'int8',
    'secu2': 'int8',
    'secu3': 'int8',
}

USAGERS_MAPPING_COLUMNS = {
    'Num_Acc': 'id_accident',
    'num_veh': 'num_vehicule',
    'catu': 'categorie_usager',
    'grav': 'gravite_blessure',
    'an_nais': 'annee_naissance',
    'trajet': 'motif_deplacement',
    'secu1': 'equipement_securite_1',
    'secu2': 'equipement_securite_2',
    'secu3': 'equipement_securite_3',
}

_MAPPING_EQUIPEMENT_SECURITE = {
    -1: 'non renseigné',
    0: 'aucun équipement',
    1: 'ceinture',
    2: 'casque',
    3: 'dispositif enfants',
    4: 'gilet réfléchissant',
    5: 'airbag (2rm/3rm)',
    6: 'gants (2rm/3rm)',
    7: 'gants + airbag (2rm/3rm)',
    8: 'non déterminable',
    9: 'autre',
}

USAGERS_MAPPING_VALUES = {
    'categorie_usager': {
        1: 'conducteur',
        2: 'passager',
        3: 'piéton',
    },
    'gravite_blessure': {
        1: 'indemne',
        2: 'tué',
        3: 'blessé hospitalisé',
        4: 'blessé léger',
    },
    'sexe': {
        1: 'masculin',
        2: 'féminin',
    },
    'motif_deplacement': {
        -1: ' non renseigné',
        0: 'non renseigné',
        1: 'domicile – travail',
        2: 'domicile – école',
        3: 'courses – achats',
        4: 'utilisation professionnelle',
        5: 'promenade – loisirs',
        9: 'autre',
    },
    'equipement_securite_1': _MAPPING_EQUIPEMENT_SECURITE,
    'equipement_securite_2': _MAPPING_EQUIPEMENT_SECURITE,
    'equipement_securite_3': _MAPPING_EQUIPEMENT_SECURITE,
}

VEHICULES_CSV_TYPES = {
    'Num_Acc': 'int64',
    'id_vehicule': 'string',
    'num_veh': 'string',
    'senc': 'int8',
    'catv': 'uint8',
    'obs': 'int8',
    'obsm': 'int8',
    'choc': 'int8',
    'manv': 'int8',
    'motor': 'int8',
    'occutc': 'float16',
}

VEHICULES_MAPPING_COLUMNS = {
    'Num_Acc': 'id_accident',
    'num_veh': 'num_vehicule',
    'senc': 'sens_circulation',
    'catv': 'categorie',
    'obs': 'obstacle_fixe_heurte',
    'obsm': 'obstacle_mobile_heurte',
    'choc': 'point_choc_initial',
    'manv': 'manoeuvre_avant_accident',
    'motor': 'motorisation',
    'nombre_occupants': 'occutc',
}

VEHICULES_MAPPING_VALUES = {
    'categorie': {
        0: 'indéterminable',
        1: 'bicyclette',
        2: 'cyclomoteur <50cm3',
        3: 'voiturette',
        4: 'scooter immatriculé',  # inutilisé depuis 2006
        5: 'motocyclette',  # inutilisé depuis 2006
        6: 'side-car',  # inutilisé depuis 2006
        7: 'vl seul',
        8: 'vl + caravane',  # inutilisé depuis 2006
        9: 'vl + remorque',  # inutilisé depuis 2006
        10: 'vu seul 1,5t <= ptac <= 3,5t avec ou sans remorque',
        11: 'vu (10) + caravane',  # inutilisé depuis 2006
        12: 'vu (10) + remorque',  # inutilisé depuis 2006
        13: 'pl seul 3,5t <ptca <= 7,5t',
        14: 'pl seul > 7,5t',
        15: 'pl > 3,5t + remorque',
        16: 'tracteur routier seul',
        17: 'tracteur routier + semi-remorque',
        18: 'transport en commun',  # inutilisé depuis 2006
        19: 'tramway (inutilisé)',  # inutilisé depuis 2006
        20: 'engin spécial',  # inutilisé depuis 2006
        21: 'tracteur agricole',  # inutilisé depuis 2006
        30: 'scooter < 50 cm3',  # inutilisé depuis 2006
        31: 'motocyclette > 50 cm 3 et <= 125 cm 3',  # inutilisé depuis 2006
        32: 'scooter > 50 cm 3 et <= 125 cm 3',  # inutilisé depuis 2006
        33: 'motocyclette > 125 cm 3',  # inutilisé depuis 2006
        34: 'scooter > 125 cm 3',  # inutilisé depuis 2006
        35: 'quad léger <= 50 cm 3',
        36: 'quad lourd > 50 cm 3',
        37: 'autobus',
        38: 'autocar',
        39: 'train',
        40: 'tramway',
        41: '3rm <= 50 cm3',
        42: '3rm > 50 cm3 <= 125 cm3',
        43: '3rm > 125 cm3',
        50: 'edp à moteur',
        60: 'edp sans moteur',
        80: 'vae',
        99: 'autre véhicule',
    },
    'obstacle_fixe_heurte': {
        -1: 'non renseigné',
        0: 'sans objet',
        1: 'véhicule en stationnement',
        2: 'arbre',
        3: 'glissière métallique',
        4: 'glissière béton',
        5: 'autre glissière',
        6: 'bâtiment, mur, pile de pont',
        7: 'support de signalisation verticale ou poste d’appel d’urgence',
        8: 'poteau',
        9: 'mobilier urbain',
        10: 'parapet',
        11: 'ilot, refuge, borne haute',
        12: 'bordure de trottoir',
        13: 'fossé, talus, paroi rocheuse',
        14: 'autre obstacle fixe sur chaussée',
        15: 'autre obstacle fixe sur trottoir ou accotement',
        16: 'sortie de chaussée sans obstacle',
        17: 'buse – tête d’aqueduc',
    }
}

ALL_CSV_TYPES = {
    FileType.CARACTERISTIQUES: CARACTERISTIQUES_CSV_TYPES,
    FileType.LIEUX: LIEUX_CSV_TYPES,
    FileType.USAGERS: USAGERS_CSV_TYPES,
    FileType.VEHICULES: VEHICULES_CSV_TYPES,
}

ALL_MAPPING_COLUMNS = {
    FileType.CARACTERISTIQUES: CARACTERISTIQUES_MAPPING_COLUMNS,
    FileType.LIEUX: LIEUX_MAPPING_COLUMNS,
    FileType.USAGERS: USAGERS_MAPPING_COLUMNS,
    FileType.VEHICULES: VEHICULES_MAPPING_COLUMNS,
}

ALL_MAPPING_VALUES = {
    FileType.CARACTERISTIQUES: CARACTERISTIQUES_MAPPING_VALUES,
    FileType.LIEUX: LIEUX_MAPPING_VALUES,
    FileType.USAGERS: USAGERS_MAPPING_VALUES,
    FileType.VEHICULES: VEHICULES_MAPPING_VALUES,
}


def transform_dataframe(file_type: FileType, raw_df: pd.DataFrame) -> pd.DataFrame:
    source_df = raw_df.rename(columns=ALL_MAPPING_COLUMNS[file_type])

    if file_type is FileType.CARACTERISTIQUES:
        source_df['date_accident'] = pd.to_datetime({
            'year': source_df['an'],
            'month': source_df['mois'],
            'day': source_df['jour'],
        }, errors='raise', unit='D', utc=True)
        source_df['date_accident'] = source_df.apply(
            lambda row: row.date_accident.date(), axis=1)
        del source_df['an']
        del source_df['mois']
        del source_df['jour']

    for name, mapping in ALL_MAPPING_VALUES[file_type].items():
        source_df[name] = source_df[name].map(mapping)

    return source_df
