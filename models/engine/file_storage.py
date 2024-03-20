#!/usr/bin/python3
"""
FileStorage module: Provides a JSON-based file storage mechanism for your
Python objects.
"""

import json
import sys


class FileStorage:
    """
    A class for handling file storage of objects in JSON format.

    Attributes:
        __file_path (str): The path to the JSON file where objects are stored.
        __objects (dict): An in-memory dictionary to hold the deserialized
        objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieves all objects stored in the file storage.

        Returns:
            dict: A dictionary containing all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the file storage.

        Args:
            obj: The object to be added to the storage. The object's class name
        and id are combined to create a unique key.
        """
        object_key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[object_key] = obj

    def save(self):
        """
        Saves all objects in the `__objects` dictionary
        to the specified JSON file.

        This method performs the following steps:

        1. **Serialization:**  Converts each object in `__objects`
        into a dictionary
        representation using the `to_dict()` method (assumed to be
        implemented in the classes of the objects being stored).

        2. **Store Class Name:** Includes the class name (`__class__`)
        in the serialized
        dictionary to enable proper deserialization later.

        3. **File Writing:** Writes the serialized dictionary to the
        JSON file, providing persistent storage.
        """
        serialized_objects = {}

        for object_key, obj in self.__objects.items():
            serialized_objects[object_key] = obj.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Loads objects from the JSON file and populates the `__objects`
        dictionary.

        This method takes care of the following aspects:

        1. **Safe Class Handling:**
            * Leverages `getattr` and `sys.modules` to dynamically import
             classes by their names from the class definitions present
            in the code.This protects against arbitrary code execution
            risks associated with direct use of `eval`.

        2. **Error Handling:**
            * Gracefully handles missing files (`FileNotFoundError`),
            simply continuing without modifying the storage.
            * Warns the user if an object's class cannot be found
            during deserialization, allowing the loading process to
             ontinue while skipping the affected object.

        3. **Deserialization and Instantiation:**
            * Creates instances of the stored objects using their
            serialized data, ensuring
              the original object state is restored from the storage file.
        """
        try:
            with open(self.__file_path, "r", encoding="UTF8") as file:
                serialized_data = json.load(file)

            for object_key, serialized_obj in serialized_data.items():
                class_name = serialized_obj.get("__class__")
                if class_name and hasattr(sys.modules, class_name):
                    module = sys.modules[class_name]
                    obj_class = getattr(module, class_name)
                    obj_instance = obj_class(**serialized_obj)
                    self.__objects[object_key] = obj_instance
                else:
                    print(f"Warning: Skipping object with key '{object_key}'")
        except FileNotFoundError:
            pass  # Nothing to load if the file doesn't exists