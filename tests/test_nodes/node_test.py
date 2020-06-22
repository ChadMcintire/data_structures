from create_node import Node
from unittest import TestCase
import unittest


class TestNode(TestCase):
    def setUp(self):
        self.node = Node('John', 123)
    def test_check_id_initialization(self):
       self.assertEqual(self.node.personal_id, 123) 
    def test_check_id_is_int(self):
        self.assertEqual(type(self.node.personal_id), type(111))
    def test_check_id_is_a_float(self):
        self.assertNotEqual(type(self.node.personal_id), type(123.))
    def test_name_initialization(self):
       self.assertEqual(self.node.name, 'John') 
        
