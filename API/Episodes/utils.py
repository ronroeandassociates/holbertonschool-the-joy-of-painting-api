""" Holds useful lists, dicts, and helper functions """
from typing import Dict, List, Union


color_list = ['black_gesso', 'bright_red', 'burnt_umber', 'cadmium_yellow',
              'dark_sienna', 'indian_red', 'indian_yellow', 'liquid_black',
              'liquid_clear', 'midnight_black', 'phthalo_blue',
              'phthalo_green', 'prussian_blue', 'sap_green', 'titanium_white',
              'van_dyke_brown', 'yellow_ochre', 'alizarin_crimson']
subject_list = ['barn', 'beach', 'boat', 'bridge', 'building', 'bushes',
                'cabin', 'cactus', 'cirrus', 'cliff', 'clouds', 'conifer',
                'cumulus', 'deciduous', 'dock', 'farm', 'fence', 'fire',
                'flowers', 'fog', 'grass', 'hills', 'lake', 'lakes',
                'lighthouse', 'mill', 'moon', 'mountain', 'mountains',
                'night', 'ocean', 'palm_trees', 'path', 'person', 'portrait',
                'river', 'rocks', 'snow', 'snowy_mountain', 'structure', 'sun',
                'tree', 'trees', 'waterfall', 'waves', 'windmill', 'winter']
month_list = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]


def add_to_dict(list: List[str]) -> Dict[int, str]:
    """ Adds values from list to dict starting key 1 """
    return {idx + 1: val for idx, val in enumerate(list)}


# Dictionaries to match int key to string value
color_dict = add_to_dict(color_list)
subject_dict = add_to_dict(subject_list)
month_dict = add_to_dict(month_list)


def find_value(dict: Dict[int, str], key: int) -> Union[str, None]:
    """ Returns value based on key in dictionary """
    return dict.get(key, None)
