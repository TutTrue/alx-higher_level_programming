#!/usr/bin/python3
"""class Base"""
import json
import csv
import os


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(list_dictionaries):
        """ returns the list of the JSON string representation json_string"""
        if list_dictionaries is None:
            return []
        return json.loads(list_dictionaries)

    @classmethod
    def create(cls, **dictionary):
        '''
            Returns an instance with all the attributes already set
        '''
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            obj = Rectangle(1, 1)
        elif cls.__name__ == "Square":
            obj = Square(1)
        obj.update(**dictionary)
        return (obj)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        file_name = cls.__name__+'.json'
        with open(file_name, "w",  encoding='UTF-8') as f:
            if list_objs is None:
                json.dump([], f)
                return
            json.dump([json.loads(cls.to_json_string(obj.to_dictionary()))
                      for obj in list_objs], f)

    @classmethod
    def load_from_file(cls):
        """loading dict representing the parameters for
            and instance and from that creating instances"""
        file_name = cls.__name__+'.json'
        try:
            with open(file_name, "r") as f:
                content = cls.from_json_string(f.read())
        except Exception:
            return []
        return list(map(lambda obj: cls.create(**obj), content))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to file csv"""
        mycsv = ""
        flag = -1
        for o in list_objs:
            if o.__class__.__name__ == "Rectangle":
                if flag == -1:
                    mycsv += "id,width,height,x,y\n"
                    flag = 0

                mycsv += f"{o.id},{o.width},{o.height},{o.x},{o.y}\n"

            else:
                if flag == -1:
                    mycsv += "id,size,x,y\n"
                    flag = 0

                mycsv += f"{o.id},{o.size},{o.x},{o.y}\n"

        with open(cls.__name__+".csv", encoding="utf-8", mode="w") as file:
            file.write(mycsv[:-1])

    @classmethod
    def load_from_file_csv(cls):
        """load from file csv"""
        data = []
        with open(cls.__name__+".csv", encoding="utf-8", mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Convert values to integers
                for key in row:
                    row[key] = int(row[key])
                data.append(row)
        return list(map(lambda obj: cls.create(**obj), data))

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw function"""
        pass
