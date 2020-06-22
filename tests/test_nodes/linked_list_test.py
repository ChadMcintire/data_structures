from ll import LinkedList 
from create_node import Node
from unittest import TestCase
import unittest

#test_node = Node('john', 123)
#print(test_node.name)

class Testll(TestCase):
    def setUp(self):
        self.link = LinkedList()

    def tearDown(self):
        del self.link

    def test_linked_list_starts_empty(self):
        self.assertEqual(self.link.head, None)

    def test_push_one_onto_list_returns_first_push_values(self):
        self.link.push("bueler", 7) 
        self.assertEqual(self.link.head.personal_id, 7)
        self.assertEqual(self.link.head.name, "bueler")

    def test_second_push_return_second_push_values(self):
        self.link.push("bueler", 7) 
        self.link.push("flowrider", 99)
        self.assertEqual(self.link.head.next.personal_id, 99)
        self.assertEqual(self.link.head.next.name, "flowrider")

    def test_third_push_return_third_push_values(self):
        self.link.push("bueler", 7) 
        self.link.push("flowrider", 99)
        self.link.push("chucky", 66)
        self.assertEqual(self.link.head.next.next.personal_id, 66)
        self.assertEqual(self.link.head.next.next.name, "chucky")
    
