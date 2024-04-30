import random

def totalSales(): #1 Total Sales
    dowdict = {0 : 'Saturday', 1 : 'Monday', 2 : 'Tuesday', 3 : 'Wednesday', 4 : 'Thursday', 5 : 'Friday', 6 : 'Sunday'}; sales = []; sum = 0
    for i in range(7): sales.append(int(input(f"Enter {dowdict.get(i)}'s sales: ")))
    for i in range(len(sales)): sum += sales[i]
    return sum

print(f"Total sales this week: {totalSales()}")

def lottoNumGen(): #2 Lottery Number Generator
    num = []; lottonum = ""
    for i in range(7): num.append(random.randint(0, 9))
    for i in range(len(num)): lottonum += str(num[i])
    return lottonum

print(f"The Lottery Number Today is: {lottoNumGen()}")

def numAnalysis(): #3 Number Analysis
    nums = []; average = 0; sum = 0
    for i in range(20): nums.append(int(input(f"Enter number {i+1}: ")))
    for i in range(len(nums)): average += nums[i]; sum += nums[i]
    for i in range(len(nums)): 
        if i == 0: max = nums[i]; min = nums[i]
        max = int(f"{nums[i] if nums[i] > max else max}"); min = int(f"{nums[i] if nums[i] < min else min}")
    return min, max, sum, average/20

min, max, sum, average = numAnalysis(); print(f"Lowest number: {min}\nHighest Number: {max}\nSum of all numbers: {sum}\nAverage of all numbers: {average}")

def driversLisence(): #4 Drivers License Test
    correctAnswers = [1,3,1,1,4,2,3,1,3,2,1,4,3,1,4,3,2,2,4,1]; tests =[[1,3,1,1,4,2,3,1,3,2,1,4,3,1,4,3,2,2,3,2], [1,3,2,1,3,2,3,2,3,2,1,3,3,1,2,3,2,2,4,1], [1,2,1,1,4,2,3,1,4,2,1,4,3,2,3,3,2,2,4,1]]; results = []
    for i in range(len(tests)): 
        numwrong = 0 
        for j in range(len(tests[i])):
            if correctAnswers[j] != tests[i][j]: numwrong += 1
        results.append(numwrong)
    return results

for i in range(len(driversLisence())): print(f"Student {i+1} got a {20 - driversLisence()[i]}/20, they {'Pass' if (20-driversLisence()[i])> 15 else 'Fail'}.")

def magicSquare(): #5 Lo Shu Magic Square
    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            num = int(input(f"Enter element {i+1},{j+1}: "))
            while num > 9: int(input("Number already exists, please re-enter: "))
            while num in row: num = int(input("Number already exists, please re-enter: "))
            for k in range(len(matrix)):
                while num in  matrix[k]: num = int(input("Number already exists, please re-enter: "))
            row.append(num)
        matrix.append(row)
    if matrix[0][0]+matrix[0][1]+matrix[0][2] != 15 or matrix[1][0]+matrix[1][1]+matrix[1][2] != 15 or matrix[2][0]+matrix[2][1]+matrix[2][2] != 15 or matrix[0][0]+matrix[1][0]+matrix[2][0] != 15 or matrix[0][1]+matrix[1][1]+matrix[2][1] != 15 or matrix[0][2]+matrix[1][2]+matrix[2][2] != 15 or matrix[0][0]+matrix[1][1]+matrix[2][2] != 15 or matrix[0][2]+matrix[1][1]+matrix[2][0] != 15: return False
    return True

flag = magicSquare(); print(f"{'You have a Lo Shu Magic Square' if flag == True else 'You dont have a Lo Shu Magic square'}")

def magicSquare(): #6 Lo Shu Magic Square EXTRA CREDIT
    matrix = []; lenmatrix = int(input("Enter the size of the matrix: "))
    for i in range(lenmatrix):
        row = []
        for j in range(lenmatrix):
            num = int(input(f"Enter element {i+1},{j+1}: "))
            while num in row: num = int(input("Number already exists, please re-enter: "))
            for k in range(len(matrix)):
                while num in  matrix[k]: num = int(input("Number already exists, please re-enter: "))
            row.append(num)
        matrix.append(row)
    tempsum = sum(matrix[i])
    for i in range(len(matrix)):
        if sum(matrix[i]) != tempsum : return False
        for j in range(len(matrix[i])):
            tempmatrix = []
            for l in range(lenmatrix):
                tempmatrix.append(matrix[l][j])
            if sum(tempmatrix) != tempsum: return False
    return True

flag = magicSquare(); print(f"{'You have a Lo Shu Magic Square' if flag == True else 'You dont have a Lo Shu Magic square'}")