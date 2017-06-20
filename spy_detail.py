#here we are importing our date and time file
from datetime import datetime

#here we are creating a class of name Spy to avoid messyness in our program.
class Spy:

#this is the correct way to make a function in a class.
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


spy = Spy('Gaurav', 'Mr.', 20, 4.0)

friend1 = Spy('Apoorav', 'Mr.', 20,4.6)
friend2 = Spy('Sameer', 'Mr.', 21,4.76)
friend3 = Spy('Kanak', 'Ms.', 26,4.98)


friends = [friend1, friend2, friend3]

#Another class with name chat_message
class chat_message:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me




