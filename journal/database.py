"""
Class for work with sqlite database.
Does all CRUD operations.
And gets entire table out of db.
Should be used using with statment.
"""
import sqlite3
from typing import List, Tuple
from datetime import datetime


class DB:
    """
    Class for work with sqlite database journal.db
    """
    
    def __init__(self, database_name: str = 'journal.db') -> None:
        """
        Every instance of this class will create a connection to db and create/open table in it.
        """
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS entry(id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, text TEXT, alarm BLOB)")
        connection.commit()
        self.connection = connection
        self.cursor = cursor
    
    def add_entry(self, text: str, date: str = f"{datetime.today()}", alarm: bool = False) -> None:
        """Addes new entry to the table.
        Args:
            text (str): Text of the entry
            date (str, optional): Adds date of the entry. Defaults to datetime.today()
            alarm (bool, optional): If entry has alarm function to trigger alarm sound on time of entry being equal to now. Defaults to False.
        """
        self.cursor.execute("INSERT INTO entry (date, text, alarm) VALUES (?, ?, ?)", (date, text, alarm))
        self.connection.commit()
    
    def update_entry(self, id: int, text: str, date: str = f"{datetime.today}", alarm: bool = False) -> None:
        """Updates an existing entry in the table.
        Args:
            id (int): ID of the entry to be updated.
            text (str): New text of the entry.
            date (str, optional): New date of the entry. Defaults to datetime.today().
            alarm (bool, optional): If the entry has an alarm function to trigger alarm sound on time of entry being equal to now. Defaults to False.
        """
        self.cursor.execute("UPDATE entry SET date=?, text=?, alarm=? WHERE id=?", (date, text, alarm, id))
        self.connection.commit()
    
    def remove_entry(self, id: int) -> None:
        """Removes an entry from the table.
        Args:
            id (int): ID of the entry to be removed.
        """
        self.cursor.execute("DELETE FROM entry WHERE id=?", (id,))
        self.connection.commit()
    
    def get_entry(self, id: int) -> Tuple[int, str, str, bool]:
        """Retrieves an entry from the table by its ID.
        Args:
            id (int): ID of the entry to be retrieved.
        Returns:
            Tuple[int, str, str, bool]: A tuple containing the ID, date, text, and alarm of the entry.
        """
        self.cursor.execute("SELECT * FROM entry WHERE id=?", (id,))
        return self.cursor.fetchone()
    
    def get_all(self) -> List[Tuple[int, str, str, bool]]:
        """Retrieves all entries from the table.
        Returns:
            List[Tuple[int, str, str, bool]]: A list of tuples containing the ID, date, text, and alarm of each entry.
        """
        self.cursor.execute("SELECT * FROM entry")
        return self.cursor.fetchall()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()
