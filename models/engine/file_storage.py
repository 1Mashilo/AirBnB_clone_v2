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

    def all(self, cls=None):
        """
        Retrieves all objects stored in the file storage, optionally filtered
        by class.

        Args:
            cls (class, optional): The class of objects to retrieve.
                If None, all objects are returned. Defaults to None.

        Returns:
            list: A list of objects of the specified class or all objects if
            cls
            is None.
        """
        if cls is not None and not issubclass(cls, object):
            raise TypeError("cls must be a class")
        return [obj for obj in self.__objects.values() if isinstance(obj, cls)]

    def delete(self, obj=None):
        """
        Deletes an object from the file storage, if provided.

        Args:
            obj (object, optional): The object to be deleted. If None,
                no deletion occurs. Defaults to None.
        """
        if obj is None:
            return
        key = '{}.{}'.format(type(obj).__name__, obj.id)
        if key in self.__objects:
            del self.__objects[key]
            self.save()
        else:
            print(f"Object with key '{key}' not found in storage.")

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
        into a dictionary representation using the `to_dict()` method
        (assumed to be implemented in the classes of the objects being stored).

        2. **Store Class Name:** Includes the class name (`__class__`)
        in the serialized dictionary to enable proper deserialization later.

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
              in the code. This protects against arbitrary code execution
              risks associated with direct use of `eval`.

        2. **Error Handling:**
            * Gracefully handles missing files (`FileNotFoundError`),
              simply continuing without modifying the storage.
            * Warns the user if an object's class cannot be found
              during deserialization, allowing the loading process to
              continue while skipping the affected object.

        3. **Deserialization and Instantiation:**
            * Creates instances of the stored objects using their
              serialized data, ensuring the original object state is
              restored from the storage file.
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
            pass