from linked_list import __version__


def test_version():
    assert __version__ == '0.1.0'

from linked_list import LinkedList, Node
import pytest

def test_import():
    """ proof of life test passes"""
    assert LinkedList
    assert Node

# add a node to the end of the linked list -- passes
def test_append ():
    node = Node(0)
    link = LinkedList(node)
    link.insert(4)
    link.append(10)
    actual = str(link)
    expected = f'{{ 4 }} -> {{ 0 }} -> {{ 10 }} -> NULL'
    assert actual == expected
    
# insert a node before a node located in the middle of a linked list -- passed
def test_before ():
    node = Node(0)
    link = LinkedList(node)
    link.insert(4)
    link.append(10)
    link.insert_before(0,5)
    actual = str(link)
    expected = f'{{ 4 }} -> {{ 5 }} -> {{ 0 }} -> {{ 10 }} -> NULL'
    assert actual == expected
    
    
    
# add multiple nodes to the end of a linked list
# insert a node before the first node of a linked list
# insert after a node in the middle of the linked list
# insert a node after the last node of the linked list



###### Fixture for CC05 and CC06  ##########    
@pytest.fixture
def generate_new_list():
    node = Node(0)
    new_list = LinkedList(node)
    list_length = 0
    
    for value in range(1,5):
        new_list.insert(value)
        list_length += 1
    
    return new_list
