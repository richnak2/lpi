import os

import os.path
import sys
sys.path[0:0] = [os.path.join(sys.path[0], '../../examples/sat')]

import sat

class SudokuSolver:
    def __init__(self):
        pass
    def solve(self,zoz):
        def p(x, y, z):
            return (((x - 1) * 9) + (y - 1)) * 9 + z
        def s(x, y, z):
            return 81 * (x - 1) + 9 * (y - 1) + z
        
        satsolver = sat.SatSolver()
        vstup = sat.DimacsWriter('vstup.txt')

    
        
        for x in range(len(zoz)):
            for y in range(len(zoz)):
                if zoz[x][y] != 0:
                    vstup.writeLiteral(s(x+1, y+1, zoz[x][y]))
                    vstup.finishClause()

        for x in range(1, 10):
            for y in range(1, 10):
                for z in range(1, 10):
                     vstup.writeLiteral(s(x, y, z))
                vstup.finishClause()

        for y in range(1, 10):
            for z in range(1, 10):
                for x in range(1, 9):
                    for i in range(x + 1, 10):
                        string = f"{-s(x, y, z)} {-s(i, y, z)}"
                        vstup.writeLiteral(string)
                        vstup.finishClause()

        for x in range(1, 10):
            for z in range(1, 10):
                for y in range(1, 9):
                    for i in range(y + 1, 10):
                         string = f"{-s(x, y, z)} {-s(x, i, z)}"
                         vstup.writeLiteral(string)
                         vstup.finishClause()

        for z in range(1, 10):
            for i in range(0, 3):
                for j in range(0, 3):
                    for x in range(1, 4):
                        for y in range(1, 4):
                            for k in range(y + 1, 4):
                                string = f"{-s(3 * i + x, 3 * j + y, z)} {-s(3 * i + x, 3 * j + k, z)}"
                                vstup.writeLiteral(string)
                                vstup.finishClause()

        for z in range(1, 10):
            for i in range(0, 3):
                for j in range(0, 3):
                    for x in range(1, 4):
                        for y in range(1, 4):
                            for k in range(x + 1, 4):
                                for l in range(1, 4):
                                    string = f"{-s(3 * i + x, 3 * j + y, z)} {-s(3 * i + k, 3 * j + l, z)}"
                                    vstup.writeLiteral(string)
                                    vstup.finishClause()

        vstup.close()

        dobre, riesenie = satsolver.solve(vstup, 'vystup.txt')
        
        if dobre:
            final = []
            for i in range(1, 10):
                zoz = []
                for j in range(1, 10):
                    for k in range(1, 10):
                        if p(i, j, k) in riesenie:
                            zoz.append(k)

                final.append(zoz)

            return final

        else:
            self.pole = [[0]*9]*9

        return self.pole


