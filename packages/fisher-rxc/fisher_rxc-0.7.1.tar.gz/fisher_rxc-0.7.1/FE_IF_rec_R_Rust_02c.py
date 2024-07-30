import math
import numpy as np
#import os
import time
#import datetime
#os.environ['R_HOME'] = 'c:\\Program Files\\R\\R-4.3.2'
#c:\Program Files\R\R-4.3.2\bin\x64\
#import rpy2.robjects.numpy2ri
#from rpy2.robjects.packages import importr
#rpy2.robjects.numpy2ri.activate()
#stats = importr('stats')
import fisher

def _dfs(mat, pos, r_sum, c_sum, p_0, p):
    (xx, yy) = pos
    (r, c) = (len(r_sum), len(c_sum))
    mat_new = []
    for i in range(len(mat)):
        temp = []
        for j in range(len(mat[0])):
            temp.append(mat[i][j])
        mat_new.append(temp)
    if xx == -1 and yy == -1:
        for i in range(r-1):
            temp = r_sum[i]
            for j in range(c-1):
                temp -= mat_new[i][j]
            mat_new[i][c-1] = temp
        for j in range(c-1):
            temp = c_sum[j]
            for i in range(r-1):
                temp -= mat_new[i][j]
            mat_new[r-1][j] = temp
        temp = r_sum[r-1]
        for j in range(c-1):
            temp -= mat_new[r-1][j]
        if temp <0:
            return
        mat_new[r-1][c-1] = temp

        p_1 = 1
        for x in r_sum:
            p_1 *= math.factorial(x)
        for y in c_sum:
            p_1 *= math.factorial(y)
        n = 0
        for x in r_sum:
            n += x
        p_1 /= math.factorial(n)

        for i in range(len(mat_new)):
            for j in range(len(mat_new[0])):
                p_1 /= math.factorial(mat_new[i][j])
        if p_1 <= p_0 + 0.00000001:
            #print(mat_new)
            #print(p_1)
            p[0] += p_1
    else:
        max_1 = r_sum[xx]
        max_2 = c_sum[yy]
        for j in range(c):
            max_1 -= mat_new[xx][j]
        for i in range(r):
            max_2 -= mat_new[i][yy]
        for k in range(min(max_1,max_2)+1):
            mat_new[xx][yy] = k
            if xx == r-2 and yy == c-2:
                pos_new = (-1, -1)
            elif xx == r-2:
                pos_new = (0, yy+1)
            else:
                pos_new = (xx+1, yy)
            _dfs(mat_new, pos_new, r_sum, c_sum, p_0, p)
def fisher_exact(table):
    row_sum = []
    col_sum = []
    for i in range(len(table)):
        temp = 0
        for j in range(len(table[0])):
            temp += table[i][j]
        row_sum.append(temp)
    
    for j in range(len(table[0])):
        temp = 0
        for i in range(len(table)):
            temp += table[i][j]
        col_sum.append(temp)
    mat = [[0] * len(col_sum)] * len(row_sum)
    pos = (0, 0)
    p_0 = 1
    for x in row_sum:
        p_0 *= math.factorial(x)
    for y in col_sum:
        p_0 *= math.factorial(y)
    n = 0
    for x in row_sum:
        n += x
    p_0 /= math.factorial(n)
    for i in range(len(table)):
        for j in range(len(table[0])):
            p_0 /= math.factorial(table[i][j])
    p = [0]
    _dfs(mat, pos, row_sum, col_sum, p_0, p)
    return p[0]

start = time.time()
tests =[
    [[10, 8, 8, 12, 12], [8, 11, 10, 9, 11]],
    [[8, 3, 9, 7], [8, 6, 6, 6], [6, 8, 6, 3]], 
    [[11,12,18,15],[15,13,13,15],[15,19,19,15]],
    [[8, 3, 5, 5, 6], [4, 3, 8, 6, 5], [2, 5, 3, 7, 6], [4, 8, 2, 3, 6]],
    [[1, 0, 0, 0, 1], [1, 2, 0, 2, 1], [1, 0, 1, 2, 1], [1, 1, 1, 3, 1], [1, 2, 1, 1, 1]],
    [[41,22,18,5],[5,3,3,0],[20,9,9,0],[10,4,5,3],[16,6,6,1],[13,8,5,2]]       
    ]
#a = [[11,12,18,15],[15,13,13,15],[15,19,19,15]] 

for a in tests:

    print(a)
    m = np.array(a)

    #print("Two sided fisher's exact test")
    #startr = time.time()
    #res = stats.fisher_test(m, simulate_p_value=True, B=1000000)
    #print('p-value - R (MC): {:.4f}'.format(res[0][0]) ,"   ", f"{time.time()-startr:.3f}"  )
    startr = time.time()
    rust_mc= fisher.sim(a,1000000)
    print('p-value - Rust (MC): {:.4f}'.format(rust_mc) ,"   ", f"{time.time()-startr:.3f}"  )
    startr = time.time()
    rust_iter= fisher.exact(a)
    print('p-value - Rust (analitical, Fortr): {:.4f}'.format(rust_iter) ,"   ", f"{time.time()-startr:.3f}" )
    if m.size <= 25: 
        #startr = time.time()
        #res = stats.fisher_test(m, workspace=2e8, )
        #print('p-value - R (Analitical): {:.4f}'.format(res[0][0]) ,"   ", f"{time.time()-startr:.3f}"  )

        
        """
        if m.size <= 15: 
            startr = time.time()
            rust_rec= fisher.recursive(a)
            print('p-value - Rust (Rec): {:.4f}'.format(rust_rec) ,"   ", f"{time.time()-startr:.3f}" )

            if m.size <= 12:     
                startr = time.time()
                print("p-value - Py (Rec) : {:.4f}".format(fisher_exact(a)) ,"   ", f"{time.time()-startr:.3f}"  )
        """
    endtime = time.time()
    print("\nKÉSZ   ", endtime-start)
    print("-------------------------------------------")





