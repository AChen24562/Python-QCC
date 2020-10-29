def middle(l):
    new_list = list(l[1:-1])
    return new_list


def main():
    num_List = [1, 2, 3, 4]
    mid_list = middle(num_List)
    print(f"Original {num_List}\nNew List {mid_list}")


main()
