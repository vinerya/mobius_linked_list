from .node import MobiusNode

class MobiusLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = MobiusNode(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head  # Point to itself to form a loop
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            # Flip orientation for the new node
            new_node.orientation = 1 - current.orientation
            current.next = new_node
            new_node.next = self.head

    def traverse(self, cycles=1):
        if not self.head:
            return

        current = self.head
        length = self.length()
        orientation = current.orientation

        for cycle in range(cycles):
            print(f"--- Cycle {cycle + 1} ---")
            for _ in range(length):
                # Process current node
                print(f"Data: {current.data}, Orientation: {orientation}")
                current = current.next
            # Invert orientation after each full cycle
            orientation = 1 - orientation

    def length(self):
        if not self.head:
            return 0
        count = 1
        current = self.head
        while current.next != self.head:
            count += 1
            current = current.next
        return count

    def __repr__(self):
        nodes = []
        current = self.head
        if not current:
            return "MobiusLinkedList([])"
        while True:
            nodes.append(f"{current.data}({current.orientation})")
            current = current.next
            if current == self.head:
                break
        return "MobiusLinkedList([" + " -> ".join(nodes) + "])"
