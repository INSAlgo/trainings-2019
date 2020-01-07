

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    cpt = 0
    while head.next != None and cpt <= 1000:
        head = head.next
        cpt += 1
    return cpt > 1000
