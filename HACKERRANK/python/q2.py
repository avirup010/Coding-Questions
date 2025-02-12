"""
Task
The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

The first line contains the sum of two numbers.
The second line contains the difference of the two numbers (first – second).
The third line contains the product of two numbers. 
Example

a = 3

b = 5

Print the following:

8
-2
15
Input Format
The first line contains the first integer, a.
The second line contains the second integer, b.

Constraints
1 ≤ a ≤ 1010
1 ≤ b ≤ 1010

Output Format
Print the three lines as explained above.

Sample Input 0

3
2
Sample Output 0

5
1
6
Explanation 0

3 + 2 ➡️ 5
3 – 2 ➡️ 1
3 * 2 ➡️ 6
"""
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)
