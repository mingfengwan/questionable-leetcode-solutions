class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def generate_combinations(a, b):
            s = {a-b, a+b, a*b, b-a}
            if a != 0:
                s.add(b/a)
            if b != 0:
                s.add(a/b)
            return s
        
        n = len(cards)
        if n == 2:
            for v in generate_combinations(cards[0], cards[1]):
                if abs(v - 24.0) < 0.1:
                    return True
        else:
            for i in range(n-1):
                for j in range(i+1, n):
                    for v in generate_combinations(cards[i], cards[j]):
                        if self.judgePoint24(cards[:i] + cards[i+1:j] + cards[j+1:] + [v]):
                            return True

        return False
