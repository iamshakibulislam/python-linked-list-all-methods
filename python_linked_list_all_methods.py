
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
    

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        
        
    
    def append(self,item):
        
        curr = self.head
        newNode = Node(item)
        if curr == None:
            
            self.head = newNode
            self.length = self.length + 1
            
        else:
            
            while(curr.next != None):
                curr = curr.next
                
            curr.next = newNode
            self.length = self.length + 1
            
    
    def traverse(self):
        traverse_list = []
        all_nodes = self.head
        while(all_nodes != None):
            traverse_list.append(all_nodes.value)
            all_nodes = all_nodes.next
            
        return traverse_list
        
    
    def insert(self,index,item):
        if index == 0:
            temp = self.head
            newNode = Node(item)
            
            self.head = newNode
            
            self.head.next = temp
            
            self.length = self.length + 1
        else:
            counter = 0
            all_nodes = self.head
            temp = None
            
            while(counter < int(index)-1):
                all_nodes = all_nodes.next
                counter = counter+1
                
            temp = all_nodes.next
            
            all_nodes.next = Node(item)
        
            all_nodes.next.next = temp
            
            self.length = self.length + 1
            
    
    
    def delete(self,index):
        
        curr = self.head
        temp = None
        
        if index == 0:
            temp = curr.next
            self.head = temp
            
            self.length = self.length - 1
            return 'deleted at beggining'
        
        counter = 1
        
        while(counter < int(index)):
            curr = curr.next
            counter = counter + 1
        
        temp = curr.next.next
        
        curr.next = temp
        
        self.length = self.length - 1
        
        return 'deleted'
        
        
    def reverse(self):
        if self.head == None:
            return None
        
        if self.length == 1:
            return self.head.value
        curr_list = self.head
        new_list = None
        temp = None
        
        while(curr_list != None):
            temp = curr_list.next
            curr_list.next  = new_list
            new_list = curr_list
            curr_list = temp
        
        self.head = new_list 
 
 
 