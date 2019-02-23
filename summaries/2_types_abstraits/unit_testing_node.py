from node import Node

if __name__ == '__main__':
    node1 = Node('one')
    node2 = Node('two')
    node3 = Node('three')

    node1.next = node2
    node2.next = node3