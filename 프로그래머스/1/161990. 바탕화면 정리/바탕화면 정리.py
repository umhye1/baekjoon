def solution(wallpaper):
    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = 0,0
    
    # wallpaper에서 파일 위치를 구하기
    for x in range(len(wallpaper)):
        for y in range(len(wallpaper[0])):
            if wallpaper[x][y] == '#':
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                
                max_x = max(max_x, x)
                max_y = max(max_y, y)
    

    return min_x, min_y, max_x+1, max_y+1