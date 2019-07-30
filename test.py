def simpleArraySum(ar):
    #
    # Write your code here.
    # ar_count = int(input())
    result=0
    for i in range (len(ar)):
         result+=ar[i]
        # i+=1
        #  print(i)
    return result

print("The sum of numbers in the array is : {}".format(simpleArraySum([1,2,4,6,9])))
