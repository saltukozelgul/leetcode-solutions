import itertools

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Beats %95.52 Runtime: 826ms

        # We have to split negatives and positives and also zeros
        solution =  set()

        pos, neg , zeros = [], [], []
        for num in nums:
            if num > 0:
                pos.append(num)
            elif num < 0:
                neg.append(num)
            else:
                zeros.append(num)

        #sort the lists
        pos.sort()
        neg.sort()

        # For avoid duplicates and make the search faster
        P, N = set(pos), set(neg)

        # For solutions that have 0 zero and 1 negative and 1 positive
        if zeros:
            for p in P:
                if -p in N:
                    solution.add((p,0,-p))

        # I dont set zeros because we will check zeros count 
        if len(zeros) >= 3:
             solution.add((0,0,0))

        ## For solutions that have 2 negative and 1 positive
        for i in range(len(neg)):
            for j in range(i+1,len(neg)):
                target = -(neg[i] + neg[j])
                if target in P:
                    # Pay attention to sorting while adding so we have to insert ith index first.
                    solution.add((neg[i],neg[j],target))
        
        ## For solutions that have 2 positive and 1 negative
        for i in range(len(pos)):
            for j in range(i+1,len(pos)):
                target = -(pos[i]+ pos[j])
                if target in N:
                    solution.add((target,pos[j],pos[i]))
    
        return set(solution)

            
