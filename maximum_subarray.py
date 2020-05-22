def maximum_subarray(input_arr):
    max_int=-2**32-1
    max_sum=0
    for i in input_arr:
        max_sum+=i
        if max_int<max_sum:
            max_int=max_sum
        if max_sum<0:
            max_sum=0
    return max_int
if __name__ == '__main__':
    input_arr=[2,4,5,8,9,3,0,1,4]
    print(maximum_subarray(input_arr))
