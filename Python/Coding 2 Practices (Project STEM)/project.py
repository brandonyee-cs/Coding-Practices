
story = "A vacation is when you take a trip to some ADJECTIVE1 place with your ADJECTIVE2 family. Usually you go to some place that is near a/an NOUN1 or up on a/an NOUN2. A good vacation place is one where you can ride  PLURAL_NOUN1 or play GAME or go hunting for PLURAL_NOUN2. I like to spend my time VERB_ENDING_IN_ING1 or  VERB_ENDING_IN_ING2. When parents go on a vacation, they spend their time eating three PLURAL_NOUN3 a day, and fathers play gold, and mothers sit around VERB_ENDING_IN_ING3. Last summer, my little brother fell in a/an NOUN3 and got poison PLANT all over his PART_OF_THE_BODY. My family is going to go to (the) PLACE and I will practice VERB_ENDING_IN_ING4. Parents need vacations more than kids because parents are always very ADJECTIVE3 and because they have to work NUMBER hours every day all year making enough PLURAL_NOUN4 to pay for the vacation."

def madlibreplace(story):
  for i in range(len(story)):
    spaceorperiodindex = 'value'
    if story[i].isupper() == True:
      if i != len(story):
        if story[i+1].isupper() == True:
          j = i
          while spaceorperiodindex == 'value':
            j += 1
            if story[j] == " " or story[j] == ".":
              spaceorperiodindex = j
          inquiry = input("Enter a " + story[i:spaceorperiodindex] + ": ")
          story = story[:i] + inquiry + story[spaceorperiodindex:]
  return story

print(madlibreplace(story))