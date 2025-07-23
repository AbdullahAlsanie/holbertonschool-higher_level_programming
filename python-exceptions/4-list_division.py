#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    if (my_list_1 and my_list_2):
        new_list = []
        for i in range(list_length):
            result = 0
            try:
                result = my_list_1[i] / my_list_2[i]
            except (TypeError, ValueError):
                print("{}".format("wrong type"))
            except ZeroDivisionError:
                print("{}".format("division by 0"))
            except IndexError:
                print("{}".format("out of range"))
            finally:
                new_list.append(result or 0)
        return (new_list)
