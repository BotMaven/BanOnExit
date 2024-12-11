import logging
from aiohttp import web
import asyncio
import aiohttp
import traceback
from BanOnExit.configs import config

logger = logging.getLogger(__name__)
routes = web.RouteTableDef()


@routes.get("/", allow_head=True)
async def root_route_handler():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Bot Status</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          display: flex;
          align-items: center;
          justify-content: center;
          height: 100vh;
          margin: 0;
          background-color: #f4f4f9;
          color: #333;
        }
        .status {
          text-align: center;
        }
        h1 {
          color: #4CAF50;
        }
      </style>
    </head>
    <body>
      <div class="status">
        <h1>Bot operational and ready to serve!</h1>
        <p>Made with ❤️ by <a href="https://t.me/BotMaven" target="_blank">@BotMaven</a></p>
      </div>
    </body>
    </html>
    """
    return web.Response(text=html_content, content_type="text/html")


def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app


async def keep_alive():
    sleep_time = config.PING_INTERVAL
    if config.URL:
        while True:
            await asyncio.sleep(sleep_time)
            try:
                async with aiohttp.ClientSession(
                    timeout=aiohttp.ClientTimeout(total=10)
                ) as session:
                    async with session.get(config.URL) as resp:
                        logger.info(
                            "Pinged {} with response: {}".format(
                                config.URL, resp.status
                            )
                        )
            except TimeoutError:
                logger.warning("Couldn't connect to the site URL..!")
            except Exception:
                traceback.print_exc()
