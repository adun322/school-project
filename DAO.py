import sqlite3 as SQLite
from sqlite3 import Connection, Cursor
from typing import Any as Unit


class DAO:
    def __init__(self, path: str):
        self.__path: str = path
        self.__ensureCreated()

    def addWord(self, word: str, translation: str, mType: str) -> Unit:  
        connection: Connection = SQLite.connect(self.__path)
        cursor: Cursor = connection.cursor()
        cursor.execute(f"INSERT INTO common VALUES (NULL, \"{word}\", \"{translation}\", \"{mType}\");")
        connection.commit()
        connection.close()

    def __ensureCreated(self) -> Unit:
        connection: Connection = SQLite.connect(self.__path)
        cursor: Cursor = connection.cursor()
        cursor.execute("""
CREATE TABLE IF NOT EXISTS "common" (
    "id" INTEGER UNIQUE, 
    "word" TEXT, 
    "translation" TEXT, 
    "type" TEXT,
    PRIMARY KEY("id" AUTOINCREMENT)
);""".strip())
        cursor.execute("""
CREATE TABLE IF NOT EXISTS "learned" (
    "id" INTEGER UNIQUE, 
    "userid" INTEGER, 
    "word" TEXT, 
    "translation" TEXT,
    PRIMARY KEY("id" AUTOINCREMENT)
);""".strip())
        cursor.execute("""
CREATE TABLE IF NOT EXISTS "new" ( 
    "id" INTEGER UNIQUE, 
    "userid" INTEGER, 
    "word" TEXT, 
    "translation" TEXT,
    PRIMARY KEY("id" AUTOINCREMENT)
);""".strip())
        cursor.execute("""
CREATE TABLE IF NOT EXISTS "users" ( 
    "id" INTEGER UNIQUE, 
    "username" TEXT, 
    "rights" INTEGER, 
    "score" INTEGER, 
    "activity" INTEGER,
    PRIMARY KEY("id" AUTOINCREMENT)
);""".strip())
        connection.commit()
        connection.close()
