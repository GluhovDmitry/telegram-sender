from aiohttp import web

import config as cfg

from views import send_message_telegram


async def init_app():
    app = web.Application()
    app.add_routes([web.post('/send-message', send_message_telegram)])
    return app


def main():
    web.run_app(init_app(), port=cfg.PORT)


if __name__ == '__main__':
    main()
