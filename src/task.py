class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_phrase = False
        self.phrase = None 

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, phrase):
        node = self.root
        for char in phrase:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_phrase = True
        node.phrase = phrase  

    def search_in_text(self, text):
        results = {}
        for i in range(len(text)):
            node = self.root
            j = i
            while j < len(text) and text[j] in node.children:
                node = node.children[text[j]]
                if node.is_end_of_phrase:
                    if node.phrase not in results:
                        results[node.phrase] = []
                    results[node.phrase].append(i)
                j += 1
        return results

def build_trie(patterns):
    trie = Trie()
    for pattern in patterns:
        trie.insert(pattern)
    return trie
