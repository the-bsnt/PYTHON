# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())


def check_regex(regex):
    try:
        re.compile(regex)
        return True
    except re.error:
        return False


regex_list = []
for i in range(n):
    regex_list.append(input())
for i in regex_list:
    print(check_regex(i))


r"""
You are given a string .
Your task is to find out whether  is a valid regex or not.


Sample Input

2
.*\+
.*+
Sample Output

True
False
Explanation

.*\+ : Valid regex.
.*+: Has the error multiple repeat. Hence, it is invalid."""
