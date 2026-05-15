class LinkedList:
    
    def __init__(self):
        self.data = []
    
    def get(self, index: int) -> int:
        if len(self.data) > index:
            return self.data[index].value
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        if self.data != []:
            new_node.next = self.data[0]
        self.data.insert(0, new_node)

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if self.data != []:
            self.data[-1].next = new_node
        self.data.append(new_node)

    def remove(self, index: int) -> bool:
        lengthy = len(self.data) - 1
        if len(self.data) > index:
            match(index):
                case 0:
                    self.data.pop(index)
                case _ if index == lengthy:
                    self.data.pop(index)
                    if self.data:
                        self.data[-1].next = None
                case _:
                    self.data[index-1].next = self.data[index+1]
                    self.data.pop(index)
            return True;
        return False;


    def getValues(self) -> List[int]:
        return [x.value for x in self.data]
        
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None