from quart import render_template
from quart_rate_limiter import rate_exempt

from . import index_bp


@index_bp.route("/")
@rate_exempt
async def _index() -> str:
    return await render_template("index.html")
