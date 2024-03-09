#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Add a call to the method new(self) on storage"""
        if kwargs:
            del kwargs['__class__']
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
            super().__init__(*args, **kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Call save() method of storage"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        obj_dict = {
            'my_number': self.my_number,
            'name': self.name,
            '__class__': self.__class__.__name__,
            'updated_at': self.updated_at.isoformat(),
            'id': self.id,
            'created_at': self.created_at.isoformat()
        }
        return obj_dict

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"