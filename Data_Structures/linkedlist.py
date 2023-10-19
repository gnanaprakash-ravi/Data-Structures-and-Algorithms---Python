class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        
        iterator.next = Node(data, None)
    
    def print(self):
        if self.head is None:
            print("LL is empty")
            return
        
        iterator = self.head
        llstring = ""
        while iterator:
            llstring += str(iterator.data) + ' '
            iterator = iterator.next
        
        print(llstring)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        iterator =self.head
        while iterator:
            count+=1
            iterator = iterator.next

        return count

    def remove_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception ("Invalid Index")
        if index ==0:
            self.head = self.head.next
            return

        count = 0
        iterator = self.head
        while iterator:
            if count ==index -1:
                iterator.next = iterator.next.next
                break

            iterator = iterator.next
            count +=1
    
    def insert_at(self, index, data):
        if index<0 or index > self.get_length():
            raise Exception ("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        iterator = self.head
        while iterator:
            if count == index - 1:
                node = Node(data, iterator.next)
                iterator.next = node
                break

            iterator = iterator.next
            count+=1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return
        iterator = self.head # same as we did in head node, same code also
        while iterator:
            if iterator.data == data_after:
                iterator.next = Node(data_to_insert, iterator.next)
                break
            iterator = iterator.next
    
    def remove_by_value(self, data):
        if self.head is None:
            return
        iterator = self.head
        while iterator.next:
            if iterator.next.data ==data:
                iterator.next = iterator.next.next
                break                
            iterator = iterator.next

    def reverse_link(self):
        prev = None
        iterator = self.head
        while iterator:
            temp = iterator
            iterator = iterator.next
            temp.next = prev
            prev = temp
        self.head = prev
        return self.head

    def sort_link(self):
    #we cannot quick sort, cannot jump in ll
        N = 0
        iterator = self.head
        while iterator:
            N +=1
            iterator = iterator.next
        i = 0
        while i < N:
            j = 0
            iterator = self.head
            while j< N-i and iterator.next:
                if iterator.data > iterator.next.data:
                    iterator.data, iterator.next.data = iterator.next.data, iterator.data
                iterator = iterator.next    
                j+=1
            i+=1
        return self.head
    
def detectloop(head):
    fast=head
    slow=head
    loopexist=0
    while(fast!=None and slow!=None and fast.next!=None):
        fast=fast.next.next
        slow=slow.next
        if(fast==slow):
            loopexist=1
            break

    if(loopexist):
        slow=head
        while(slow!=fast):
            slow=slow.next
            fast=fast.next
        return slow
    return None

# ll =LinkedList()
# ll.insert_values([45,5,67,78,7,45])
# ll.insert_at_end(34)
# ll.print()
# ll.insert_values([8, 58, 254, 45, 458, 85, 644])
# ll.print()
# ll.insert_after_value(85, 23)
# ll.print()
# ll.remove_by_value(85)
# ll.print()
# ll.insert_at(4, 22)
# ll.print()
# ll.remove_at(5)
# ll.print()
# ll.reverse_link()
# ll.print()
# ll.sort_link()
# ll.print()

head  = Node('a', None)
nodeB = Node('b', None)
nodeC = Node('c', None)
nodeD = Node('d', None)
nodeE = Node('e', None)
nodeF = Node('f', None)
nodeG = Node('g', None)
nodeH = Node('h', None)
nodeI = Node('i', None)
nodeJ = Node('j', None)

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF
nodeF.next = nodeG
nodeG.next = nodeH
nodeH.next = nodeI
nodeI.next = nodeJ
nodeJ.next = nodeD

head = detectloop(head)
print(head.data)
