#!/usr/bin/python3
import json
import models
"""
Contains the FileStorage Class
"""


class FileStorage:
    """
    FileStorage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ displays dictionary of objects """
        return type(self).__objects

    def new(self, obj):
        """ Formats object into key value pair and adds to __objects """
        k = "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[k] = obj

    def save(self):
        """ Serialized objects into __file_path """
        save_dict = {}
        for k, v in type(self).__objects.items():
            save_dict[k] = v.to_dict()
        with open(type(self).__file_path, mode='w', encoding='utf-8') as f:
            json.dump(save_dict, f)

    def reload(self):
        """ Deserialized json into python objects if file is found """
        try:
            with open("file.json", "r", encoding="utf-8") as f:
                obj = json.load(f)
                for k, v in obj.items():
                    val = models.classes[v["__class__"]](**v)
                    type(self).__objects[k] = val
        except FileNotFoundError:
            pass
