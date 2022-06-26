# Functions to help with database managaement.
# Works like an in-game API to the save.db for efficiency, I suppose.
# 26 June 2022


import sqlite3 as sql
from handler import *
from rich import print

def getDB():
    return sql.connect("save.db")

class Character():
    # Base class to retrieve/use character data efficiently.
    def __init__(self, name:str):
        dat = []
        self.name = name
        with getDB() as conn:
            dats = conn.execute("SELECT * FROM chars WHERE name = ?", (self.name,))
            for deet in dats:
                dat.append(deet)
                break
        dat = dat[0]
        self.name = dat[0]
        self.loc = dat[1]
        self.ph = dat[2]
        self.mh = dat[3]
        self.money = dat[4]
        self.age = dat[5]
        self.job = dat[6]

def createDB():
    with getDB() as conn:
        conn.execute("CREATE TABLE chars (name VARCHAR(255), loc VARCHAR(255), ph INT, mh INT, money INT, age INT, job VARCHAR(255))")
        conn.commit()

def createChar(name:str, loc:str):
    try:
        createDB()
    except:
        pass
    try:
        with getDB() as conn:
            cursor = conn.execute("SELECT EXISTS(SELECT name FROM chars WHERE name = ?)", (name,))
            for row in cursor:
                if row[0] == 1: raise CharacterAlreadyExists()
    except CharacterAlreadyExists:
        print("[italic yellow]The character you tried to create has already been created. Please load it from the save![/italic yellow]")
        return "Error"        
    try:
        with getDB() as conn:
            ph = 100
            mh = 100
            money = 0
            age = 0
            job = "not decided yet."
            conn.execute("INSERT INTO chars VALUES (?, ?, ?, ?, ?,?, ?)", (name, loc, ph, mh, money, age, job))
            conn.commit()
        return Success
    except:
        raise GameError("Something went wrong in-game. Please try again (Source: createChar())")

def addMoney(name:str, amt:int):
    try:
        char = Character(name)
        money = char.money + amt
        with getDB() as conn:
            conn.execute("UPDATE chars SET money = ? WHERE name = ?", (money, char.name))
            conn.commit()
        return Success
    except:
        raise GameError("Something went wrong in-game. Please try again (Source: addMoney())")

def subMoney(name:str, amt:int):
    try:
        char = Character(name)
        if char.money > amt:
            money = char.money - amt
        elif amt > char.money:
            money = 0
        with getDB() as conn:
            conn.execute("UPDATE chars SET money = ? WHERE name = ?", (money, char.name))
            conn.commit()
        return Success
    except:
        raise GameError("Something went wrong in-game. Please try again (Source: subMoney())")

def addPH(name:str, amt:int):
    try:
        char = Character(name)
        ph = char.ph + amt
        with getDB() as conn:
            conn.execute("UPDATE chars SET ph = ? WHERE name = ?", (ph, char.name))
            conn.commit()
        return Success
    except:
        raise GameError("Something went wrong in-game. Please try again (Source: addPH())")

def subPH(name:str, amt:int):
    try:
        char = Character(name)
        if char.ph > amt:
            ph = char.ph - amt
        elif amt > char.ph:
            ph = 0
        with getDB() as conn:
            conn.execute("UPDATE chars SET ph = ? WHERE name = ?", (ph, char.name))
            conn.commit()
        return Success
    except:
        raise GameError("Something went wrong in-game. Please try again (Source: subPH())")

def addMH(name:str, amt:int):
    try:
        char = Character(name)
        mh = char.mh + amt
        with getDB() as conn:
            conn.execute("UPDATE chars SET mh = ? WHERE name = ?", (mh, char.name))
            conn.commit()
        return Success
    except:
        raise GameError("Something went wrong in-game. Please try again (Source: addMH())")

def subMH(name:str, amt:int):
    try:
        char = Character(name)
        if char.mh > amt:
            mh = char.mh - amt
        elif amt > char.mh:
            mh = 0
        with getDB() as conn:
            conn.execute("UPDATE chars SET mh = ? WHERE name = ?", (mh, char.name))
            conn.commit()
        return Success
    except:
        raise GameError("Something went wrong in-game. Please try again (Source: subMH())")

def addAge(name:str, amt:int):
    try:
        char = Character(name)
        age = char.age + amt
        with getDB() as conn:
            conn.execute("UPDATE chars SET age = ? WHERE name = ?", (age, char.name))
            conn.commit()
        return Success
    except:
        raise GameError("Something went wrong in-game. Please try again (Source: addAge())")