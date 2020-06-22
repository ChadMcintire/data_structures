class Node:
    def __init__(self, name, personal_id):
        if type(personal_id) != int:
            raise NameError('Incorrect type, please return an int for personal id')
        self.name = name
        self.personal_id = personal_id
        self.next = None
        
        
