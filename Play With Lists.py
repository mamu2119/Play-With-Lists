L = [5465,2123,6878,7,54,561465,653,7777777]
print("Original List :", L)
count = 0
for i in L:
    count += i
avg = count/len(L)
print("sum = ", count)
print("average = ", avg)
L.sort()
print("Smallest element is:", L[0])
print("Largest element is:", L[-1])