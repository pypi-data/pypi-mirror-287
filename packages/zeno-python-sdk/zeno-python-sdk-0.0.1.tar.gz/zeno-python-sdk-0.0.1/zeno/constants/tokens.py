from zeno.constants.assets import (
  ASSET_BTC,
  ASSET_ETH,
  ASSET_mUSDC,
  ASSET_mUSDT
)

COLLATERAL_WETH = "0x420000000000000000000000000000000000000A"
COLLATERAL_WBTC = "0xa5B55ab1dAF0F8e1EFc0eB1931a957fd89B918f4"
COLLATERAL_mUSDC = "0xEA32A96608495e54156Ae48931A7c20f0dcc1a21"
COLLATERAL_mUSDT = "0xbB06DCA3AE6887fAbF931640f67cab3e3a16F4dC"

CHAIN_COLLATERAL = {
  1088: [
      COLLATERAL_WETH,
      COLLATERAL_WBTC,
      COLLATERAL_mUSDC,
      COLLATERAL_mUSDT,
  ]
}

# ------ Token Profiles ------
TOKEN_PROFILE = {
  # Metis
  1088: {
    "m.USDC": {
      "symbol": "m.USDC",
      "address": COLLATERAL_mUSDC,
      "asset": ASSET_mUSDC,
      "decimals": 6
    },
    COLLATERAL_mUSDC: {
      "symbol": "m.USDC",
      "address": COLLATERAL_mUSDC,
      "asset": ASSET_mUSDC,
      "decimals": 6
    },
    "m.USDT": {
      "symbol": "m.USDT",
      "address": COLLATERAL_mUSDT,
      "asset": ASSET_mUSDT,
      "decimals": 6
    },
    COLLATERAL_mUSDT: {
      "symbol": "m.USDT",
      "address": COLLATERAL_mUSDT,
      "asset": ASSET_mUSDT,
      "decimals": 6
    },
      "WETH": {
        "symbol": "WETH",
        "address": COLLATERAL_WETH,
        "asset": ASSET_ETH,
        "decimals": 18
    },
      COLLATERAL_WETH: {
        "symbol": "WETH",
        "address": COLLATERAL_WETH,
        "asset": ASSET_ETH,
        "decimals": 18
    },
      "WBTC": {
        "symbol": "WBTC",
        "address": COLLATERAL_WBTC,
        "asset": ASSET_BTC,
        "decimals": 8
    },
      COLLATERAL_WBTC: {
        "symbol": "WBTC",
        "address": COLLATERAL_WBTC,
        "asset": ASSET_BTC,
        "decimals": 8
    },
  }
}
