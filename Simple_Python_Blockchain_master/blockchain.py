import datetime
import hashlib

class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0 # Number used only Once
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

# Developing the block's hash
    def hash(self):

        # The block header 
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

# Output expected
    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"


# This class is consernde with the connection of blocks
class Blockchain:

    diff = 20 # Dictates the gas needed to create a new block ( how much work the miners nned to create a valid block.)
    maxNonce = 2**32
    target = 2 ** (256-diff)

    block = Block("Genesis")
    dummy = head = block

# When adding a new block this should happen

    def add(self, block): 

        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

# Deterimne a block's nonce (in this case hashes)
    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

blockchain = Blockchain()

# The number of blocks to be mined
for n in range(10):
    blockchain.mine(Block("Block " + str(n+1)))


while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next
