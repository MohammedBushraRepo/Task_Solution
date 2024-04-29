def get(map):
    rows = len(map)
    colms = len(map[0])

    ans = 0

    for r in range(rows):
        for c in range(colms):
            low_point = True
            for d in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                rr = r + d[0]
                cc = c + d[1]

                if not ((0 <= rr and rr < rows) and (0 <= cc and cc < colms)):
                    continue

                if map[rr][cc] <= map[r][c]:
                    low_point = False
                    break

            if low_point:
                ans += map[r][c] + 1

    print(ans)

map = [
    [2,1,9,9,9,4,5,2,1,0],
    [3,9,8,7,8,9,4,9,1,0],
    [9,8,5,6,7,8,9,8,9,2],
    [8,7,6,7,8,9,6,7,8,9],
    [9,8,9,9,9,6,5,6,7,8]
]
get(map)