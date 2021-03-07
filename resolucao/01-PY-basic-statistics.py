
#resolução 01

def findMean(a, n):
    sum = 0
    for i in range( 0, n):
        sum += a[i]
    return float(sum/n)

def findMedian(a, n):
    a.sort()
    even = True
    if len(a)%2 == 1:
        even = False
    if even:
        slice_start = (len(a)//2) - 1
        slice_end   = (len(a)//2) + 1
        median      = sum(a[slice_start:slice_end]) / 2
    else:
        median      = a[len(a)//2]
    return float(median)

def findMode(a,n):
    sorted(a)
    numbers = dict()
    for item in a:
        if item not in numbers:
            numbers[item] = 1
        else:
            numbers[item] = numbers[item] + 1
    max_count = 0
    for key in numbers:
        if numbers[key] > max_count:
            max_count = numbers[key]
    max_modal_elements = []
    for key in numbers:
        if numbers[key] == max_count:
            max_modal_elements.append(key)
    mode = min(max_modal_elements)
    return float(mode)


n = int(input())
number = input()
number = list(map(int, number.split()))

mean = findMean(number,n)
median = findMedian(number,n)
mode = findMode(number,n)

print(mean)
print(median)
print(mode)


#---------------------------------------------------------------------------------------------------------
# resolução 02
def scale(n, scale):
    """Returns n with a number of decimal places equal to scale, after rounding.
    """
    return int(n*10**scale + .5) / 10**scale


_ = input()
line = input()
values = line.split()
numbers = [int(i) for i in values]

# mean
average = sum(numbers) / len(numbers)

# median
numbers.sort()
N = len(numbers)
if (N%2 == 0):          
    leftOfCentre = numbers[int (N/2)-1]
    rightOfCentre = numbers[int (N/2)]
    median = (leftOfCentre + rightOfCentre) / 2
else:
    median = numbers[int (N/2)]
    
# mode
count = {}
max = None
for item in numbers:
    if item in count:
        count[item] = count[item] + 1
    else:
        count[item] = 1
    if max is None:
        max = (item, 1)
    else:
        if count[item] > max[1]:
            max = (item, count[item])
mode = max[0]

print (scale(average,1))
print (scale(median,1))
print (mode)