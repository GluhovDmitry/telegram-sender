import aiohttp

import config as cfg

from aiohttp import web


async def send_message_telegram(request) -> web.json_response():
    request_data = await request.json()
    url = f"https://api.telegram.org/bot{cfg.BOT_ID}/sendMessage"
    body = {
        "chat_id": cfg.CHAT_ID,
        "text": request_data['message']
    }
    headers = {
        "Content-Type": "application/json",
        "cache-control": "no-cache",
        'Access-Control-Allow-Origin': '*',
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(
                url=url,
                json=body,
                headers=headers
        ) as resp:
            if resp.status == 200:
                return web.json_response({'message': 'Data sent'}, status=200)
            else:
                return web.json_response({'message': f'Failure: {await resp.text()}'}, status=400)