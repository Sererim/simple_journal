from journal.database import DB
from typing import List, Tuple

def test_Remove_Entry() -> None:
    """
    Tests remove and add entry methods of DB class.
    """
    with DB(database_name='test_db1.db') as db:
        db.add_entry(text=" ")
        db.remove_entry(id=1)
        result = db.get_all()
    print(result)
    assert len(result) == 0

def test_Add_Entry() -> None:
    """
    Tests add and remove entry methods of DB class.
    """
    with DB(database_name='test_db2.db') as db:
        db.add_entry(
            text="Hello, World!"
        )
        result = db.get_entry(id=1)
        db.remove_entry(id=1)   
    print(result) 
    assert(result[0]) == 1
    assert(result[2]) == "Hello, World!"
    assert(result[3]) == False

def test_Update_Entry() -> None:
    """
    Tests update entry method of DB class.
    """
    with DB(database_name='test_db3.db') as db:
        db.add_entry(
            text="Hello, World!"
        )
        db.update_entry(
            id=1,
            text="Are you siwulus right mewyo?"
        )
        result = db.get_entry(id=1)
        db.remove_entry(id=1)   
    print(result) 
    assert(result[0]) == 1
    assert(result[2]) != "Hello, World!"
    assert(result[2]) == "Are you siwulus right mewyo?"
    assert(result[3]) == False

def test_Get_All() -> None:
    """
    Tests get all method of DB class.
    """
    with DB('test_db4.db') as db:
        db.add_entry(text="Hello")
        db.add_entry(text="ALRAM", alarm=True)
        result = db.get_all()
        db.remove_entry(id=2)
        db.remove_entry(id=1)
    print(result)
    assert(len(result)) == 2
