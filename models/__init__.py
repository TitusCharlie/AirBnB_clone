#!/usr/bin/python3
"""
==============
import module
==============
"""

from models.engine.file_storage import FileStorage
import models


"""create a unique FileStorage instance for your application"""

storage = FileStorage()
storage.reload()