class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def print(self):
        if self.head is None:
            print("Linkedlist is empty")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
        
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def get_length(self):
        cnt = 0
        itr = self.head
        while itr:
            cnt += 1
            itr = itr.next
        return cnt
    
    def remove_at(self, index):
        # case 1: index negative or greater than size of linkedlist
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        # case 2: to remove first element
        if index == 0:
            self.head = self.head.next
            return
        
        # case 3: for specific index 
        cnt = 0
        itr = self.head
        while itr:
            if cnt == index - 1:
                itr.next = itr.next.next 
                break
            itr = itr.next
            cnt += 1
            
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        cnt = 0
        itr = self.head
        while itr:
            if cnt == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            
            itr = itr.next
            cnt += 1
            
    def insert_after_value(self, data_after, data_to_insert):
        # check linkedlist is empty or not
        if self.head is None:
            return
        
        # check head == data_after
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return
        
        # if ll not emply, data_after not head , then do the following
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            
            itr = itr.next
            
            
    def remove_by_value(self, data):
        if self.head is None:
            return 
        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next 
                break
            
            itr = itr.next
            
            
if __name__ == "__main__":
    
    # create linkedlist
    ll = LinkedList()
    
    # insert at begining
    ll.insert_at_begining(5)
    ll.insert_at_begining(10)
    ll.insert_at_begining(13)

    ll.insert_at_end(100)
    ll.insert_at_end(200)
    ll.insert_at_end(10)
    ll.print()
    print(f"Length : {ll.get_length()}")

    ll.insert_at(2, "mixer")
    ll.insert_at(0, "Head")
    ll.insert_at_end("Tail")

    ll.insert_after_value(100, 150)
    ll.insert_after_value(10, 99)
    
    ll.remove_by_value("mixer")
    ##ll.remove_at(2)
    ##ll.insert_values(['banana', 'apple', 'mango', 'grape'])
    # print the linkedlist
    ll.print()
    
    # length of the linkedlist
    print(f"Length : {ll.get_length()}")
        