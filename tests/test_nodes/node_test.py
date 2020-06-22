from create_node import Node
from unittest import TestCase
import unittest


class TestNode(TestCase):
    def setUp(self):
        self.node = Node('John', 123)

    def tearDown(self):
        del self.node

    def test_check_id_initialization(self):
       self.assertEqual(self.node.personal_id, 123) 

    def test_check_id_is_int(self):
        self.assertEqual(type(self.node.personal_id), type(111))

    def test_check_id_is_a_float(self):
        self.assertNotEqual(type(self.node.personal_id), type(123.))

    def test_assert_error_if_float(self):
        with self.assertRaises(Exception) as context:
            Node('John', 123.)
        self.assertTrue('Incorrect type, please return an int for personal id' in str(context.exception))

    def test_name_initialization(self):
        self.assertEqual(self.node.name, 'John') 

    def test_next_starts_as_none(self):
        self.assertEqual(self.node.next, None) 
    
    
