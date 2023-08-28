def maxDropPoints(n, x_coords, y_coords):
    dic_x = {}
    dic_y = {}
    for i in range(n):
        if x_coords[i] not in dic_x:
            dic_x[x_coords[i]] = 1
        else:
            dic_x[x_coords[i]] += 1
        
        if y_coords[i] not in dic_y:
            dic_y[y_coords[i]] = 1
        else:
            dic_y[y_coords[i]] += 1
        
    return max(max(dic_x.values()), max(dic_y.values()))
if __name__ == '__main__':
    num_x_coord = int(input().strip())
    x_coords = list(map(int, input().split()))
    num_y_coord = int(input().strip())
    y_coords = list(map(int, input().split()))
    print(maxDropPoints(num_x_coord, x_coords, y_coords))
