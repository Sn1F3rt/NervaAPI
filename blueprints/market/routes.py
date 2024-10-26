from __future__ import annotations

from typing import Any, Dict, Union

from datetime import datetime

import aiohttp
from quart import Response, jsonify, current_app

from . import market_bp

MarketData = Dict[str, Union[str, Dict[str, Any]]]


@market_bp.route("/market/tradeogre")
async def _market_tradeogre() -> tuple[Response, int]:
    market_data: MarketData = {
        "status": "success",
        "exchange": "TradeOgre",
        "pairs": current_app.config.get("TRADEOGRE_MARKET_PAIRS", []),
        "result": {},
    }

    for pair in market_data["pairs"]:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://tradeogre.com/api/v1/ticker/{pair.lower()}"
            ) as res:
                data: Dict[str, Any] = await res.json(content_type=None)

                if "error" in data:
                    market_data["result"].update(
                        {
                            pair: {
                                "error": data["error"],
                            }
                        }
                    )

                else:
                    last_price: str
                    bid: str
                    ask: str
                    volume: str
                    high: str
                    low: str

                    if pair.endswith("BTC"):
                        last_price = (
                            f"{round(float(data['price']) * 100_000_000)} sat"
                        )
                        bid = f"{round(float(data['bid']) * 100_000_000)} sat"
                        ask = f"{round(float(data['ask']) * 100_000_000)} sat"
                        volume = f"{float(data['volume'])} BTC"
                        high = f"{round(float(data['high']) * 100_000_000)} sat"
                        low = f"{round(float(data['low']) * 100_000_000)} sat"

                    else:
                        last_price = f"${round(float(data['price']), 4)}"
                        bid = f"${round(float(data['bid']), 4)}"
                        ask = f"${round(float(data['ask']), 4)}"
                        volume = f"${round(float(data['volume']), 2)}"
                        high = f"${round(float(data['high']), 4)}"
                        low = f"${round(float(data['low']), 4)}"

                    market_data["result"].update(
                        {
                            pair: {
                                "last_price": last_price,
                                "bid": bid,
                                "ask": ask,
                                "volume": volume,
                                "high": high,
                                "low": low,
                            }
                        }
                    )

    return jsonify(market_data), 200


@market_bp.route("/market/xeggex")
async def _market_xeggex() -> tuple[Response, int]:
    market_data: MarketData = {
        "status": "success",
        "exchange": "XeggeX",
        "pairs": current_app.config.get("XEGGEX_MARKET_PAIRS", []),
        "result": {},
    }

    for pair in market_data["pairs"]:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://api.xeggex.com/api/v2/market/getbysymbol/{pair.replace('-', '_')}"
            ) as res:
                data: Dict[str, Any] = await res.json()

                if "error" in data:
                    market_data["result"].update(
                        {
                            pair: {
                                "error": data["error"],
                            }
                        }
                    )

                else:
                    last_price: str
                    bid: str
                    ask: str
                    volume: str
                    high: str
                    low: str
                    last_trade: str

                    if pair.endswith("BTC"):
                        last_price = (
                            f"{round(float(data['lastPrice']) * 100_000_000)} sat"
                        )
                        bid = f"{round(float(data['bestBid']) * 100_000_000)} sat"
                        ask = f"{round(float(data['bestAsk']) * 100_000_000)} sat"
                        volume = f"{float(data['volumeSecondary'])} BTC"
                        high = f"{round(float(data['highPrice']) * 100_000_000)} sat"
                        low = f"{round(float(data['lowPrice']) * 100_000_000)} sat"
                        last_trade = datetime.fromtimestamp(
                            data["lastTradeAt"] // 1000
                        ).isoformat()

                    elif pair.endswith("USDT") or pair.endswith("USDC"):
                        last_price = f"${round(float(data['lastPrice']), 4)}"
                        bid = f"${round(float(data['bestBid']), 4)}"
                        ask = f"${round(float(data['bestAsk']), 4)}"
                        volume = f"${round(float(data['volumeSecondary']), 2)}"
                        high = f"${round(float(data['highPrice']), 4)}"
                        low = f"${round(float(data['lowPrice']), 4)}"
                        last_trade = datetime.fromtimestamp(
                            data["lastTradeAt"] // 1000
                        ).isoformat()

                    else:
                        last_price = f"{round(float(data['lastPrice']), 4)} XPE"
                        bid = f"{round(float(data['bestBid']), 4)} XPE"
                        ask = f"{round(float(data['bestAsk']), 4)} XPE"
                        volume = f"{float(data['volumeSecondary'])} XPE"
                        high = f"{round(float(data['highPrice']), 4)} XPE"
                        low = f"{round(float(data['lowPrice']), 4)} XPE"
                        last_trade = datetime.fromtimestamp(
                            data["lastTradeAt"] // 1000
                        ).isoformat()

                    market_data["result"].update(
                        {
                            pair: {
                                "last_price": last_price,
                                "bid": bid,
                                "ask": ask,
                                "volume": volume,
                                "high": high,
                                "low": low,
                                "last_trade": last_trade,
                            }
                        }
                    )

    return jsonify(market_data), 200
