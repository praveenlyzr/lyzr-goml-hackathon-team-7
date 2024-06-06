def active_stocks_at_investor_times(stocks, investors):
    answer = []
    for investor_time in investors:
        count = 0
        for start, end in stocks:
            if start <= investor_time <= end:
                count += 1
        answer.append(count)
    return answer

# Test Case 1
stocks_1 = [[1, 4], [2, 3], [3, 5]]
investors_1 = [2, 3, 5]
print(active_stocks_at_investor_times(stocks_1, investors_1))  # Expected output: [2, 3, 1]

# Test Case 2
stocks_2 = [[1, 6], [3, 7], [9, 12], [4, 13]]
investors_2 = [2, 3, 7, 11]
print(active_stocks_at_investor_times(stocks_2, investors_2))  # Expected output: [1, 2, 2, 2]

# Test Case 3
stocks_3 = [[1, 10], [3, 3]]
investors_3 = [3, 3, 2]
print(active_stocks_at_investor_times(stocks_3, investors_3))  # Expected output: [2, 2, 1]

# Test Case 4
stocks_4 = [[5, 8], [6, 7], [8, 10]]
investors_4 = [6, 9, 10, 5]
print(active_stocks_at_investor_times(stocks_4, investors_4))  # Expected output: [2, 1, 1, 1]

# Test Case 5
stocks_5 = [[1, 2], [2, 3], [3, 4]]
investors_5 = [1, 2, 3, 4]
print(active_stocks_at_investor_times(stocks_5, investors_5))  # Expected output: [1, 2, 2, 1]