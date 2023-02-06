class Selector:

    def __init__(self, label_selector: dict):
        self.label_selector = label_selector

    def get(self):
        return label_dictionary_to_label_selector(self.label_selector)


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

    label_selector = ""

    for key in label_dict:
        label_selector += "{}={},".format(key, label_dict[key])

    return label_selector[:-1]
