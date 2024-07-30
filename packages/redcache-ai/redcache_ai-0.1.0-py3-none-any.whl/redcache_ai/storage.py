"""
Storage Backend: this storage is the default storage backend
SQLite storage is an alternative storage backend 

""" 

import json
import sqlite3
import numpy as np
from abc import ABC, abstractmethod

class StorageBackend(ABC):
    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def load(self):
        pass

class DiskStorage(StorageBackend):
    def __init__(self, file_path='redcache_data.json'):
        self.file_path = file_path

    def save(self, data):
        with open(self.file_path, 'w') as f:
            json.dump(data, f, default=lambda x: x.tolist() if isinstance(x, np.ndarray) else x)

    def load(self):
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

class SQLiteStorage(StorageBackend):
    def __init__(self, db_path='redcache.db'):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS memories
            (user_id TEXT, memory_id TEXT, data TEXT,
             PRIMARY KEY (user_id, memory_id))
        ''')
        self.conn.commit()

    def save(self, data):
        cursor = self.conn.cursor()
        for user_id, user_memories in data.items():
            for memory_id, memory_data in user_memories.items():
                cursor.execute('''
                    INSERT OR REPLACE INTO memories (user_id, memory_id, data)
                    VALUES (?, ?, ?)
                ''', (user_id, memory_id, json.dumps(memory_data)))
        self.conn.commit()

    def load(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT user_id, memory_id, data FROM memories')
        data = {}
        for row in cursor.fetchall():
            user_id, memory_id, memory_data = row
            if user_id not in data:
                data[user_id] = {}
            data[user_id][memory_id] = json.loads(memory_data)
        return data