#!/usr/bin/python

import argparse

def find_max_profit(prices):
    # base case/initial max
    max_profit = prices[1] - prices[0]
    print(max_profit)

    # loop through all numbers
    for i in range(3, len(prices)+1):
        print(i)
        # create temp list
        temp_list = prices[:i]
        print(temp_list)

        # loop through temp_list, in reverse
        for x in range(1, len(temp_list), -1):
          profit = temp_list[-1] - temp_list[x-1]
          print(x, profit)
          if profit > max_profit:
            max_profit = profit
    
    return max_profit

l = [10, 7, 5, 8, 11, 9]
print(find_max_profit(l))