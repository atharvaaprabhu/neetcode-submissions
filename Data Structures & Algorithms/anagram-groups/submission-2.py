class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        count = {}
        for i in strs :
            temp = "".join(sorted(i))
            count[temp] = 1 + count.get(temp,0)
        for i in count :
            print(i)
            tempo = []
            for j in strs :
                if i == "".join(sorted(j)) :
                    tempo.append(j)
            res.append(tempo)
        return res