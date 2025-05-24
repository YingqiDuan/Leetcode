class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=prices[0]
        res=0
        for p in prices:
            res=max(res,p-b)
            if p<b:
                b=p
        return res


############################################################
# Solution.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2022
###########################################################
############################################################
# All imports
###########################################################
from typing import List


class Solution:
    def __init__(self):
        pass
        ## YoU can have what ever you want here
        

    ##LEETCODE INTERFACE.  DO NOT CHANGE
    ## YOU CANNOT CHANGE ANYTHING
    def maxProfit(self, prices: List[int]) -> int:
        if False:
            [sellday, buyday, work] = self.nsquare_time_constant_space(prices)
        if False:
            [sellday, buyday, work] = self.nlogn_time_logn_space(prices)
        if True:
            [sellday, buyday, work] = self.ntime_constant_space(prices)
        p = self._compute_profit(prices, sellday, buyday)
        return p

    #############################################
    # All public function here. 
    #############################################

    ########################################
    # TIME:THETA(N^2)
    # Space:THETA(1)
    # CANNOT CHANGE ANYTHING BELOW
    #########################################
    def nsquare_time_constant_space(self, a: List[int]) -> "[sellday,buyday,work]":
        return self._nsquare_time_constant_space(a) 


    ########################################
    # TIME:THETA(NlogN)
    # Space:THETA(logn)
    # CANNOT CHANGE ANYTHING BELOW
    #########################################
    def nlogn_time_logn_space(self, a: List[int]) -> "[sellday,buyday,work]":
        return self._nlogn_time_logn_space(a)

    ########################################
    # TIME:THETA(N)
    # Space:THETA(1)
    # CANNOT CHANGE ANYTHING BELOW
    #########################################
    def ntime_constant_space(self, a: List[int]) -> "[sellday,buyday,work]":
        return self._ntime_constant_space(a)
        

    #############################################
    # All private function here. 
    # WRIYE CODE BELOW
    # You can have any number of private functions and variables
    # NOTHING CAN BE CHABGED BELOW
    #############################################
    def _compute_profit(self, a: List[int], s: "int", b: "int") -> "int":
        n = len(a)
        if n == 0:
            return 0
        assert s >= 0 and s < n
        assert b >= 0 and b < n
        assert s >= b
        p = a[s] - a[b]
        return p
    
    def _nsquare_time_constant_space(self, a: List[int]) -> "[sellday,buyday,work]":
        n = len(a)
        work = 0
        best = 0
        buyday = 0
        sellday = 0
        for b in range(n):
            for s in range(b, n):
                work += 1
                profit = a[s] - a[b]
                if profit > best:
                    best = profit
                    buyday = b
                    sellday = s
        return [sellday, buyday, work]
    
    def _ntime_constant_space(self, a: List[int]) -> "[sellday,buyday,work]":
        n=len(a)
        if n==0:
            return [0,0,0]
        work=0
        idx=0
        best=0
        buyday=0
        sellday=0

        for i in range(n):
            work+=1
            if a[i]<a[idx]:
                idx=i
            profit=a[i]-a[idx]
            if profit>best:
                best=profit
                buyday=idx
                sellday=i
        return [sellday,buyday,work]
    
    def _nlogn_time_logn_space(self, a: List[int]) -> "[sellday,buyday,work]":
        n=len(a)
        if n<2:
            return [0,0,0]
        diff = [a[i+1] - a[i] for i in range(n-1)]
        work_diff = len(diff)

        def maxSubarray(diff: List[int], low: int, high: int):
            if low == high:
                w = 1
                if diff[low] > 0:
                    return (diff[low], low, low, w)
                else:
                    return (0, low, low, w)
            mid = (low + high) // 2
            l_sum, l_start, l_end, w_left = maxSubarray(diff, low, mid)
            r_sum, r_start, r_end, w_right = maxSubarray(diff, mid+1, high)
            sum = 0
            l_max_sum = float('-inf')
            best_l_i = mid
            w_cross = 0
            for i in range(mid, low - 1, -1):
                sum += diff[i]
                w_cross += 1  
                if sum > l_max_sum:
                    l_max_sum = sum
                    best_l_i = i
            sum = 0
            r_max_sum = float('-inf')
            best_r_i = mid + 1
            for j in range(mid+1, high+1):
                sum += diff[j]
                w_cross += 1
                if sum > r_max_sum:
                    r_max_sum = sum
                    best_r_i = j
            cross_sum = l_max_sum + r_max_sum
            w_total = w_left + w_right + w_cross + 2  
            if l_sum >= r_sum and l_sum >= cross_sum:
                return (l_sum, l_start, l_end, w_total)
            elif r_sum >= l_sum and r_sum >= cross_sum:
                return (r_sum, r_start, r_end, w_total)
            else:
                return (cross_sum, best_l_i, best_r_i, w_total)
        
        max_sum, start_index, end_index, work_rec = maxSubarray(diff, 0, len(diff)-1)
        work = work_diff + work_rec
        if max_sum > 0:
            buyday = start_index
            sellday = end_index + 1
        else:
            buyday = 0
            sellday = 0
        return [sellday, buyday, work]