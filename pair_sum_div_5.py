# Given an array "arr", find the pair of elements whose sum is divisible by 5 and print those pairs.
# Also find the total number of such pair of elements whose sum is an even number.
#
# Note: Please read both the parts of question properly and then attempt.
# Don't take static array, create a method that will take any array as input.
def arrayDivision(arr):
    fiveCount=0
    evenCount=0
    div_five=[]
    div_even=[]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if (arr[i]+arr[j])%5==0:
                fiveCount+=1
                div_five.append((arr[i],arr[j]))

            if (arr[i]+arr[j])%2==0:
                evenCount+=1
                div_even.append((arr[i], arr[j]))
    return [{'Count':fiveCount, "Pairs of Five_div":div_five},
            {"Count":fiveCount,"Pairs of Five_div":div_five}]


arr= []
n = int(input("Enter number of elements to be inserted in list : "))
for i in range(0, n):
     element= int(input())
     arr.append(element)


obj=arrayDivision(arr)
print(obj)