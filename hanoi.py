def HanoiTower(n):
    
    # Check wrong input
    if n < 1:
        print('Invalid input')
        return
    if not isinstance(n, int):
        print('Invalid input')
        return
    # Create a storge
    storge = []
    this_string = [n, 'A', 'C']
    storge.append(this_string)
    finish = False
    while not finish:
        bool_list = []
        for string_list in storge:
            n = string_list[0]
            if n != 1:
                bool_list.append(0)
        # If finished, print it
        if not bool_list:
            for p_string_list in storge:
                p_start = p_string_list[1]
                p_end = p_string_list[2]
                print_string = p_start + '-->' + p_end
                print(print_string)
            break
        else:
            # A new turn
            new_storge = []
            for i_string_list in storge:
                if i_string_list[0] == 1:
                    new_storge.append(i_string_list)
                else:
                    n = i_string_list[0]
                    start = i_string_list[1]
                    end = i_string_list[2]

                    # to judge the direction
                    if start == 'A':
                        if end == 'B':
                            mid = 'C'
                        else:
                            if end == 'C':
                                mid = 'B'
                    else:
                        if start == 'B':
                            if end == 'A':
                                mid = 'C'
                            else:
                                if end == 'C':
                                    mid = 'A'
                        else:
                            if start == 'C':
                                if end == 'A':
                                    mid = 'B'
                                else:
                                    if end == 'B':
                                        mid = 'A'
                    # Recursion
                    this_string = [n - 1, start, mid]
                    new_storge.append(this_string)
                    this_string = [1, start, end]
                    new_storge.append(this_string)
                    this_string = [n - 1, mid, end]
                    # End of recursion
                    new_storge.append(this_string)
            # Renew storge
            storge = new_storge
            continue
    return


HanoiTower(4)

