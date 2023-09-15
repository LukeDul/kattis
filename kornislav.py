a, b, c, d = map(int, input().split(" "))

def rectangleIsEnclosed (l1, l2, h1, h2 , depth, max_area):
    if depth == 4:
        print ("l1: ", l1, "l2: ", l2, "h1: ", h1, "h2: ", h2)
        return max_area
    
    elif (l2 <= l1 and h2 >= h1): 

        current_area = min(l1, l2) * min (h1, h2)

        if current_area > max_area:
            max_area = current_area

        return rectangleIsEnclosed(h2, l1, l2, h1, depth+1, max_area)

    else:
        return rectangleIsEnclosed(h2, l1, l2, h1, depth +1, max_area)

print(rectangleIsEnclosed(a, b, c, d, 0, 0))
