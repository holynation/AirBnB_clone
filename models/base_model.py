#!/usr/bin/python3
"""
Module BaseModel
This is the parent class for all models
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """The Base class for the Airbnb console
    Methods:
        __init__(self)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize instance attributes id, created_at, updated_at
        """
        if kwargs:
            for key, val in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(kwargs['created_at'],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return the string represention of the model object
        """
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        """
        Returns the string representation of the model object
        """
        return (self.__str__())

    def save(self):
        """
        Update the instance attribute updated_at with updated time
        and save to serialized file
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dic = {}  # create an empty dict
        dic["__class__"] = self.__class__.__name__
        for k, val in self.__dict__.items():
            if isinstance(val, datetime):  # if pair is of datetime instance
                dic[k] = val.isoformat()  # or strftime(%Y-%m-%dT%H:%M:%S.%f)
            else:
                dic[k] = val
        return dic
