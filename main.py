from CinemaBot import crawling as cinema_bot
from CoinoneBot import cointickerbot as coinone_bot
from EbookBot import ebook as ebook_bot
from GithubSlackBot import github_bot 
from SpellCheckBot import bots as spell_check_bot
from TranslateBot import connectSlack as translate_bot
from ShuttleCokeBot import shuttlecockBot as shuttlecoke_bot

import requests
import websocket
import json
import os
import datetime
import time
import threading

vars = {
    'shuttlecoke': {
        'msgs': None
    },
    'ebook': {
        'packt_channel_id': 'C9AHFRRMX'
    }
}
credentials = None
with open('credentials.json', 'r') as fr:
    credentials = json.loads(fr.read())

with open('ShuttleCokeBot/businfo.json', 'r') as fr:
    vars['shuttlecoke']['msgs'] = json.loads(fr.read())

def packt_alarm_thread(ws):
    while True:
        now = datetime.datetime.now()
        tomorrow_9am = datetime.datetime.now()
        if now.hour >= 9:
            tomorrow_9am += datetime.timedelta(days=1)
        tomorrow_9am = tomorrow_9am.replace(hour=9, minute=0, second=0)
        delta = tomorrow_9am - now
        time.sleep(delta.seconds + 1)
        mock_msg = {
            'channel': vars['ebook']['packt_channel_id'],
            'type': 'message',
            'text': 'eBook'
        }
        ebook_bot.on_message(ws, json.dumps(mock_msg))

def on_message(ws, message):
    orig_message = message
    message = json.loads(message) # 전달받은 message는 무조건 JSON 형태이므로, 이를 사용하기 쉽게 Python Dict 형식으로 변환 
    if 'type' not in message.keys() or message['type'] != 'message': # 입력받은 메세지가 텍스트가 아닐 경우
        return # 여기서 다룰 필요가 없으므로 그냥 끝내기
    print(message)
    
    if type(message['text']) == 'str' and message['text'].startswith('맞춤법:'):
        new_message = message
        new_message['text'] = new_message['text'][4:]
        spell_check_bot.on_message(ws, orig_message)
    if '영화' in message['text']:
        cinema_bot.on_message(ws, orig_message)
    if message['text'].startswith('코인원'):
        coinone_bot.on_message(ws, orig_message)
    if 'ebook' in message['text'] or 'eBook' in message['text'] or 'e북' in message['text'] or '이북' in message['text'] or 'Ebook' in message['text']:
        ebook_bot.on_message(ws, orig_message)
    if message['text'].startswith('!github_register') or message['text'].startswith('!github_unregister'):
        github_bot.message(ws, orig_message)
    if translate_bot.translator_check(message['text']):
        translate_bot.on_message(ws, orig_message)
    shuttlecoke_bot.on_message(ws, orig_message)
    
token = credentials['SLACKBOT_TOKEN']
get_url = requests.get('https://slack.com/api/rtm.connect?token=' + token) # Slack RTM에 WebSocket 통신 URL을 가져오는 API 요청 보냄

socket_endpoint = get_url.json()['url'] # get_url.json()은 위의 JSON 객체 형태를 지니니까, 여기서 ULR 부분만 뽑아와서 socket_endpoint에 저장


websocket.enableTrace(True) # 디버깅을 위해 통신 정보를 모두 콘솔에 프린트 
ws = websocket.WebSocketApp(socket_endpoint, on_message=on_message) # 가져온 URL, 콜백 함수를 이용하여 WebSocket 객체 생성

thread = threading.Thread(target=packt_alarm_thread, args=(ws,))
thread.start()
ws.run_forever() # WebSocket 서버와 통신
