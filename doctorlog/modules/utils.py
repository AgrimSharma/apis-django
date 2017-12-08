# coding=utf-8
#
from .description import description
from .location import location
from .trigger import trigger
from .relief import relief
from .other_symptoms import other_symptoms
from .length import length


def check_disease(disease):
    """
    :param disease: disease name patient have choosen
    :return: dict of all data
    """
    return dict(description=description.get(disease,'Not Applicable'),
                location=location.get(disease,'Not Applicable'),
                trigger=trigger.get(disease,'Not Applicable'),
                relief=relief.get(disease,'Not Applicable'),
                other_symptoms=other_symptoms.get(disease,'Not Applicable'),
                length=length.get(disease,'Not Applicable'))