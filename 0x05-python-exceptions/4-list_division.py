#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    ans_list = []
    for i in range(list_length):
        ans = 0
        try:
            ans = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            ans_list.append(ans)
    return ans_list
