from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.pts = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.pts[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        for (x, y), diagonal_count in self.pts.items():
            if (abs(px - x) != abs(py - y) or x == px or y == py):
                continue
            
            corner1_count = self.pts.get((x, py), 0)
            corner2_count = self.pts.get((px, y), 0)

            res += corner1_count * corner2_count * diagonal_count     
        
        return res 
        

        
