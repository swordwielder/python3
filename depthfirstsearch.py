class TapeReader(self):
    
    def ReadandAdvance(self):
        return num


    def hasMoreTape(self):

        return True/False


'''
2 5 6 1 7 3 4 
'''



class PeakReader(self, TapeReader):
    self.seen = []
    def peak(self):
        if len(self.seen) == 0:
            if self.hasMoreTape():
                seen.append(self.ReadandAdvance())
                return self.seen[0]
            else:
                return None
        else:
            return self.seen[0]
        
    def ReadandAdvance(self):
        if len(self.seen > 0):
            return self.seen.pop(0)
        else:
            return self.ReadandAdvance()


    def hasMoreTape(self):

        return True/False


if "__name__" == "__main__":
    pr = PeakReader( 2 5 6 1 7 3 4  )
    pr.peak()# 2
    pr.ReadandAdvance() # 5
    pr.ReadandAdvance() # 5

