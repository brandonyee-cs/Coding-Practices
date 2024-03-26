import random

def totalSales(): #1 Total Sales
    dowdict = {0 : 'Saturday', 1 : 'Monday', 2 : 'Tuesday', 3 : 'Wednesday', 4 : 'Thursday', 5 : 'Friday', 6 : 'Sunday'}; sales = []
    for i in range(7): sales.append(int(input(f"Enter {dowdict.get(i)}'s sales: ")))
    return sum(sales)

print(f"Total sales this week: {totalSales()}")

def lottoNumGen(): #2 Lottery Number Generator
    num = []; lottonum = ""
    for i in range(7): num.append(random.randint(0, 9))
    for i in range(len(num)): lottonum += str(num[i])
    return lottonum

print(f"The Lottery Number Today is: {lottoNumGen()}")

def numAnalysis(): #3 Number Analysis
    nums = []; average = 0
    for i in range(20): nums.append(int(input(f"Enter number {i+1}: ")))
    for i in range(len(nums)): average += nums[i]
    return min(nums), max(nums), sum(nums), average/20

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
    matrix = [[4,9,2], [3,5,7], [8,1,6]]; sum_list = []; result1 = 0; result2 = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])): matrix[i][j] = int(input("Enter value: "))
    iSize = len(matrix[0]); sum_list.extend([sum (lines) for lines in matrix])   
    for col in range(iSize): sum_list.append(sum(row[col] for row in matrix))
    for i in range(0,iSize): result1 += matrix[i][i]  
    for i in range(iSize-1,-1,-1): result2 += matrix[i][i]
    sum_list.append(result1); sum_list.append(result2)
    if len(set(sum_list))>1: return False
    return True

flag = magicSquare(); print(f"{'You have a Lo Shu Magic Square' if flag == True else 'You dont have a Lo Shu Magic square'}")