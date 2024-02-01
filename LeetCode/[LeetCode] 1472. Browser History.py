class Node() :
    def __init__(self, value=0, next=None, prev=None) :
        self.value = value
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = self.tail = new_node = Node(homepage)

    def visit(self, url: str) -> None:
        new_node = Node(value=url)
        if self.head == None :
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def back(self, steps: int) -> str:
        for _ in range(steps) :
            if self.tail.prev :
                self.tail = self.tail.prev
        return self.tail.value

    def forward(self, steps: int) -> str:
        for _ in range(steps) :
            if self.tail.next :
                self.tail = self.tail.next
        return self.tail.value