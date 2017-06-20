#we are going to import some additional files from pre built files.
from spy_detail import spy, Spy, chat_message, friends
from steganography.steganography import Steganography
from termcolor import *
import colorama
colorama.init()

#Let me define some status.
STATUS_MESSAGES = ['Hey dude!, What\'s up', 'Gaurav , Gaurav Garkoti', 'Welcome to the creed', 'Always MATOKA']

#Lets go now we are supose to print a normal string.

cprint("Hello! Let\'s get started",'red')
#print("\033[1;32;40m  \n")

#Let me ask wether spy is new or older.
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)

#Let us  create some functions wich will make our program simple and beautiful.
def add_status():

    updated_status_message = None
#if else for satesfyng our conditions.
    if spy.current_status_message != None:

        cprint('Your current status message is %s \n' % (spy.current_status_message),'red')
    else:
        cprint('Right now you don\'t have any status message  \n','red')

#To ask to update new status or wants to choose from previous one's.
    default = raw_input("Do you want to select from the older status (y/n)? ")

#.upper command will automatically convert n to N.
    if default.upper() == "N":
        new_status_message = raw_input("What status do you want to set? ")

#len command is used to check the lenght.
        if len(new_status_message) > 0:
#.append will add new status in previous one's.
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

#for is a loop used to print message in loops.
        for message in STATUS_MESSAGES:
#%d is for integer value, %s is for strings.
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))


        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        cprint('The option you chose is not valid! Press either y or n.','red')

    if updated_status_message:
        cprint('Your updated status is: %s' % (updated_status_message),'red')
    else:
        cprint('No status right now','red')

#return will give updated status in this case.
    return updated_status_message


def add_friend():

    new_friend = Spy('','',0,0.0)
#Kindly enter frien's name.
    new_friend.name = raw_input("Kindly enter your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name
#Now ask the age of spy's friend.
    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)
#Ask for there rating.
    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        cprint('Sorry! we cann\'t add you as our spy right now ','red')

    return len(friends)

#For chatting u must select a friend.
def select_a_friend():
    item_number = 0

    for friend in friends:
        cprint('%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,friend.age,friend.rating),'blue')
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position

#After successful selection send message you want to send.
def send_message():
#Make your choice from added friend.
    friend_choice = select_a_friend()
#Now you have to ask for image in which spy will hide a secret message.
    original_image = raw_input("Kindly enter name of the image : ")
    output_path = "output.jpg"
    text = raw_input("Kindly enter you want to hide : ")
    Steganography.encode(original_image, output_path, text)

    new_chat = chat_message(text,True)


    if len(text) > 0:
        print "Your secret message image is ready!"
        friends[friend_choice].chats.append(new_chat)
#now wht if by mistake sender click enter before writing anything.


    else:
        print "Invalid entry! Please try again"
        send_message()


#Afre sending successful message other have to read it.
def read_message():

    sender = select_a_friend()

    output_path = raw_input("Kindly enter yourr file name : ")

    secret_text = Steganography.decode(output_path)

    new_chat = chat_message(secret_text,False)

    friends[sender].chats.append(new_chat)




#if sender is in trouble and sends any of these messages return them appropriate message.
    if secret_text in ['sos', 'SOS', 'SAVE ME', 'HELP', 'save me', 'help']:
        print "Our team will be there in just 5 min"
#If everyhing is fine the print the message send by spy.
    else:
        print "Your secret message is : " + secret_text


#this function will called when you have to read someones chat history.
def read_chat_history():

    read_for = select_a_friend()


    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            cprint('[%s]'%chat.time.strftime("%d %B %Y"),'blue')
            cprint('%s'%'you said : ','red')
            print '%s' %chat.message
        else:
            cprint('[%s]' % chat.time.strftime("%d %B %Y"),'blue')
            cprint('%s said : '% friends[read_for].name,'red')
            print '%s' %chat.message
#This will help in starting chat.
def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name

#here we have provided a condition.
    if spy.age > 12 and spy.age < 50:

#if condition get satesfied this line will be printed.
        print "Authentication complete. Welcome \n" + spy.name + " \nage : "  + str(spy.age) + " \nRating : " + str(spy.rating) + " \nGlad to see you back"

        show_menu = True

        while show_menu:
            menu_choices = "Kindly enter your choice \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
#elif is used when we have multiple condition
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False

#else this line will get printed.
    else:
        print 'Sorry you are too young to get tag of a spy '

if existing == "Y":
    start_chat(spy)
else:

    spy = Spy('','',0,0.0)


    spy.name = raw_input("Welcome to spy chat, you have to enter your spy name first : ")

    if len(spy.name) > 0:
        spy.salutation = raw_input("Should I call you Mr. or Ms. or Miss.?: ")

        spy.age = raw_input("Kindly enter your age : ")
        spy.age = int(spy.age)

        spy.rating = raw_input("Kindly enter your spy rating : ")
        spy.rating = float(spy.rating)

#here we are calling our start_chat function.
        start_chat(spy)
    else:
        print 'Please enter a valid spy name'