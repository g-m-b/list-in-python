def zeroones(input_arr):
    count=0
    length=len(input_arr)
    for i in input_arr:
        if i==0:
            count+=1
    for j in range(0,count):
        input_arr[j]=0
    for n in range(count,length):
        input_arr[n]=1
    return input_arr
if __name__ == '__main__':
    input_arr=[0,1,0,1,0,0,0,0,1]
    print(zeroones(input_arr))
