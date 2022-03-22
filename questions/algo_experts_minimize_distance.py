blocks = [
    {"gym": False, "school": True, "store": False},
    {"gym": True, "school": False, "store": False},
    {"gym": True, "school": True, "store": False},
    {"gym": False, "school": True, "store": False},
    {"gym": False, "school": True, "store": True},
]

min_distances = []


def findMinDistance(current_index, key, blocks):
    # Look left
    distance_left = 0
    key_found_left = False
    i = current_index - 1
    cont_loop = True
    while i > 0 and cont_loop == True:
        for k, v in blocks[i].items():
            if k == key:
                if v == True:
                    key_found_left = True
                    distance_left = distance_left + 1
                    cont_loop = False
                    break
                else:
                    distance_left = distance_left + 1
        i = i - 1
    if key_found_left == False:
        distance_left = 9999999

    # Look right
    distance_right = 0
    key_found_right = 0
    i = current_index
    cont_loop = True
    for i in range(i + 1, len(blocks)):
        if cont_loop == False:
            break
        for k, v in blocks[i].items():
            if k == key:
                if v == True:
                    key_found_right = True
                    distance_right = distance_right + 1
                    cont_loop = False
                    break
                else:
                    distance_right = distance_right + 1
    if key_found_right == False:
        distance_right = 9999999

    return min(distance_right, distance_left)


def findOptimalBlock(blocks):
    # For each block, do the following
    for i in range(0, len(blocks)):
        distance = 0
        for k, v in blocks[i].items():
            if v == False:
                # Look left and right to find the max distance until value is True
                min_dist = findMinDistance(i, k, blocks)
                # Assuming POI will be eventually found - left or right
                distance = distance + min_dist
            else:
                distance = distance  # better way to handle this?

        min_distances.append(distance)
        print(min_distances)

    return None


findOptimalBlock(blocks)
