class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}

        for num in nums:
            numbers[num] = numbers.get(num, 0) + 1

        output = []

        for num, freq in numbers.items():
            output.append([num, freq])

        output.sort(key=lambda x: x[1], reverse=True)

        result = []

        for i in range(k):
            result.append(output[i][0])

        return result