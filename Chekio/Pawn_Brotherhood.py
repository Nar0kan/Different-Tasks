def safe_pawns(pawns: set) -> int:
    # count will be returned as number of 'safe' pawns
    global count
    count = 0
    safe_list = []
    
    # check for pawns on borders
    def left_border(i, pawns):
        for el in pawns:
            if el[0] == chr(ord(i[0]) + 1) and int(el[1]) == int(i[1])-1 and i not in safe_list:
                count += 1
                safe_list.append(i)
                #print(i, ", safe")
        return count

    def right_border(i, pawns):
        global count
        for el in pawns:
            if el[0] == chr(ord(i[0]) - 1) and int(el[1]) == int(i[1])-1 and i not in safe_list:
                count += 1
                safe_list.append(i)
                #print(i, ", safe")
        return count

    # check for pawns inside
    def inside(i, pawns):
        global count
        for el in pawns:
            if el[0] == chr(ord(i[0]) + 1) and int(el[1]) == int(i[1])-1 and i not in safe_list:
                count += 1
                safe_list.append(i)
                #print(i, ", safe")
            elif el[0] == chr(ord(i[0]) - 1) and int(el[1]) == int(i[1])-1 and i not in safe_list:
                count += 1
                safe_list.append(i)
                #print(i, ", safe")
        return count

    # main loop, that maintain upper functions, depending on each pawn spot
    
    for element in pawns:
        if '1' in element:
            pass
        elif 'a' in element:
            left_border(element, pawns)
        elif 'h' in element:
            right_border(element, pawns)
        else:
            inside(element, pawns)
    
    return count


print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}), '\t',
      safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}))
