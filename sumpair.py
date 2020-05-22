def sum_pair(input_arr,sum_given):
    """
    In array if the given sum pair exists or not
    """
    result=list()
    length=len(input_arr)
    for i in range(length):
        for j in range(i+1,length):
            if input_arr[i]+input_arr[j]==sum_given:
                result.append(input_arr[i])
                result.append(input_arr[j])
    return result
if __name__ == '__main__':
    input_arr=[1,2,5,3,7,5,8]
    sum_given=3
    print(sum_pair(input_arr,sum_given))
