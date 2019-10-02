class TreiNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.last = False


class Trei(object):

    def __init__(self):
        self.root  = TreiNode()

    def _charToIndex(self, char):
        return ord(char) - ord('a')
    
    def insert(self, word):
        node = self.root
        #print(word)
        #wordLen = len(word)
        for char in word:
            #print(char)
            index = self._charToIndex(char)
            if not node.children[index]:
                node.children[index] = TreiNode()

            node = node.children[index]
        node.last = True

    def iterate(self, r=0):
        if self.root.last:
            print("Yes")
            return True
        elif self.root.children != None:
            self.iterate(self.root.children)

        
def main():
    trei = Trei()
    words = ["hello", "how", "are", "you"]
    for word in words:
        trei.insert(word)
    
    trei.iterate()
    
        
if __name__ == "__main__":
    main()
