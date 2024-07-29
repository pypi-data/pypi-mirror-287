
from typing import Any, Callable, Type, Tuple

class Node:
    def __init__(self, data, next = None):
        self.data: Any = data
        self.next: Node = next

class LinkedList:
    def __init__(self, *args: Any) -> None:
        self.head : Node = None

        # Add data if provided a list
        if len(args):
            for arg in args:
                self.append(arg)

    def append(self, data: Any) -> None:
        # Create node
        new_node: Node = Node(data)

        # If there is no head existing already
        if self.isempty:
            self.head = new_node
        else:
            node_to_traverse = self.head
            while node_to_traverse.next:
                node_to_traverse = node_to_traverse.next
            node_to_traverse.next = new_node

    def insert_at_nth(self, n, data: Any) -> None:
        # Create node
        new_node: Node = Node(data)

        # Validate index
        self._validate_index(n)
        
        if self.isempty:
            return
        
        # Traverse n times
        node_to_traverse = self.head
        for i in range(n):
            node_to_traverse = node_to_traverse.next
        
        # Assign next node to new data
        node_to_traverse.next = new_node
        

    def prepend(self, data: Any) -> None:
        # Create node
        new_node: Node = Node(data)

        # If there is no head existing already
        if self.isempty: # or self.head == None
            new_node.next = self.head

        # Assign new node to head
        new_node.next = self.head
        self.head = new_node

    def remove_head(self) -> None:
        
        if self.isempty:
            pass

        self.head = self.head.next

    def remove_nth_node(self, n: int) -> None:

        self._validate_index(n)

        if self.isempty:
            return
        
        node_to_traverse = self.head
        for _ in range(n - 1):
            node_to_traverse = node_to_traverse.next
        
        if self.size == 1:
            self.head = None
        else:
            node_to_traverse.next = node_to_traverse.next.next
    
    def remove_by_val(self, d: Any) -> None:
        
        if self.isempty:
            return
        
        node_to_traverse = self.head

        # Checks head
        if node_to_traverse.data == d:
            self.remove_head()

        # Looks forward from (head + 1) to (tail)
        while node_to_traverse.next:
            if node_to_traverse.next.data == d:

                # Edge case for removing tail
                if node_to_traverse.next == self.tail:
                    node_to_traverse.next = None
                    return
                
                # For all other cases
                else:
                    node_to_traverse.next = node_to_traverse.next.next
            node_to_traverse = node_to_traverse.next

            
      
    def remove_tail(self) -> None:
        self.remove_nth_node(self.size)

    def access_nth(self, n: int) -> Any:

        self._validate_index(n)

        if self.isempty:
            return
        
        node_to_traverse = self.head
        for _ in range(n):
            node_to_traverse = node_to_traverse.next
        
        return node_to_traverse.data
            
    def where(self, data: Any):
        
        if self.isempty:
            return
        
        node_to_traverse: Node = self.head
        cnt: int = 0

        while node_to_traverse.next:
            cnt +=1
            node_to_traverse = node_to_traverse.next
            if node_to_traverse.data == data:
                return cnt
            
        return -1
            
    
    def traverse(self, func: Callable = print) -> None:

        if self.isempty:
            return
        # Create a temporary node to traverse
        node_to_traverse = self.head
        while node_to_traverse.next:
            func(node_to_traverse.data)
            node_to_traverse = node_to_traverse.next
        func(node_to_traverse.data) # Print the last one
    

    # Wrapper to pass self.head as an argument
    def reverse_traverse(self, func: Callable = print):
        
        self.reverse_traverse_util(func, self.head)

    def reverse_traverse_util(self, func: Callable, node: Node) -> None:

        # Base condition: Finish iteration when at tail
        if node == None:
            return
        else:
            # Recurse to the next before going to next line
            self.reverse_traverse_util(func, node.next) 
            # The action
            func(node.data)

    def concatenate(self, ll: Type['LinkedList']) -> Type['LinkedList']:
        
        new_list: Type['LinkedList'] = self

        if ll.isempty:
            pass
        else:
            node_to_traverse: Node = ll.head
            while node_to_traverse.next:
                new_list.append(node_to_traverse.data)
                node_to_traverse = node_to_traverse.next
            new_list.append(node_to_traverse.data)

        return new_list
    
    def split(self, n: int) -> Tuple[Type['LinkedList'], Type['LinkedList']]:

        self._validate_index(n)

        l1 = LinkedList()
        l2 = LinkedList()

        if self.isempty:
            pass
        
        node_to_traverse: Node = self.head
        for _ in range(n + 1):
            l1.append(node_to_traverse.data)
            node_to_traverse = node_to_traverse.next
        for _ in range(n + 1, self.size):
            l2.append(node_to_traverse.data)
            node_to_traverse = node_to_traverse.next
        
        return (l1, l2)

  
    @property
    def size(self) -> int:
        cnt: int = 0
        if self.head == None:
            pass
        else:
            # Create temporary node to traverse
            node_to_traverse = self.head
            while node_to_traverse.next:
                cnt += 1
                node_to_traverse = node_to_traverse.next
            cnt += 1
        return cnt
    
    @property
    def tail(self) -> Node:
        if self.head == None:
            pass
        else:
            # Create temporary node to traverse
            node_to_traverse = self.head
            while node_to_traverse.next:
                node_to_traverse = node_to_traverse.next
        return node_to_traverse
    
    @property 
    def isempty(self) -> bool:
        return self.size == 0
    
    # Private
    def _validate_index(self, n: int):
        if n > self.size:
            raise IndexError("Selected too large of n value")
        
    
    

    
    


        



