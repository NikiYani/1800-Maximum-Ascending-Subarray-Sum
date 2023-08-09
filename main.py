class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max = 0
        localSum = 0

        for i in range(0, len(nums)) :
            if i == 0 :
                localSum += nums[i]
                continue

            if nums[i] > nums[i - 1] :
                localSum += nums[i]
                continue
            else :
                if max < localSum :
                    max = localSum

                localSum = 0
                localSum += nums[i]

        if max < localSum :
            max = localSum

        return max