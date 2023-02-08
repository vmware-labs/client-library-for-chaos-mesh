import json


class Selector:

    def __init__(self, label_selector: dict):
        self.label_selector = label_selector

    def get(self):
        return self.label_selector


def label_dictionary_to_label_selector(label_dict):
    """
    Convert the label dictionary to key=value pair

    dict: {'app': 'postgres', 'kapp': '1234'}
    returns: 'app=postgres,kapp=1234'

    :param label_dict: 
    :return: 
    """
    if len(label_dict) == 0:
        raise ValueError("The length of label dict can not be 0")

    return json.dumps(label_dict)
