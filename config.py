import os
import argparse

BOT_ID = os.getenv('BOT_ID', '5820943379:AAFTRZFbcG8sdDzN1YbwXul8hWipEgSKi-c')
CHAT_ID = os.getenv('CHAT_ID', '319647436')
PORT = os.getenv('PORT', '53110')
parser = argparse.ArgumentParser()
parser.add_argument('--port', type=str, default=PORT)
args = parser.parse_args()
if args.port:
    PORT = args.port

# BOT_ID = '6019323408:AAF-gkpzbqnZQBTqSVBT-JnESavJjyAmgHA'
# CHAT_ID = '1006019323408'