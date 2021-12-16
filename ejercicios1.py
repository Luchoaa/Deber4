from typing import List

class Islas:
    def busProf(self, r, c, grid, m, n):

        for sop in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            sigR = r+sop[0];
            sigC = c+sop[1];

            if 0<=sigR<m and 0<=sigC<n and grid[sigR][sigC]=='1':
                grid[sigR][sigC] = '0';
                self.busProf(sigR, sigC, grid, m, n);
        
    def cantIslas(self, grid: List[List[str]]):
        m = len(grid);
        n = len(grid[0]);
        numIsl = 0;

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    numIsl += 1;
                    self.busProf(i, j, grid, m, n);
        return numIsl;

vr = Islas();
print(vr.cantIslas([["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]]));