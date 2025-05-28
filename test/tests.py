import unittest
from src.task import Trie, build_trie

class TestTrie(unittest.TestCase):

    def setUp(self):
        patterns = ["apple", "app", "apply", "apt"]
        self.trie = build_trie(patterns)
    
    def test_insert_and_search(self):
        self.assertTrue(self.trie.search("apple"))
        self.assertTrue(self.trie.search("app"))
        self.assertFalse(self.trie.search("apples"))
    
    def test_starts_with(self):
        self.assertTrue(self.trie.starts_with("ap"))
        self.assertTrue(self.trie.starts_with("app"))
        self.assertFalse(self.trie.starts_with("banana"))
    
    def test_empty_string(self):
        self.trie.insert("")
        self.assertTrue(self.trie.search(""))


