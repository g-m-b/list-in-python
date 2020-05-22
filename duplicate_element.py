def repeat(input_arr):
    length=len(input_arr)
    for i in range(0,length+1):
        for j in range(1,length+1):
            if input_arr[i]==input_arr[j]:
                return input_arr[i]
if __name__ == '__main__':
    input_arr=[1,1,2,3,4]
    print(repeat(input_arr))
