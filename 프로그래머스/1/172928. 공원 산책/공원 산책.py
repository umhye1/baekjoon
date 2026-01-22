def solution(park, routes):
    h = len(park) # 행
    w = len(park[0]) # 열
    
    directions = {'N':(-1,0), 'S':(1,0), 'W':(0,-1), 'E':(0,1)}
    
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                x,y = i,j
    
    for k in routes:
        route,num = k.split(" ")
        num = int(num)
        
        now_x, now_y = x, y
        is_okay = True
        
        
        for _ in range(num):
            dx, dy = directions[route]
            nx, ny = now_x + dx , now_y + dy
            
            if 0 <= nx <h and 0<= ny < w and park[nx][ny]!='X':
                now_x = nx
                now_y = ny
            
            else :
                is_okay = False
                break
            
        if is_okay:
            x,y = now_x, now_y

    return [x,y]