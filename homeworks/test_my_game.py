def beginning_zeros(number: str) -> int:
    # your code here
    #my_number = number.count('0')
    num = ('1234')
    my_number = enumerate(number)
    my_dict = dict(my_number)

    print(dict(my_number))
    print(my_dict)
    values = my_dict.values()

    print(values)
    my_num = ()
    for keys, values in my_dict:
        if values == 0:
            my_num.append(values)

    count = 0
    #for i in my_number:
        #while my_number.values() == 0:

            #if n
            #count += 1



       # my_dict.append(i)

        #print(my_dict)


        #while number.values() == 0:





        #if i == '0':
            #my_number += 1
    #print(my_number)
    #return my_number


if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print("Coding complete? Click 'Check' to earn cool rewards!")

