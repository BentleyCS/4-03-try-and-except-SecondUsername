#No using the built in type check function
#https://www.w3schools.com/python/python_try_except.asp


def sum(arr : list) -> int:
    sum = 0
    index = 0
    for _ in arr:
        try:
            sum += arr[index]
        except:
            pass
        index += 1
        # print("sum: ", sum)
        # print("index: ", sum)
    """
    Modify the function such that it returns the sum of all numebrs within the given list.
    :param arr:
    :return:
    """
    return  sum

def cleanData(rawData : list) ->list:
    clean_list = []
    for i in rawData:
        try:
            clean_list.append(float(i))
        except:
            pass
    return clean_list
    """
    modify the function such that it takes in a list as an argument will return a new list that
     contains only the valeus that can be typecast to a float.
    :param rawData:
    :return:
    """
    pass
def unreliableCalculator(divisors : list) -> list:
    unreliable_result = []
    for i in divisors:
        try:
            unreliable_result.append(100/i)
        except ZeroDivisionError:
            unreliable_result.append("ZeroDivisionError")
        except TypeError:
            unreliable_result.append("TypeError")
    return unreliable_result

    """
    Modify the function such that it takes in a list as an argument and returns a new list where each
    index is 100 divided by the values from the input list.
    If division ever causes an error instead have the value be the type of error as a string.
    Example the list [100,50,25,"5"] as an argument would return [1, 2, 4, "TypeError"]
    :param divisors:
    :return:
    """
    pass

def upperAll(arr : list) -> None:
    index = 0
    for i in arr:
        try:
            arr[index] = i.upper()
        except:
            pass
        index+=1

    """
    Modiy the function such that is uppercases all strings within the given argument list.
    The string method .upper() turns all characters in as tirng uppercase.
    You should mpdify the original list not return a new list.
    :param arr:
    :return:
    """
    x = "hello"
    print(x)
    x = x.upper()
    print(x)


def firstItems(arr : list) -> list:
    first_list = []
    for i in range(0, len(arr)):
        try:
            first_list.append(arr[i][0])
        except:
            first_list.append(arr[i])
    return first_list
    """
    Modify the function below such that given a list of values. Many of the list elements will be lists
    themselves. For any list element that is a list grab the first element from that list. If the list
    element is not a list then just grab the value itself.
    Create a new list of all the first indexes of inner lists or just values themselves.
    Example firstItems( [[1,2],[3,4],[5,6],[7,8]],9 ) == [1,3,5,7,9]
    :param arr:
    :return:
    """
    pass

