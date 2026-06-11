#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

#
# Complete the 'reverseList' function below.
#
# The function is expected to return a SinglyLinkedListNode.
# The function accepts SinglyLinkedListNode head as parameter.
#

def reverseList(head):
    # Write your code here
    pass


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ll = SinglyLinkedList()
    for _ in range(n):
        ll.insert_node(int(input().strip()))

    result = reverseList(ll.head)

    while result:
        fptr.write(str(result.data) + '\n')
        result = result.next

    fptr.close()