import hashlib
import time
import CatChainv2 as CC

#set difficulty
difficulty = 5

#list to mine with genesis block
CatList = [CC.newGenesisBlock()]

#create a Block object with proof of work
class Block:
    def __init__(self, index, prevHash, timestamp, data, currentHash, proof):
        self.index = index
        self.prevHash = prevHash
        self.timestamp = timestamp
        self.data = data
        self.currentHash = currentHash
        self.proof = proof

    def __repr__(self):
        return self.currentHash

def mineNewCat(difficulty=difficulty,CatChain = CatList):
    CatChain = CatChain
    timestamp = time.time()
    proof = 0
    newCatFound = False
    print("Meowing a new block...")
    while not newCatFound:
        newCatAttempt = CC.generateBlock(CatList,proof)
        if newCatAttempt.currentHash[0:difficulty] == '0'*difficulty:
            stopTime = time.time()
            timer = stopTime - timestamp
            print("Meow! You just found me!.. with proof: ",proof," in ",round(timer, 2),' seconds.')

            newCatFound = True
        else:
            proof +=1
    CatChain.append(newCatAttempt)

def mine(catToMine = 10):
    for _ in range(catToMine):
        mineNewCat()

def showCatChain(chain = CatList):
    for i in chain:
        print(CatList)

mine()
showCatChain()
