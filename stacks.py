class Stack:
    def __init__(self):
        '''Initializing attributes of Stack class'''
        self.mystack = []
        
    def stack_len(self):
        '''This method prints out the number of items in the stack'''
        print('This stack contains {} items'.format(len(self.mystack)))

    def stack_status(self):
        '''This checks if the stack is empty is not'''
        if not self.mystack:
            print('Your stack is empty')
        else:
            print('Your stack is not empty')

    def add_items(self,item):
        '''Adds items in the stack.

        args:
        item - This arguement inputs an item to be added to the list.
        '''
        self.mystack.append(item)
        return self.mystack
        
    def remove_item(self):
        '''Removing the top most item and printing out the stack thereafter.'''
        try:
            self.mystack.pop()
        except Exception:
            print('Your Stack is empty so there is nothing to remove')
        else:
            print(self.mystack)

    def peek(self):
        '''Prints out the item at the top of the stack.'''
        try:
            top_item = (self.mystack[-1])
        except Exception:
            print('Your Stack is empty so there is nothing to peek')
        else:
            print('The item at the top of the stack is {}'.format(top_item))
    

        

    


    

    '''Create a stack
    Check if the stack is empty or not, boolean
    Check length of stack
    Adding an item to the stack
    Remove, pop item at the top only if the stack is not empty
    Peeking at the stack
    Push an item at the top of the stack
    '''

