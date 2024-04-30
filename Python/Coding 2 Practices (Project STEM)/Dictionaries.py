def Course_Information(): 
    print('Course Information')

    room = { 
    'CS101' : '3004',
    'CS102' : '4501',
    'CS103' : '6755',
    'NT110' : '1244',
    'CM241' : '1411'
    }
    instructor = {
        'CS101' : 'Haynes',
        'CS102' : 'Alvarado',
        'CS103' : 'Rich',
        'NT110' : 'Burke',
        'CM241' : 'Lee'
    }
    time = {
        'CS101' : '8:00 AM',
        'CS102' : '9:00 AM',
        'CS103' : '10:00 AM',
        'NT110' : '11:00 AM',
        'CM241' : '1:00 PM'
    }
    
    userinput = input("Enter Course Number: ")

    if  userinput in room:
        print(f"{userinput}: Room {room[userinput]}, Instructor {instructor[userinput]}, Time  {time[userinput]}")
    else:
        print("Error // Course Not Available.")

Course_Information()

def NameandEmailAddresses():
    print("Email List:")
    loop = True

    phonebook = {}

    while loop == True:

        userinput = input('Enter Option (d for delete, a for add, l for lookup, q for quit): ')

        if userinput == 'd':
            keytodelete = input('Enter  name to be deleted: ')
            del phonebook[keytodelete]

        elif userinput == 'a':
            keytoadd = input('Enter name to be added: ' )
            numbertoadd = input('Enter corresponding email: ')
            phonebook[keytoadd] = numbertoadd

        elif userinput == 'l':
            keytolookup = input('Enter name to be looked up: ')
            if keytolookup in phonebook:
                print(f"{keytolookup}'s email is {phonebook[keytolookup]}")
            else:
                print("Error // Name Not Available")
        
        elif userinput == 'q':
            loop = False

        else: 
            print('Error // Option is not Available.')

NameandEmailAddresses()