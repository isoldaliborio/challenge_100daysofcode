class Solution:
    def containsDuplicate(self, nums):
        hashset = set() # set() é um conjunto vazio -  é igual a lista, de items únicos (não pode ter duplicado) e não respeita ordem, a posição é irrelevante.
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        return False
        # for i, num in enumerate(nums): #create tuples (position, value)
        #     for x in nums[i+1:]: #slicing from position i+1
        #         if x == num:
        #             return True
        # return False

solution = Solution()

lst = [1, 2, 3, 1]
has_duplicate = solution.containsDuplicate(lst)
print(has_duplicate)


