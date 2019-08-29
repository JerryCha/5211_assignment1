import unittest
from operator import add
import random
random.seed(a=0)

class TestChangeFeasible(unittest.TestCase):
    def setUp(self):
      self.denominations = [1, 5, 10, 20, 100]
      self.multiplicities = []
    
    def checkFeasible(self, boolean, changes):
        if boolean:
            possible = "possible"
        else:
            possible = "impossible"
        msg = "it should be {} to give the change {} given multiplicities {}.".format(possible, changes, self.multiplicities)
        self.assertEqual(boolean, change_feasible(self.denominations, self.multiplicities, changes), msg)
        
    def testEmpty(self):
        self.multiplicities = [0, 0, 0, 0, 0]
        self.checkFeasible(True, [])
        self.checkFeasible(True, [0])
        self.checkFeasible(False, [1])
        self.checkFeasible(False, [1, 2, 5])
        
    def testSingle(self):
        for i in range(len(self.denominations)):
            self.multiplicities = [0, 0, 0, 0, 0]
            self.multiplicities[i] = 1
            self.checkFeasible(True, [self.denominations[i]])
            self.checkFeasible(False, [2*self.denominations[i]])

    def testMultiple(self):
        constant = 10
        for i in range(len(self.denominations)):
            self.multiplicities = [0, 0, 0, 0, 0]
            self.multiplicities[i] = constant
            for mult in range(constant+1):
                self.checkFeasible(True, [mult*self.denominations[i]])
            self.checkFeasible(False, [(constant+1)*self.denominations[i]])
            
    def generateChangeAndMults(self, denomination_mask, max_multiple = 10):
        change = 0
        change_multiplicities = []
        for i in range(len(self.denominations)):
            mult = 0
            if denomination_mask[i]:
                mult = random.randint(1, max_multiple)
                change += mult * self.denominations[i]
            change_multiplicities.append(mult)
        return change, change_multiplicities
                
            
    def makeSingleChange(self):
        max_different_denominations = random.randint(1, len(self.denominations))
        which_denominations = random.sample(self.denominations, max_different_denominations)
        which_denominations.sort()
        
        denomination_mask = []
        for denom in self.denominations:
            denomination_mask.append(denom in which_denominations)
            
        return self.generateChangeAndMults(denomination_mask)

    def testSingleChange(self):
        number_tests = 100
        for _ in range(number_tests):
            change, change_multiplicities = self.makeSingleChange()
            self.multiplicities = change_multiplicities
            self.checkFeasible(True, [change])
            self.checkFeasible(False, [change+1])
            
    def testMultipleChange(self):
        max_test_size = 100
        for test_size in range(1, max_test_size):
            changes = []
            self.multiplicities = [0, 0, 0, 0, 0]
            for _ in range(test_size):
                change, change_multiplicities = self.makeSingleChange()
                changes.append(change)
                self.multiplicities = list(map(add, self.multiplicities, change_multiplicities))
                
            random.shuffle(changes)
            self.checkFeasible(True, changes)
            changes[0] += random.sample(self.denominations, 1)[0]
            self.checkFeasible(False, changes)

def change_feasible(denominations, multiplicities, change_amounts):
    assert len(denominations) == len(multiplicities)
    
    #we make local copies so we can change these lists within the function
    multiplicities = multiplicities.copy()
    change_amounts = change_amounts.copy()
    
    # DONE
    k = len(denominations)
    for change in change_amounts:
        for i in range(k-1, -1, -1):
            if change > 0:
                if multiplicities[i] > 0 and denominations[i] <= change:
                    numOfDomina = change//denominations[i]
                    if numOfDomina <= multiplicities[i]:
                        multiplicities[i] -= numOfDomina
                    else:
                        numOfDomina = multiplicities[i]
                        multiplicities[i] = 0
                    change = change - denominations[i]*numOfDomina
        if change > 0:
            return False
    return True

testlist = TestChangeFeasible()
suite = unittest.TestLoader().loadTestsFromModule(testlist)
unittest.TextTestRunner().run(suite)