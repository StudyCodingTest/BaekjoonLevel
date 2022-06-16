import sys

def make_star_list(i, j, n, star_list):
    if n == 3:
        star_list[i][j] = '*'
        star_list[i+1][j-1] = '*'
        star_list[i+1][j+1] = '*'
        for col in range(j-2, j+3):
            star_list[i+2][col] = '*'
    else:
        star_list = make_star_list(i, j, n//2, star_list)
        star_list = make_star_list(i+n//2, j-n//2, n//2, star_list)
        star_list = make_star_list(i+n//2, j+n//2, n//2, star_list)
    return star_list

N = int(input())
empty_list = [[' ' for _ in range(2*N-1)] for _ in range(N)]
star_list = make_star_list(0, N-1, N, empty_list)
star_string = '\n'.join([''.join(row) for row in star_list])
sys.stdout.write(star_string)