#1 Sentence Capitalizer
def sent_caps(string):
    string = string[0].upper() + string[1:]
    for i in range(len(string)):
        if string[i] == '.':
            string = string[:i+2] + string[i+2].upper() + string[i+3:]
    return string

string = input("Enter a Sentence: ")
print("New String: ", sent_caps(string))

#2 Word Seperator
def word_sep(string):
    result = ""
    for i in range(len(string)):
        if i > 0 and string[i-1].islower() and string[i].isupper():
            result += " "
        result += string[i]
    return result

string = input("Enter a Sentence: ")
print("New String: ", word_sep(string))

#3 English --> Pig Latin Converter
def piglatconv(string):
  string = string.upper(); last_index = 0; word = ''; piglatay = ''; piglat = ''
  for i in range(len(string)):
    if string[i] == " ":
      piglatay += string[last_index:i] + "AY "; last_index = i + 1
  piglatay += string[last_index:] + "AY"; last_index = 0
  for j in range(len(piglatay)):
    if piglatay[j] == " " or j == len(piglatay)-1:
      word = piglatay[last_index:j]; piglat += word[1:len(word)-2] + word[0] + "AY "; last_index = j + 1
    word = ""
  return piglat

string = input("Enter a sentence: ")
print(piglatconv(string))

#4 System Login and Password
def sysnames(firstname, lastname, ID): #4.A
    login = ""
    for i in range(0, 3):
       login += firstname[i]
    for j in range(0, 3):
       login += lastname[j]
    login += ID[-3]
    login += ID[-2]
    login += ID[-1]
    return login

def passdefiner(): #4.B
   validpass = False
   upper = 0
   lower = 0
   nummer = 0
   while validpass == False:
    trypass = input("Enter a Password: ")
    for char in trypass:
        if upper == 0 and char.isupper() == True:
            upper = 1
        if lower == 0 and char.islower() == True:
            lower = 1
        if nummer == 0 and char.isnumeric() == True:
            nummer = 1
    if upper == 1 and lower == 1 and nummer ==1:
       print("Password is valid.")
       validpass = True
    else:
       print("Password is not valid!")

firstname = input("First Name: ")
lastname = input("Last Name: ")
a = input("Student ID: ")
print("Your system login name: ", sysnames(firstname,lastname, a))
passdefiner()