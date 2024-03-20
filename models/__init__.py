#!/usr/bin/python3

"""
Key Components:

* **models.engine.file_storage:** responsible for file-based
 data storage mechanisms.
* **FileStorage:** A class providing methods for saving and
 loading data to/from files.
* **storage:** An instance of the `FileStorage` class, used
 to interact with your file-based storage.
* **storage.reload():** A method call on the `FileStorage`
 instance to load existing data from a file.
This implies some form of data persistence across sessions.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()