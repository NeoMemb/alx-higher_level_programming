#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
<<<<<<< HEAD
    """Print x elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
=======
    count = 0
    try:
        for i in range(0):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    print()
    return (count)
>>>>>>> 5db41e9b69095061c370275f6a9181938f268163
