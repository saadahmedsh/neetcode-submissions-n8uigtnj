from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize:
            return False

        counts = Counter(hand)
        hand.sort()


        for h in hand:
            if counts[h]:
                for i in range(h, h + groupSize):
                    if not counts[i]:
                        return False
                    counts[i] -= 1

        return True

        
        