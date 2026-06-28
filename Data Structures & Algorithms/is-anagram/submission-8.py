class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMapS = {}
        hashMapT = {}

        for letter in s:
            if hashMapS.get(letter):
                hashMapS[letter] += 1
            else:
                hashMapS[letter] = 1

        for letter in t:
            if hashMapT.get(letter):
                hashMapT[letter] += 1
            else:
                hashMapT[letter] = 1

        print(hashMapS, hashMapT)
        mismatches = hashMapS.items() ^ hashMapT.items()
        return len(mismatches) == 0
        