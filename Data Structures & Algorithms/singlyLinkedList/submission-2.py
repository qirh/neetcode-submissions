class LinkedList:
    
    def __init__(self):
        self.data = []

    
    def get(self, index: int) -> int:
        if index < 0 or index >= len(self.data):
            return -1
        return self.data[index]
        

    def insertHead(self, val: int) -> None:
        self.data.insert(0, val)
        

    def insertTail(self, val: int) -> None:
        self.data.append(val)

    def remove(self, index: int) -> bool:
        if index < 0 or index >= len(self.data):
            return False
        del self.data[index]
        return True

    def getValues(self) -> List[int]:
        return self.data