# [[1,24],[5,20],[14,11],[11,14]]  Two sided fisher's exact test:   0.0001228337404686859,  R R MC: p-value - R: 0.000130999869000131


# [[41,22,18,5],[5,3,3,0],[20,9,9,0],[10,4,5,3],[16,6,6,1],[13,8,5,2],[19,12,12,6],[28,16,9,2]]  
# [[41,22,18,5],[5,3,3,0],[20,9,9,0],[10,4,5,3],[16,6,6,1],[13,8,5,2],[19,12,12,6],[28,16,9,2]]  sokáig fut/nem fut le ...  R MC  p-value - R: 0.9287610712389288

#[[3,1,1,1,0],[1,4,1,0,0],[2,1,3,2,0],[1,1,1,2,0],[1,1,0,0,3],[2,1,1,0,0],[1,1,1,2,0],[2,2,2,0,0],[2,2,2,0,0],[3,2,2,0,0],[2,3,3,0,0],[1,2,1,1,0]] 0.828  p-value - R: 0.8365817091454273  p-value - R: 0.8302201697798303 (10 000 000 kísérlet)

#[[41,22,18,5],[5,3,3,0],[20,9,9,0],[10,4,5,3],[16,6,6,1],[13,8,5,2],[19,12,12,6],[28,16,9,2]]     p-value - R: 0.9287610712389288
# [[1,0,0,0,1],[1,2,0,2,1],[1,0,1,2,1],[1,1,1,3,1],[1,2,1,1,1]] Jamovi Fisher's exact test	0.880 MC-vel, Py Two sided fisher's exact test:   0.9911507266330448,  Py R p-value - R: 0.991080008919991
# [[1,2,0,1,0,1,0,1,0,2],[1,0,0,0,1,1,2,1,3,0],[1,2,0,2,1,0,3,1,1,1],[1,0,1,2,1,0,2,2,0,1],[1,1,0,1,3,2,1,1,0,2],[1,2,2,0,0,1,1,0,2,0],[1,1,1,3,1,1,0,1,2,0],[2,0,1,0,0,1,1,1,1,1],[1,2,1,1,1,0,1,0,0,1],[2,0,1,1,2,1,0,0,0,2]]
# p-value - R (MC): 0.9446620553379447
# p-value - Rust (MC): 0.9443430556569443
# Jamovi (MC): 0,880
# 
# [[3,4,9,4,7,5],[5,5,7,7,4,4],[7,9,1,5,5,8]] Jamovi: 0.182
#6x3 p-value - R (MC): 0.18247681752318248
#p-value - Rust (MC): 0.18217881782118217

# [[6,8,6,3],[8,3,9,7],[8,6,6,6],[5,8,3,7]]  
# [[4,2,2,0],[4,2,4,7],[3,4,1,3],[4,3,1,6]] Jamovi Fisher's exact test 0.401	 p-value - R (MC): 0.4000825999174001 p-value - Rust (MC): 0.40102459897540105 p-value - Rust (Rec): 0.4009153791697379

"""
# [[10,8,8,12,12],[8,11,10,9,11]]
#[[10, 8, 8, 12, 12], [8, 11, 10, 9, 11]]
#Two sided fisher's exact test
p-value : 0.8583     0.592
p-value - R (Analitical): 0.8583     0.040
p-value - Rust (Rec): 0.8583     0.194
p-value - R (MC): 0.8588     0.891
p-value - Rust (MC): 0.8585     0.886
"""
"""
[[8, 3, 9, 7], [8, 6, 6, 6], [6, 8, 6, 3], [5, 8, 3, 7]]
Two sided fisher's exact test
p-value - R (MC): 0.5042     1.782
p-value - Rust (MC): 0.5041     1.117
"""
"""
[[8, 3, 5, 5, 6], [4, 3, 8, 6, 5], [2, 5, 3, 7, 6], [4, 8, 2, 3, 6]]
Two sided fisher's exact test
p-value - R (Analitical): 0.3935     1.028
p-value - R (MC): 0.3932     2.140
p-value - Rust (MC): 0.3934     1.175
"""
"""
[[8, 3, 9, 7], [8, 6, 6, 6], [6, 8, 6, 3]]
Two sided fisher's exact test
p-value - R (Analitical): 0.5823     0.039
p-value - Rust (Rec): 0.5823     5.007
p-value - Py (Rec) : 0.5823     21.053
p-value - R (MC): 0.5827     1.166
p-value - Rust (MC): 0.5828     0.803

KÉSZ    28.069625854492188
"""
"""
[[1, 0, 0, 0, 1], [1, 2, 0, 2, 1], [1, 0, 1, 2, 1], [1, 1, 1, 3, 1], [1, 2, 1, 1, 1]]
Two sided fisher's exact test
p-value - R (Analitical): 0.9912     0.040
p-value - Rust (analitical, R): 0.9912     0.001
p-value - R (MC): 0.9912     1.529
p-value - Rust (MC): 0.9912     1.605
"""
"""
[[11, 12, 18, 15], [15, 13, 13, 15], [15, 19, 19, 15]]
Two sided fisher's exact test
p-value - R (MC): 0.8816     1.776
p-value - Rust (MC): 0.8824     3.518
p-value - R (Analitical): 0.8822     3.605
p-value - Rust (analitical, R): 0.8257     0.004  !!!!!!!!
"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""


