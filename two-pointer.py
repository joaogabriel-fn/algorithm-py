#Leetcode 557

class Solution:
  def reverseWords_manual(s): # O(n)
    res = ''
    l, r = 0, 0

    while r < len(s):
      if s[r] != ' ':
        r += 1
      else:
        res += s[l:r+1][::-1]
        r += 1
        l = r

    res += ' '
    res += s[l:r+2][::-1]
    return res[1:]
  

string = "Let's take LeetCode contest"

print(Solution.reverseWords_manual(string))