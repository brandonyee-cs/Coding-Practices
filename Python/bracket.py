class bracket:
    
    def __init__(self) -> None:
        self.weightclass = [106, 115, 120, 125, 130, 135, 140, 145, 155, 160, 170, 175, 190, 210, 285]
        self.brackets = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        self.currentbracket = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        self.done = False
    
    def setup(self):
        # Setting up Bracket
        for i in range(len(self.weightclass)): 
            for j in range(int(input(f"Enter number of participants for weight class {self.weightclass[i]}: "))):

                inp = input("Enter the seed and the name of the participant: (seed name): ").split()
                seed = int(inp[0]); name = inp[1]
                self.brackets[i].append([seed,name])

            self.brackets[i] = sorted(self.brackets[i], key=lambda x: x[0]) #Sorts each indivisual weightclass bracket by it's seed
        
    def update(self):
        # Setting Up Visible Bracket
        for i in range(len(self.brackets)):
            tempbracket = []

            # Tests for an odd number of participants in a bracket and gives the #1 see a pass
            self.passvar = False if (len(self.brackets[i]) % 2) != 0 else True
            if self.passvar == True: tempbracket.append(f"{self.brackets[i][0][1]} vs PASS")

            for j in range(0, len(self.brackets[i]), 2):
                if self.passvar == True and j == 0: pass # Makes sure not to reappend the first seed if their is a Pass
                else: tempbracket.append(f"{self.brackets[i][j][1]} vs {self.brackets[i][j+1][1]}")
            
            for j in range(len(self.currentbracket)):
                self.currentbracket[j].append(tempbracket)

    def updatebracket(self):
        self.tempbracket = self.brackets; self.brackets = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        for i in range(len(self.weightclass)):
            for j in range(len(self.tempbrackets[i])):
                winner = input(f"Who won {self.currentbracket[i][j]}? ")
                self.brackets[i].append({winner})

    def get_currentbracket(self):
        wc = int(input("Enter the weight class of the bracket you are searching for: "))
        ind = (self.brackets).index(wc)
        
        for i in range(len(self.currentbracket[ind])):
            print(self.currentbracket[ind[i]])
    
    def checkbracket(self):
        # Check to make sure all brackets have been completed
        bracketsflag = 0
        for i in range(self.brackets):
            if len(self.brackets[0]) == 0: bracketsflag += 1
        if bracketsflag == len(self.brackets): self.done = True

def main():
    test = bracket()
    bracket.setup(test)
    
    while test.done == False:

        userinput = input("(Show for Current Bracket | Change to edit the bracket) ")
        if userinput == 'Show': bracket.get_currentbracket(test)
        elif userinput == 'Change': bracket.updatebracket(test)
        else: print('Error // Command Not Found')

        bracket.checkbracket(test)

main()