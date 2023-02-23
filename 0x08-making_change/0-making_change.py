#!/usr/bin/python3
"""
Make changes
"""


def makeChange(coins, total):
    """ make changes """
    if total <= 0:
        return 0

    def combSum(candidates, target, index, cur, res):
        """ helper function """
        if target <= 0:
            if target == 0:
                res.append(cur[::])
            return
        if res:
            return
        for i in range(index, len(candidates)):
            val = candidates[i]
            cur.append(val)
            combSum(candidates, target - val, i, cur, res)
            last = cur.pop()
        return res
    res = combSum(sorted(list(set(coins)), reverse=True), total, 0, [], [])
    if res:
        return len(res[0])
    return -1
