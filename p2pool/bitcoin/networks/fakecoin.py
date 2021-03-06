import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'fbc0b6db'.decode('hex')
P2P_PORT = 9333
ADDRESS_VERSION = 48
RPC_PORT = 9332
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'fakecoinaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getblockchaininfo())['chain'] != 'test'
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//840000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'FAK'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Fakecoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Fakecoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.fakecoin'), 'fakecoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://explorer.fakeco.in/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://explorer.fakeco.in/address/'
TX_EXPLORER_URL_PREFIX = 'http://explorer.fakeco.in/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
