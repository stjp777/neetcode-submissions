from typing import List

# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value


class Solution:

    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        b_arr = []

        for i in range(len(pairs)):
            j = i
            # Shift the current element left until it is in its sorted position
            while j > 0 and pairs[j].key < pairs[j - 1].key:
                pairs[j], pairs[j - 1] = pairs[j - 1], pairs[j]
                j -= 1

            # Snapshot the state of the list at this stage
            b_arr.append(pairs.copy())

        return b_arr