class Deque:
    
    def __init__(self):
        self.data = []


    def isEmpty(self) -> bool:
        return len(self.data) == 0
        

    def append(self, value: int) -> None:
        self.data.append(value)
        

    def appendleft(self, value: int) -> None:
        self.data.insert(0, value)
        

    def pop(self) -> int:
        if len(self.data) == 0:
            return -1
        return self.data.pop()
        
    def popleft(self) -> int:
        if len(self.data) == 0:
            return -1
        return self.data.pop(0)
        
