class Node(object):
  """Node in a linked list."""

  def __init__(self,data):
    self.data = data
    self.next = None

new_node = Node(5)


class LinkedList(object):
    """Linked list class."""

    def __init__(self):
        self.head = None
        self.tail = None


    def print_list(self):
        """Print all items in the linked list."""

        current = self.head

        while current is not None:
            print current.data
            current = current.next

    def find_node(self, data):
        """Is a matching node in the linked list."""

        current = self.head

        while current is not None:
            if current.data == data:
                return True

            current = current.next

        return False

    def add_node(self, data):
        """Add a node with data to end of linked list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node


#Version 1
    def remove_node(self, value):
        """Remove node with a given value."""

        #If the head node has our value, we will make the second item our new head
        if self.head and self.head.data == value:
            self.head = self.head.next
            return

        current = self.head

        while current.next is not None:

            if current.next.data == value:
                current.next = current.next.next
                return

            else:
                current = current.next


#Version 2
    def remove_node(self,value):
        """Remove node with a given value."""

        prev = None
        current = self.head

        while current is not None:

            if current.data == value:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return

            else:
                prev = current
                current = current.next


# Create a method that removes node at a certain index
    def remove_by_index(self, index):
        """Remove node with a given index."""

        current = self.head
        x = 1

        if index == 0:
            self.head = self.head.next
            return

        while x < index:
            current = current.next
            x += 1

        current.next = current.next.next

# Create a method that inserts into list at position given by index
    def insert_by_index(self, index, data):
        """Insert node at position given by index."""

        new_node = Node(data)
        current = self.head
        x = 1

        if index == 0:

            self.head = new_node
            new_node.next = current

        while x < index:
            current = current.next
            x += 1

        next_node = current.next.next
        current.next = new_node
        new_node.next = next_node
