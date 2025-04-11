from functools import cache

n, m = map(int, input().split())

pa = {}
at = {}


for i in range(1, m + 1):
    v, w, q = map(int, input().split())
    if q == 0:
        pa[i] = [v, w]
        continue
    if q not in at:
        at[q] = [[v, w]]
    else:
        at[q].append([v, w])

    
idx = list(pa.keys())


@cache
def dfs(i, b):
    if i < 0:
        return 0
    res = dfs(i - 1, b)
    if b >= pa[idx[i]][0]:
        res = max(res, dfs(i - 1, b - pa[idx[i]][0]) + pa[idx[i]][0] * pa[idx[i]][1])
    if idx[i] in at and len(at[idx[i]]) == 1:
        if b >= pa[idx[i]][0] + at[idx[i]][0][0]:
            res = max(res, dfs(i - 1, b - pa[idx[i]][0] - at[idx[i]][0][0]) + pa[idx[i]][0] * pa[idx[i]][1] + at[idx[i]][0][0] * at[idx[i]][0][1])
        
    if idx[i] in at and len(at[idx[i]]) == 2:
        if b >= pa[idx[i]][0] + at[idx[i]][0][0]:
            res = max(res, dfs(i - 1, b - pa[idx[i]][0] - at[idx[i]][0][0]) + pa[idx[i]][0] * pa[idx[i]][1] + at[idx[i]][0][0] * at[idx[i]][0][1])
        if b >= pa[idx[i]][0] + at[idx[i]][1][0]:
            res = max(res, dfs(i - 1, b - pa[idx[i]][0] - at[idx[i]][1][0]) + pa[idx[i]][0] * pa[idx[i]][1] + at[idx[i]][1][0] * at[idx[i]][1][1])
        if b >= pa[idx[i]][0] + at[idx[i]][0][0] + at[idx[i]][1][0]:
            res = max(res, dfs(i - 1, b - pa[idx[i]][0] - at[idx[i]][0][0] - at[idx[i]][1][0]) + pa[idx[i]][0] * pa[idx[i]][1] + at[idx[i]][0][0] * at[idx[i]][0][1] + at[idx[i]][1][0] * at[idx[i]][1][1])
    return res

res = dfs(len(idx) - 1, n)

print(res)