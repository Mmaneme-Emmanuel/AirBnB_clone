#!/usr/bin/python3
"""class Basemodel"""
from datetime import datetime
from uuid import uuid4
import models
import storage

class BaseModel:
    def __init__(self, *args, **kwargs):
        if (**kwargs):
            for key, value in kwargs.items():
                if key !=  '__class__':
                    if key == 'created_at'or key == 'updated_at':
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
             iself.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
		obj_dict['created_at'] = self.created_at.isoformat()
		obj_dict['updated_at'] = self.updated_at.isoformat()
        trptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                            setattr(self, key, value)eturn obj_dict