import hashlib
import time
#class to handle blocks
class Block:
    #constant(s)
    one_min_to_sec = 60

    def __init__(self, index, prevHash, timestamp, data, currentHash):
        self.index = index
        self.prevHash = prevHash
        self.timestamp = timestamp
        self.data = data
        self.currentHash = currentHash

#create a genesis block
    def newGenesisBlock():
        #genesisAttributes
        genIndex = 0
        genPrevHash  = 0
        genTimestamp = time.time() - one_min_to_sec
        genData = 'genesis'
        genHashValue = this.newHash(genIndex,genPrevHash,genTimestamp,genData)
        return Block(genIndex,str(genPrevHash),genTimestamp,genData,genHashValue)

#generateHash
    def newHash(index, prevHash, timestamp, data):
        hashComp = str(index) + str(prevHash) + str(timestamp) + str(data)
        shaValue = hashlib.sha256(hashComp.encode('utf-8'))
        return str(shaValue.hexdigest())
