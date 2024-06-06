# import streamlit as st
# from rag import Data, RAG
# import os
# from utils import *

# temp_directory()
# # Streamlit UI
# st.image(
#     "dowjones.jpg", width=600, caption="POWERING THE PROFESSIONAL WORLD"
# )

# query_text = st.text_area("Enter your query:")

# if st.button("Submit Query"):
#     if query_text:
#         rag = RAG()
#         with st.spinner("Processing your query..."):
#             response_text = rag.query_rag(query_text)
#         st.write(response_text)
#     else:
#         st.error("Please enter a query text.")

import streamlit as st

# Define the function
def active_stocks_at_investor_times(stocks, investors):
    answer = []
    for investor_time in investors:
        count = 0
        for start, end in stocks:
            if start <= investor_time <= end:
                count += 1
        answer.append(count)
    return answer

# Problem statement
problem_statement = """
### Problem 3: Active Stock Trading Analysis Python Coding Challenge

**Scenario:**
You need to analyze the active trading periods of stocks and how they align with investor interest. This will help you gauge investor sentiment and predict market movements more accurately.

**Description:**
You are provided with a 0-indexed 2D integer array `stocks`, where `stocks[i] = [starti, endi]` signifies that the ith stock is actively traded from `starti` to `endi` (inclusive). Additionally, you have a 0-indexed integer array `investors` of size `n`, where `investors[i]` indicates the time that the ith investor arrives to check the active trades.

**Task:**
Return an integer array `answer` of size `n`, where `answer[i]` is the number of stocks that are actively traded when the ith investor arrives.

You Need to provide output as results of 5 Test Cases (Given below):

Example:

```python
# Input:
stocks = [[1,6], [3,7], [9,12], [4,13]]
investors = [2, 3, 7, 11]
# Output:
[1, 2, 2, 2]
```

**Explanation:**
For each investor, return the number of stocks that are actively traded during their arrival.

- Investor at time 2: 1 stock is active (stocks[0])
- Investor at time 3: 2 stocks are active (stocks[0], stocks[1])
- Investor at time 7: 2 stocks are active (stocks[1], stocks[3])
- Investor at time 11: 2 stocks are active (stocks[2], stocks[3])

"""

# Display the problem statement in Streamlit
st.markdown(problem_statement)

# Display the solution function as a code block
solution_code = """
```python
def active_stocks_at_investor_times(stocks, investors):
    answer = []
    for investor_time in investors:
        count = 0
        for start, end in stocks:
            if start <= investor_time <= end:
                count += 1
        answer.append(count)
    return answer
```
"""
st.markdown("### Solution Function")
st.code(solution_code)

# Test Cases
test_cases = [
    {"stocks": [[1, 4], [2, 3], [3, 5]], "investors": [2, 3, 5], "expected": [2, 3, 1]},
    {"stocks": [[1, 6], [3, 7], [9, 12], [4, 13]], "investors": [2, 3, 7, 11], "expected": [1, 2, 2, 2]},
    {"stocks": [[1, 10], [3, 3]], "investors": [3, 3, 2], "expected": [2, 2, 1]},
    {"stocks": [[5, 8], [6, 7], [8, 10]], "investors": [6, 9, 10, 5], "expected": [2, 1, 1, 1]},
    {"stocks": [[1, 2], [2, 3], [3, 4]], "investors": [1, 2, 3, 4], "expected": [1, 2, 2, 1]}
]

# Execute test cases and output the results
for idx, case in enumerate(test_cases):
    stocks = case["stocks"]
    investors = case["investors"]
    expected = case["expected"]
    result = active_stocks_at_investor_times(stocks, investors)
    
    st.write(f"**Test Case {idx + 1}**")
    st.write(f"**Input Stocks:** {stocks}")
    st.write(f"**Input Investors:** {investors}")
    st.write(f"**Expected Output:** {expected}")
    st.write(f"**Function Output:** {result}")
    st.write("----")
