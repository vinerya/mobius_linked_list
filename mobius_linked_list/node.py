class MobiusNode:
    def __init__(self, data, orientation=0):
        self.data = data
        self.orientation = orientation  # 0 or 1
        self.next = None

    def __repr__(self):
        return f"MobiusNode(data={self.data}, orientation={self.orientation})"
