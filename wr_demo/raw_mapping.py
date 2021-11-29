# -*- coding: utf-8 -*-
from enum import Enum
from pathlib import Path

import pandas as pd

WR_DEMO_DIR = Path(__file__).parent.parent
RAW_DIR = WR_DEMO_DIR / 'raw'
SRC_DIR = WR_DEMO_DIR / 'source'
BUCKET_NAME = 'wescale-pandas-demo'


class FileType(Enum):
    USAGERS = 'usagers'
    VEHICULES = 'vehicules'


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

ALL_MAPPING_COLUMNS = {
    FileType.USAGERS: USAGERS_MAPPING_COLUMNS,
    FileType.VEHICULES: VEHICULES_MAPPING_COLUMNS,
}

ALL_MAPPING_VALUES = {
    FileType.USAGERS: USAGERS_MAPPING_VALUES,
    FileType.VEHICULES: VEHICULES_MAPPING_VALUES,
}


def transform_dataframe(file_type: FileType, raw_df: pd.DataFrame) -> pd.DataFrame:
    source_df = raw_df.rename(columns=ALL_MAPPING_COLUMNS[file_type])

    for name, mapping in ALL_MAPPING_VALUES[file_type].items():
        source_df[name] = source_df[name].map(mapping)

    return source_df
