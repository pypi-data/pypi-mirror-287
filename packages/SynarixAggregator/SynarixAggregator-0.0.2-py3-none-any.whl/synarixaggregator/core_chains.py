
class chains:
    def __init__(self, chainID):
        self.RixSwapAggregator = None
        self.RixFeeUtils = None
        self.ZERO = "0x0000000000000000000000000000000000000000"  # This is constant across all chains
        self.WETH = None
        self.RIX = None

        if int(chainID) == 56:
            self.RixSwapAggregator = "0xa88EE4962D365535aa02e60E93f1C10F51DFd5EA"
            self.RIX = "0x0717462a4294a753A35072ED9ceB268599030959"
            self.WETH = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
            self.chainID = 56

        elif int(chainID) == 31337: #Local Hardhat fork for testing 
            self.RixSwapAggregator = "0xa88EE4962D365535aa02e60E93f1C10F51DFd5EA"
            self.RIX = "0x0717462a4294a753A35072ED9ceB268599030959"
            self.WETH = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
            self.chainID = 31337

        else:
            raise SystemExit(f"ChainID {chainID} currently not Supported!")

