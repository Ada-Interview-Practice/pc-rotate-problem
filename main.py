# DO NOT MODIFY THE NODE CLASS
class Node:
    def __init__(self, value, next=None):
        self.value = value 
        # if next is None, this is the last element in the list
        self.next = next

    def __eq__(self, other):
        '''
        Understanding this function is NOT necessary for solving the problem;
        it is only used for the assertions.
        Feel free to explore your curiosity of how this works after the interview :)
        '''
        try:
            return (type(other) == Node and 
                    self.value == other.value and 
                    self.next == other.next)
        except RecursionError:
            raise Exception("Linked list has a cycle or is too large")

# This is one possible approach. An alternative approach follows.
def rotate(head, k):
    # determine length of list by looping until the end
    length = 1
    current = head
    while current.next:
        current = current.next
        length += 1

    # If the requested rotation is larger than the length of the list,
    # truncate the rotation
    k = k % length
    # If k is a multiple of the length of the list, nothing needs to happen
    # (e.g. doing ten rotations on a 5-element list brings us back to the start)
    if k == 0:
        return head

    # This helper function moves the last element of a list to the front
    def pop_to_front(head):
        # Iterate through the list to find the second-to-last element
        current = head
        while current.next and current.next.next:
            current = current.next

        # The element after the second-to-last is the current tail
        tail = current.next
        # Have the second-to-last point to None, marking it as the new end of the list
        current.next = None
        # Have the old tail point to the old head
        # This makes the old tail the new head
        tail.next = head

        return tail

    # Move the last element to the front k times
    for _ in range(k):
        head = pop_to_front(head)

    return head


# ALTERNATE IMPLEMENTATION
def rotate_alternative(head, k):
    '''
    Our strategy will be to split the list into two parts, and then put the 
    second part in front. E.g. rotate 1->2->3->4->5 by 2 will look like:
    - Split into 1->2->3 and 4->5
    - Swap the first and second list: 4->5 and 1->2->3
    - Recombine: 4->5->1->2->3
    '''

    # determine length of list by looping until the end
    length = 1
    current = head
    while current.next:
        current = current.next
        length += 1

    # The last node we visit is the tail
    tail = current

    # If the requested rotation is larger than the length of the list,
    # truncate the rotation
    k = k % length
    # If k is a multiple of the length of the list, nothing needs to happen
    # (e.g. doing ten rotations on a 5-element list brings us back to the start)
    if k == 0:
        return head

    # Find where the new list will end
    current = head
    for _ in range(length-k-1):
        current = current.next

    # The node after the new end will be the new start
    new_head = current.next
    # Make sure the new end points to None to show it's the end of the list
    current.next = None
    # Stitch the two lists back together
    tail.next = head

    return new_head


# Input list: a->b->c->d->e
# Rotate by 1
# Output list: e->a->b->c->d
list_1 = Node('a', Node('b', Node('c', Node('d', Node('e')))))
expected = Node('e', Node('a', Node('b', Node('c', Node('d')))))
assert rotate(list_1, 1) == expected

# Input list: a->b->c->d->e
# Rotate by 2
# Output list: d->e->a->b->c
list_2 = Node('a', Node('b', Node('c', Node('d', Node('e')))))
expected = Node('d', Node('e', Node('a', Node('b', Node('c')))))
assert rotate(list_2, 2) == expected

# Input list: a->b->c->d->e
# Rotate by 10
# Input list: a->b->c->d->e
list_3 = Node('a', Node('b', Node('c', Node('d', Node('e')))))
expected = Node('a', Node('b', Node('c', Node('d', Node('e')))))
assert rotate(list_3, 10) == expected

# Input list: 55->8->2->99
# Rotate by 6
# Output list: 2->99->55->8
list_4 = Node(55, Node(8, Node(2, Node(99))))
expected = Node(2, Node(99, Node(55, Node(8))))
assert rotate(list_4, 6) == expected

# Input list: 1->2
# Rotate by 5
# Output list: 2->1
list_5 = Node(1, Node(2))
expected = Node(2, Node(1))
assert rotate(list_5, 5) == expected

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
