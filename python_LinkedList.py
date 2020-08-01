class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data, pos =None):
        new_node = Node(data)
        if pos == None or pos == (self.length()+1):
            current_pointer = self.head
            while current_pointer.next != None:
                current_pointer = current_pointer.next
            current_pointer.next = new_node
        else:
            if pos > self.length():
                print("ERROR, index izvan granice, nema toliko elemenata")
                print(f"Poslednja pozicija na koji moze da se ubaci element je pozicija sa indeksom {self.length()+1}")
                return
            else:
                counter = 0 
                curent_node = self.head
                while curent_node.next != None:
                    previous_node = curent_node
                    curent_node = curent_node.next
                    counter+=1
                    if counter == pos:
                        previous_node.next = new_node
                        new_node.next = curent_node
                        return


    def display(self):
        elements= []
        curent_node = self.head
        while curent_node.next != None:
            curent_node = curent_node.next
            elements.append(curent_node.data)
        print (elements)
    
    def length(self):
        total = 0
        cur_pointer = self.head
        while cur_pointer.next != None:
            cur_pointer = cur_pointer.next
            total += 1
        
        return total
    
    def get(self, index):
        a = self.length()
        if index > a:
            print("Ups, ne postoji element sa tim indeksom")
            return None

        counter = 0
        curent_node = self.head
        while curent_node.next != None:
            curent_node = curent_node.next
            counter += 1
            if index == counter:
                print(curent_node.data)
                return curent_node.data
    
    def erase(self, index):
        if index > self.length():
            print("Ups, ne postoji element sa tim indeksom")
            return None
        
        counter = 0 
        curent_node = self.head
        while curent_node.next != None:
            previous_node = curent_node
            curent_node = curent_node.next
            counter += 1
            if counter == index:
                previous_node.next = curent_node.next
                return


#testing
new = LinkedList()

new.append(1)
new.append(2)
new.append(3)
new.append(4)

print(new.length())

new.display()
new.append(10,5)
new.display()

new.get(4)
new.erase(5)

new.display()