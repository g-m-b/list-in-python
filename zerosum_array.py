def zerosum(input_arr):
    """
    Checks wheter an array consits of zero sum
    parameters are input array
    """
    set_sum=set()
    set_sum.add(0)
    sum=0
    for i in input_arr:
        sum+=i
        if sum in set_sum:
            return True
        set_sum.add(sum)
    return False
if __name__ == '__main__':
    input_arr=[1,-1,2,3,4,5,8,9,-9]
    if zerosum(input_arr):
        print("Zero sum is present")
    else:
        print("Zero sum is not present")
