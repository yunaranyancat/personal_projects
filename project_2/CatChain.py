import hashlib
import time
import random

#constant(s)
one_min_to_sec = 60
ynChain = []

#create a Block object
class Block:
    def __init__(self, index, prevHash, timestamp, data, currentHash):
        self.index = index
        self.prevHash = prevHash
        self.timestamp = timestamp
        self.data = data
        self.currentHash = currentHash

    def __repr__(self):
        return self.currentHash

#create a genesis block
def newGenesisBlock():
    #genesisAttributes
    genIndex = 0
    genPrevHash  = 0
    genTimestamp = time.time() - one_min_to_sec
    genData = 'genesis'
    genHashValue = newHash(genIndex,genPrevHash,genTimestamp,genData)
    print("GenesisCat has been generated! : Meow!")
    return Block(genIndex,str(genPrevHash),genTimestamp,genData,genHashValue)

#generateHash
def newHash(index, prevHash, timestamp, data):
    hashComp = str(index) + str(prevHash) + str(timestamp) + str(data)
    shaValue = hashlib.sha256(hashComp.encode('utf-8'))
    return str(shaValue.hexdigest())

#generate hash for block object
def newHashBlock(block):
    return newHash(block.index, block.prevHash, block.timestamp, block.data, block.currentHash)

#get the last block of the chain
def getLastCurrentBlock(list_of_blocks):
    return list_of_blocks[len(list_of_blocks)-1]

#generate cat or no cat.
def generateCat():
    randomBinary = random.randint(0,1)
    if randomBinary==1:
        return "cat"
    else:
        return "no cat"

#generate new Block
def generateBlock(list_of_blocks):
    dataBlock = generateCat()
    lastBlock = getLastCurrentBlock(list_of_blocks)
    nextIndex = lastBlock.index + 1
    nextTimestamp = time.time()
    nextHash = newHash(nextIndex, lastBlock.currentHash, nextTimestamp,generateCat())
    return Block(nextIndex,lastBlock.currentHash,dataBlock,nextTimestamp,nextHash)

def validBlock(newBlock, lastValidBlock):
    if lastValidBlock.index + 1 != newBlock.index:
        print("Block Index Not Valid!")
        return False
    elif lastValidBlock.currentHash != newBlock.prevHash:
        print("Last Hash Does Not Match!")
        return False
    elif newHashBlock(newBlock) != newBlock.currentHash:
        print("Hash Do Not Match!")
        return False
    else:
        print("Valid Block!")
        return True







#TEST
#add genesis block into the list
ynChain.append(newGenesisBlock())
#print(ynChain)
block1 = generateBlock(ynChain)
print(block1)
