from decimal import Decimal, ROUND_DOWN
from web3 import Web3 



class W3Utils:
    def __init__(self, settings, w3):
        self.settings, self.w3 = settings, w3

    def block(self):
        return self.w3.eth.blockNumber
    
    def getMnemonicToPrivKey(self, mnemonic, account_path:str="m/44'/60'/0'/0/0"):
        self.w3.eth.account.enable_unaudited_hdwallet_features()
        account = self.w3.eth.account.from_mnemonic(mnemonic, account_path)
        return account.address, self.w3.to_hex(account.key)
    
    def getAddresFromPrivKey(self, private_key):
        return self.w3.eth.account.from_key(str(private_key)).address

    def estimateGas(self, txn):
        gas = self.w3.eth.estimate_gas(txn)
        gas_wei = gas + (gas / 10)  # Adding 1/10 from gas to gas!
        gas_cost = self.custom_round(Web3.from_wei(gas * (self.w3.eth.gas_price + (int(self.settings.settings['GWEI_OFFSET']) * (10**9))), "ether"))
        if float(gas_cost) > float(self.settings.settings["MaxTXFeeBNB"]):
            return gas_wei, gas_cost, False
        return int(gas_wei), gas_cost, True
    

    def custom_round(self, num):
        num_str = str(self.get_human_amount(num))
        try:
            integer_part, fractional_part = num_str.split('.')
            if integer_part != '0':
                if len(integer_part) >= 4:
                    return Decimal(num).quantize(Decimal('0'), rounding=ROUND_DOWN)
                else:
                    return Decimal(num).quantize(Decimal('0.00'), rounding=ROUND_DOWN)    
            else:
                first_non_zero_idx = next((idx for idx, char in enumerate(fractional_part) if char != '0'), None)
                if len(fractional_part[first_non_zero_idx:]) >= 3:
                    total_digits = first_non_zero_idx + 4
                else:
                    total_digits = first_non_zero_idx + 2
                idx_str = "0." + "0" * (total_digits)  
                return self.get_human_amount(Decimal(num).quantize(Decimal(idx_str), rounding=ROUND_DOWN))
        except Exception as e:
            return num


    def to_wei(self, token_amount: Decimal, decimals: int) -> int:
        token_amount_decimal = Decimal(token_amount)
        smallest_amount = int(token_amount_decimal * (10 ** decimals))
        return smallest_amount

    def from_wei(self, token_amount: int, decimals: int) -> Decimal:
        amount_decimal = Decimal(token_amount) / (10 ** decimals)
        return amount_decimal
    
    def get_decimal_places(self, number):
        decimal_number = Decimal(str(number))
        decimal_places = -decimal_number.as_tuple().exponent
        return decimal_places
    
    def get_human_amount(self, number):
        format = "{:." + f"{self.get_decimal_places(number)}" + "f}"
        decimal_number = format.format(number)
        return decimal_number
    
