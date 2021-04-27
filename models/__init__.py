#!/usr/bin/python3
"""This file initiate packages needed
for the programs."""

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
