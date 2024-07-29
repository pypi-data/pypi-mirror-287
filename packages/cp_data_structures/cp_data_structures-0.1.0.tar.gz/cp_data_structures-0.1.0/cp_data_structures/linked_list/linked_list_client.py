from .linked_list import LinkedList

def print_wrapper(txt: str) -> None:
    print(txt)
    return print

    
if __name__ == "__main__":

    ll = LinkedList("HEAD")

    # Appending
    ll.append(24)
    ll.append("Christian")

    # Print ll
    print("ll:")
    ll.traverse()

    # Print Size
    print(f"size of ll: {ll.size}")

    # Prepending
    l2 = LinkedList()
    print(f"size of l2: {l2.size}")
    l2.prepend("scdklscds")
    l2.prepend("This is prepended")
    
    # Print l2
    print("l2:")
    l2.traverse()
    # l2.traverse(print_wrapper("l2:"))
    
    # Prepend to existing list and get tail
    ll.prepend("My age is")
    ll.traverse(print_wrapper("ll:"))
    print(f"Tail's data of ll is {ll.tail.data}")
    print(f"size of ll: {ll.size}")

    # Get Size and Check If Empty
    l3 = LinkedList()
    print(f"size of l3: {l3.size}")
    print(f"is l3 empty?: {l3.isempty}")

    # Insert at Nth
    ll.insert_at_nth(2, "This is a random insertion")
    ll.traverse(print_wrapper("ll"))
    print(f"size of ll: {ll.size}")
    print(f"index 3 of ll is: {ll.access_nth(3)}")

    # Search
    print(ll.where("Christian"))

    # Reverse Traverse
    ll.reverse_traverse(print_wrapper("ll:"))
    print("\n")

    # Concatenate
    l4 = ll.concatenate(l2)
    l4.traverse(print_wrapper("l4:"))

    # Splitting
    l5, l6 = l4.split(3)
    l5.traverse()
    print("\nl6:")
    l6.traverse()

    # Remove Head and Tail
    l2.remove_head()
    l2.traverse(print_wrapper("l2:"))
    l2.remove_tail()
    l2.traverse(print_wrapper("l2:"))

    # Remove Nth Node
    l4.traverse(print_wrapper("l4:"))
    l4.remove_nth_node(3)
    l4.traverse(print_wrapper("l4:"))

    # Remove Search
    l4.remove_by_val("Christian")
    l4.remove_by_val("My age is")
    l4.remove_by_val("scdklscds")
    l4.traverse(print_wrapper("l4:"))

    # Linked Lists in Loops
    for i in range(l5.size):
        print(l5.access_nth(i), end=", ")

    # Initialize a List from Constructor
    print("\n")
    l7 = LinkedList("Hello", "My favorite number is", 5, True)
    l7.traverse()
    print(l7.head.data)

    # Traversal using custom function
    print(l7.traverse(lambda x: print(str(x).upper()) if isinstance(x, str) else print(x)))    
    






# def print_wrapper(ll: LinkedList, txt: str) -> None:
#     print(str)
#     ll.traverse()





