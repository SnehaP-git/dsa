"""
Problem: Merge Strings Alternately
LeetCode: https://leetcode.com/problems/merge-strings-alternately/

You are given two strings word1 and word2. 
Merge them by adding letters in alternating order, starting with word1. 
If a string is longer, append the remaining letters.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
"""

def mergeAlternately(word1: str, word2: str) -> str:
    merged = []
    i, j = 0, 0
    while i < len(word1) and j < len(word2):
        merged.append(word1[i])
        merged.append(word2[j])
        i += 1
        j += 1 
    merged.extend(word1[i:])
    merged.extend(word2[j:])
    return "".join(merged)


# 🔹 Test Cases
if __name__ == "__main__":
    print(mergeAlternately("abc", "pqr"))   # "apbqcr"
    print(mergeAlternately("ab", "pqrs"))   # "apbqrs"
    print(mergeAlternately("abcd", "pq"))   # "apbqcd"

