class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = node()
        
    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
        
    def lenght(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print("------Original list------")
        print(elems)
        print("------Reversed List------")
        elems.reverse()
        print(elems)
        print("==========================")
    
    def convert_to_int(self):
        digits = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            digits.append(cur_node.data)
        digits.reverse()
        number = int("".join(map(str, digits)))
        # print(number)
        return number

def convert_to_list2(number):
    digits = [int(d) for d in str(number)]
    digits.reverse()
    print(digits)


#Case 1
list1 = LinkedList()
list1.append(2)
list1.append(4)
list1.append(3)

list2 = LinkedList()
list2.append(5)
list2.append(6)
list2.append(4)

#Case 2
list3 = LinkedList()
list3.append(0)
list4 = LinkedList()
list4.append(0)

#Case 3
list5 = LinkedList()
list5.append(9)
list5.append(9)
list5.append(9)
list5.append(9)
list5.append(9)
list5.append(9)
list5.append(9)
list6 = LinkedList()
list6.append(9)
list6.append(9)
list6.append(9)
list6.append(9)

total = list5.convert_to_int() + list6.convert_to_int()
print("------Sum of two numbers------")
print(total)
print("-------Convert to list--------")
convert_to_list2(total)