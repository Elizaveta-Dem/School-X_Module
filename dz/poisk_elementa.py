def elements(N):
    indexes_elements: list =[]

    for i in range(1,len(N)):
        if N[i] != N[i-1] + 1:
            indexes_elements.append(i)  #записать индекс элемента

    if indexes_elements:
        return indexes_elements
    else:
        return "Not found"
    
print(*elements([1, 3, 5, 6, 8]))

# 0 1 2 3 4 5 index
# 0 1 3 5 6 8

# 0 1 2 3 4 5 index
# 1 3 5 6 8