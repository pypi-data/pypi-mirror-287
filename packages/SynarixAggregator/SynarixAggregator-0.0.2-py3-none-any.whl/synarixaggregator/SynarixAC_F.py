from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_abi import abi
from .core_abis import RixAggregator_ABI
from .core_chains import chains
import time


class InterfaceAggregatorContract: #IAC
    
    def __init__(self, settings, w3, IERC20, w3U):
        self.settings, self.user_address, self.priv_key, self.w3, self.IERC20, self.w3U = settings, settings.settings["address"], settings.settings["private_key"], w3, IERC20, w3U
        self.chain = chains(self.w3.eth.chain_id)
        self.RixSwapAggregator = self.initRouter()

    def initRouter(self):
        RixSwapAggregator = self.w3.eth.contract(
            address=self.chain.RixSwapAggregator, abi=RixAggregator_ABI)
        return RixSwapAggregator
    
    def getAmountsOutV3(self, pools, path, amountIn):
        return self.RixSwapAggregator.functions.getAmountsOutV3(
            pools, path, amountIn
            ).call()
    
    def getAmountsOutV2(self, amountIn, path, dexPath):
        return self.RixSwapAggregator.functions.getAmountsOutV2(
            amountIn, path, dexPath
            ).call()
    
    def getUSDPrice_(self):
        return self.RixSwapAggregator.functions.getUSDPrice(
            self.IERC20.get_token_address()
            ).call()
        
    def getUSDPrice(self):
        return Web3.from_wei(self.RixSwapAggregator.functions.getUSDPrice(
            self.IERC20.get_token_address()
            ).call(), "ether")
    
    
    def getUSDPriceOf(self, tokenAddress):
        return Web3.from_wei(self.RixSwapAggregator.functions.getUSDPrice(
            self.w3.to_checksum_address(tokenAddress)
            ).call(), "ether")
    
    def getUSDPriceOf_(self, tokenAddress):
        return self.RixSwapAggregator.functions.getUSDPrice(
            self.w3.to_checksum_address(tokenAddress)
            ).call()
    
        
    def getWBNBPrice_(self):
        return self.RixSwapAggregator.functions.getUSDPrice(
            self.chain.WETH).call()
        
    def getWBNBPrice(self):
        return Web3.from_wei(self.RixSwapAggregator.functions.getUSDPrice(
            self.chain.WETH).call(), "ether")
    
    def getAmountsOutTokenToBNB_(self, inputAmount:int):
        return self.RixSwapAggregator.functions.getAmountsOut(
            self.IERC20.get_token_address(),
            self.chain.WETH,
            inputAmount
        ).call()

    def getAmountsOutBNBToToken_(self, inputAmount:int):
        return self.RixSwapAggregator.functions.getAmountsOut(
            self.chain.WETH,
            self.IERC20.get_token_address(),
            inputAmount
        ).call()
    
    def getAmountsOutTokenToToken_(self, tokenIn, tokenOut, inputAmount:int):
        return self.RixSwapAggregator.functions.getAmountsOut(
            Web3.to_checksum_address(tokenIn),
            Web3.to_checksum_address(tokenOut),
            inputAmount
        ).call()
    
    def getLiquidityUSD_(self, isTokenIn:bool=True):
        return self.RixSwapAggregator.functions.getLiquidity(
            self.IERC20.get_token_address(),
            isTokenIn
        ).call()
        
    def getLiquidityUSD(self, isTokenIn:bool=True):
        return self.w3U.from_wei(
            self.RixSwapAggregator.functions.getLiquidity(
            self.IERC20.get_token_address(),
            isTokenIn
        ).call(), 18)

    def getSwapProtocollVersion(self):
        return self.RixSwapAggregator.functions.checkVersion(self.IERC20.get_token_address()).call()

    def getTokenInfos(self):
        function_signature = self.RixSwapAggregator.encodeABI(fn_name="getTokenInfos", args=[self.IERC20.get_token_address()])
        data = {
            "to": self.RixSwapAggregator.address,
            "data": function_signature,
            "from": self.chain.ZERO
        }
        _data = self.w3.eth.call(data)
        call = abi.decode(
            ['uint256', 'uint256', 'uint256', 'uint256', 'bool', 'bool', 'bool', 'bool', 'string'],
            _data
        )
        buy_tax = round(
            ((call[0] - call[1]) / (call[0]) * 100) - 1, 3)
        sell_tax = round(
            ((call[2] - call[3]) / (call[2]) * 100) - 1, 3)

        if call[4] and call[5] and call[6] and call[7] == True:
            honeypot = False
        else:
            honeypot = True
        return buy_tax, sell_tax, honeypot
    
    def getWalletTokenDATA(self, tokenList):
        tokenList = [Web3.to_checksum_address(address) for address in tokenList]
        tokenBalances ,tokenDecimals ,tokenPrice ,tokensVersion ,tokenAddress = self.RixSwapAggregator.functions.getWalletTokenDATA(self.user_address, tokenList).call()
        return tokenBalances ,tokenDecimals ,tokenPrice ,tokensVersion ,tokenAddress
    
    def getETHtoTokenPathV3(self):
        return self.RixSwapAggregator.functions.getSwapPathV3(self.chain.WETH, self.IERC20.get_token_address()).call()
    
    def getTokentoETHPathV3(self):
        return self.RixSwapAggregator.functions.getSwapPathV3(self.IERC20.get_token_address(),self.chain.WETH).call()
        
    def getTokentoTokenPathV3(self, tokenIn, tokenOut):
        return self.RixSwapAggregator.functions.getSwapPathV3(
                Web3.to_checksum_address(tokenIn),
                Web3.to_checksum_address(tokenOut)
            ).call()
    
    
    def getETHtoTokenPathV2(self):
        return self.RixSwapAggregator.functions.getSwapPathV2(self.chain.WETH, self.IERC20.get_token_address()).call()
    
    def getTokentoETHPathV2(self):
        return self.RixSwapAggregator.functions.getSwapPathV2(self.IERC20.get_token_address(),self.chain.WETH).call()
        
    def getTokentoTokenPathV2(self, tokenIn, tokenOut):
        return self.RixSwapAggregator.functions.getSwapPathV2(
                Web3.to_checksum_address(tokenIn),
                Web3.to_checksum_address(tokenOut)
            ).call()
    
    def getBNBBalance_(self):
        return self.w3.eth.get_balance(self.user_address)
    
    def getBNBBalance(self):
        return self.w3.from_wei(self.w3.eth.get_balance(self.user_address), "ether")
    
    def getBNBBalanceOf_(self, address):
        return self.w3.eth.get_balance(address)
    
    def getBNBBalanceOf(self, address):
        return self.w3.from_wei(self.w3.eth.get_balance(address), "ether")

    def TestSwapETHtoToken(self, inputAmount: float):
        try:
            v = self.getSwapProtocollVersion()
            inputBNB = self.w3U.to_wei(inputAmount, 18)
            if int(v) == 2:
                try:
                    if self.TestSwapFromETHtoTokenV2(inputBNB):
                        return True
                except ValueError as e:
                    if 'message' in str(e):
                        if  'insufficient funds for transfer' in str(e):
                            print("")
                            print("ERROR:", "insufficient BNB funds for transaction!")
                            print("Exiting Now")
                            raise SystemExit
                        
            elif int(v) == 3:
               try:
                    if self.TestSwapFromETHtoTokenV3(inputBNB):
                         return True
               except ValueError as e:
                    if 'message' in str(e):
                        if  'insufficient funds for transfer' in str(e):
                            print("")
                            print("ERROR:", "insufficient BNB funds for transaction!")
                            print("Exiting Now")
                            raise SystemExit

        except Exception as e:
            print(e)
            return False


    def TestSwapFromETHtoTokenV2(self, inputAmount: int):
        path, dexIdents  = self.getETHtoTokenPathV2()
        amountOut = self.getAmountsOutV2(inputAmount, path, dexIdents)[-1]
        amountOutMinimum = int(amountOut - (amountOut * int(self.settings.settings["Slippage"])) / 100)
        txn = self.RixSwapAggregator.functions.swapETHtoTokenV2(
                path,
                dexIdents,
                amountOutMinimum
        ).build_transaction({
                    'from': self.user_address,
                    'gasPrice': self.w3.eth.gas_price + Web3.to_wei(int(self.settings.settings["GWEI_OFFSET"]) ,"gwei"),
                    'nonce': self.w3.eth.get_transaction_count(self.user_address),
                    'value': int(inputAmount)
        })
        return True


    def TestSwapFromETHtoTokenV3(self, inputAmount: int):
        path, _, pools, poolFees = self.getETHtoTokenPathV3()
        amountOut = self.getAmountsOutV3(pools, path, inputAmount)[-1]
        minOutput = int(amountOut - (amountOut * int(self.settings.settings["Slippage"])) / 100)
        txn = self.RixSwapAggregator.functions.swapETHtoTokenV3(
            path,
            pools,
            poolFees,
            minOutput
        ).build_transaction({
                'from': self.user_address,
                'gasPrice': int(self.w3.eth.gas_price + Web3.to_wei(int(self.settings.settings["GWEI_OFFSET"]), "gwei")),
                'nonce': self.w3.eth.get_transaction_count(self.user_address),
                'value': int(inputAmount)
        })
        return True
    

    def SwapETHtoToken(self, inputAmount: float, trys: int):
        while trys:
            try:
                v = self.getSwapProtocollVersion()
                inputBNB = self.w3U.to_wei(inputAmount, 18)
                if int(v) == 2:
                    return self.SwapFromETHtoTokenV2(inputBNB)
                elif int(v) == 3:
                    return self.SwapFromETHtoTokenV3(inputBNB)
            except Exception as e:
                print(e)
                trys -= 1
                time.sleep(1)
                if trys == 0:
                    return False, "0", e

    def SwapFromETHtoTokenV2(self, inputAmount: int):
        path, dexIdents  = self.getETHtoTokenPathV2()
        amountOut = self.getAmountsOutV2(inputAmount, path, dexIdents)[-1]
        amountOutMinimum = int(amountOut - (amountOut * int(self.settings.settings["Slippage"])) / 100)
        txn = self.RixSwapAggregator.functions.swapETHtoTokenV2(
            path,
            dexIdents,
            amountOutMinimum
        ).build_transaction({
            'from': self.user_address,
             'gasPrice': self.w3.eth.gas_price + Web3.to_wei(int(self.settings.settings["GWEI_OFFSET"]) ,"gwei"),
             'nonce': self.w3.eth.get_transaction_count(self.user_address),
             'value': int(inputAmount)
        })
        gas = self.w3U.estimateGas(txn)
        txn.update({'gas': gas[0]})
        signed_txn = self.w3.eth.account.sign_transaction(
            txn,
            self.priv_key
        )
        txn = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        txn_receipt = self.w3.eth.wait_for_transaction_receipt(
            txn, timeout=self.settings.settings["timeout"])
        if txn_receipt["status"] == 1:
            return True, txn.hex(), gas
        else:
            return False, txn.hex(), gas
                



    def SwapFromETHtoTokenV3(self, inputAmount: int):
        path, dexIdents, pools, poolFees = self.getETHtoTokenPathV3()
        amountOut = self.getAmountsOutV3(pools, path, inputAmount)[-1]
        minOutput = int(amountOut - (amountOut * int(self.settings.settings["Slippage"])) / 100)
        txn = self.RixSwapAggregator.functions.swapETHtoTokenV3(
            path,
            pools,
            poolFees,
            minOutput
        ).build_transaction({
            'from': self.user_address,
            'gasPrice': int(self.w3.eth.gas_price + Web3.to_wei(int(self.settings.settings["GWEI_OFFSET"]), "gwei")),
            'nonce': self.w3.eth.get_transaction_count(self.user_address),
            'value': int(inputAmount)
        })
        gas = self.w3U.estimateGas(txn)
        txn.update({'gas': gas[0]})
        signed_txn = self.w3.eth.account.sign_transaction(
            txn,
            self.priv_key
        )
        txn = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        txn_receipt = self.w3.eth.wait_for_transaction_receipt(
            txn, timeout=self.settings.settings["timeout"])
        if txn_receipt["status"] == 1:
            return True, txn.hex(), gas
        else:
            return False, txn.hex(), gas




    def SwapTokentoETH(self, inputAmount: float, trys: int = 1):
        while trys:
            try:
                v = self.getSwapProtocollVersion()
                inputToken = self.w3U.to_wei(inputAmount, self.IERC20.get_token_decimals())
                if int(v) == 2:
                    return self.SwapFromTokentoETHV2(inputToken)
                elif int(v) == 3:
                    return self.SwapFromTokentoETHV3(inputToken)
            except Exception as e:
                #print(e)
                trys -= 1
                time.sleep(1)
                if trys == 0:
                    return False, "0", e
        


    def SwapFromTokentoETHV3(self, inputAmount: int,):
        path, _, pools, poolFees = self.getTokentoETHPathV3()
        amountOut = self.getAmountsOutV3(pools, path, inputAmount)[-1]
        amountOutMinimum = int(amountOut - (amountOut * int(self.settings.settings["Slippage"])) / 100)
        txn = self.RixSwapAggregator.functions.swapTokenToETHV3(
            path,
            pools,
            poolFees,
            inputAmount,
            amountOutMinimum
        ).build_transaction({
            'from': self.user_address,
            'gasPrice': self.w3.eth.gas_price + Web3.to_wei(int(self.settings.settings["GWEI_OFFSET"]),"gwei"),
            'nonce': self.w3.eth.get_transaction_count(self.user_address),
            'value': 0
        })
        gas = self.w3U.estimateGas(txn)
        txn.update({'gas': gas[0]})
        signed_txn = self.w3.eth.account.sign_transaction(
            txn,
            self.priv_key
        )
        txn = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        txn_receipt = self.w3.eth.wait_for_transaction_receipt(
            txn, timeout=self.settings.settings["timeout"])
        if txn_receipt["status"] == 1:
            return True, txn.hex(), gas
        else:
            return False, txn.hex(), gas



    def SwapFromTokentoTokenV3(self, tokenIn, tokenOut, inputAmount: int):
        path, dexIdents, pools, poolFees = self.getTokentoTokenPathV3(tokenIn, tokenOut)
        amountOut = self.getAmountsOutV3(pools, path, inputAmount)[-1]
        amountOutMinimum = int(amountOut - (amountOut * int(self.settings.settings["Slippage"])) / 100)
        txn = self.RixSwapAggregator.functions.swapTokentoTokenV3(
            path,
            pools,
            poolFees,
            inputAmount,
            amountOutMinimum
        ).build_transaction({
            'from': self.user_address,
            'gasPrice': self.w3.eth.gas_price + Web3.to_wei(int(self.settings.settings["GWEI_OFFSET"]),"gwei"),
            'nonce': self.w3.eth.get_transaction_count(self.user_address),
            'value': 0
        })
        gas = self.w3U.estimateGas(txn)
        txn.update({'gas': gas[0]})
        signed_txn = self.w3.eth.account.sign_transaction(
            txn,
            self.priv_key
        )
        txn = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        txn_receipt = self.w3.eth.wait_for_transaction_receipt(
            txn, timeout=self.settings.settings["timeout"])
        if txn_receipt["status"] == 1:
            return True, txn.hex(), gas
        else:
            return False, txn.hex(), gas

    


    def SwapFromTokentoETHV2(self, inputAmount: int, trys: int = 1):
        path, dexIdents = self.getTokentoETHPathV2()
        amountOut = self.getAmountsOutV2(inputAmount, path, dexIdents)[-1]
        amountOutMinimum = int(amountOut - (amountOut * int(self.settings.settings["Slippage"])) / 100)
        txn = self.RixSwapAggregator.functions.swapTokentoETHV2(
            path,
            dexIdents,
            inputAmount,
            amountOutMinimum
        ).build_transaction({
            'from': self.user_address,
            'gasPrice': self.w3.eth.gas_price + Web3.to_wei(int(self.settings.settings["GWEI_OFFSET"]),"gwei"),
            'nonce': self.w3.eth.get_transaction_count(self.user_address),
            'value': 0
        })
        gas = self.w3U.estimateGas(txn)
        txn.update({'gas': gas[0]})
        signed_txn = self.w3.eth.account.sign_transaction(
            txn,
            self.priv_key
        )
        txn = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        txn_receipt = self.w3.eth.wait_for_transaction_receipt(
            txn, timeout=self.settings.settings["timeout"])
        if txn_receipt["status"] == 1:
            return True, txn.hex(), gas
        else:
            return False, txn.hex(), gas


    def SwapFromTokentoTokenV2(self, tokenIn, tokenOut, inputAmount: int, trys: int = 1):
        path, dexIdents = self.getTokentoTokenPathV2(tokenIn, tokenOut)
        amountOut = self.getAmountsOutV2(inputAmount, path, dexIdents)[-1]
        amountOutMinimum = int(amountOut - (amountOut * int(self.settings.settings["Slippage"])) / 100)
        txn = self.RixSwapAggregator.functions.swapTokentoTokenV2(
            path,
            dexIdents,
            inputAmount,
            amountOutMinimum
        ).build_transaction({
                'from': self.user_address,
                'gasPrice': self.w3.eth.gas_price + Web3.to_wei(int(self.settings.settings["GWEI_OFFSET"]),"gwei"),
                'nonce': self.w3.eth.get_transaction_count(self.user_address),
                'value': 0
        })
        gas = self.w3U.estimateGas(txn)
        txn.update({'gas': gas[0]})
        signed_txn = self.w3.eth.account.sign_transaction(
            txn,
            self.priv_key
        )
        txn = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        txn_receipt = self.w3.eth.wait_for_transaction_receipt(
            txn, timeout=self.settings.settings["timeout"])
        if txn_receipt["status"] == 1:
            return True, txn.hex(), gas
        else:
            return False, txn.hex(), gas
