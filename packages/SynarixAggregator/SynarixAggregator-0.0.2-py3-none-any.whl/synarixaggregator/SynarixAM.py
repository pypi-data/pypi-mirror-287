from .W3Utils import W3Utils
from .core_settings import CoreSettings
from .core_chains import chains
from .IERC20 import IERC20
from .SynarixAC_F import InterfaceAggregatorContract  
from web3 import Web3
from web3.middleware import geth_poa_middleware
import logging, json

class SynarixAggregatorModul:
    def __init__(self, token:str=None, settings_file_path:str="./Settings.json", saveSettings:bool=False):
        self.settings = CoreSettings(settings_file_path,  saveSettings)
        self.w3 = self.connect()
        self.w3U = W3Utils(self.settings, self.w3)
        if Web3.is_address(token):
            self.token = Web3.to_checksum_address(token)
            pass
        else:
            logging.info("No Token Addresss Provided fallback to Synarix Governance Token")
            self.token = chains(self.w3.eth.chain_id).RIX
        self.IERC20 = IERC20(self.settings, self.w3, Web3.to_checksum_address(self.token), self.w3U)
        self.IAC = InterfaceAggregatorContract(self.settings, self.w3, self.IERC20, self.w3U)

    def reload(self):
        self.w3 = self.connect()
        self.w3U = W3Utils(self.settings, self.w3)
        self.IERC20 = IERC20(self.settings, self.w3, self.token, self.w3U)
        self.IAC = InterfaceAggregatorContract(self.settings, self.w3, self.IERC20, self.w3U)

    def connect(self):
        keys = self.settings.settings
        if keys["RPC"][:2].lower() == "ws":
            w3 = Web3(Web3.WebsocketProvider(keys["RPC"],websocket_timeout=keys["timeout"]))
            w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        else:
            w3 = Web3(Web3.HTTPProvider(keys["RPC"], request_kwargs={'timeout': int(keys["timeout"])}))
            w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        return w3
    
    def check_settings(self) -> str:
        if self.settings.settings.get("address") and not Web3.is_address(self.settings.settings["address"]):
            return "Invalid address in settings!"
        if len(self.settings.settings.get("private_key")) and len(self.settings.settings["private_key"]) not in [64, 66]:
            return"Invalid private_key in settings!"
        return "Address Setup is done"
    
    def printSettings(self):
         print(json.dumps(self.settings.settings, indent=4))
        
    def loadWalletFromMnomic(self, mnemoic):
        mne_address , private_key = self.w3U.getMnemonicToPrivKey(mnemoic)
        self.editSettings("address", mne_address, skipReload=True)
        self.editSettings("private_key", private_key)

    def loadWalletFromPrivKey(self, private_key ):
        address = self.w3U.getAddresFromPrivKey(private_key)
        self.editSettings("address", address, skipReload=True)
        self.editSettings("private_key", private_key)

    def changeRPC(self, newRPC):
        self.editSettings("RPC", newRPC)

    def editSettings(self, key, newValue, skipReload:bool = False):
        self.settings.change_settings(key, newValue)
        if not skipReload:
            self.reload()

    
        
    def getSettings(self):
        return self.settings.settings
        
    def changeToken(self, token:str):
       self.IERC20 = IERC20(
            self.settings,
            self.w3,
            Web3.to_checksum_address(token),
            self.w3U
        )
       self.IAC = InterfaceAggregatorContract(self.settings, self.w3, self.IERC20, self.w3U)
       
    






