"""Mini-game by CAN YILDIRIM · Hugging Games."""
import random
import math

def reply(state, message):
    return state, message

def finish(state, message):
    state["done"] = True
    return state, message + "\n🏁 Oyun bitti. Yeniden başlat ile tekrar oyna."

def new_game():
    n=random.randint(1,12);return {'current':n,'round':0,'score':0,'done':False},f"Başlangıç sayısı: {n}. Sonraki daha 'yüksek' mi 'düşük' mü? (8 tur)"
def play(s,action):
    if s['done']:return reply(s,'Yeni oyun başlat.')
    a=action.lower().strip()
    if a not in ('yüksek','yuksek','düşük','dusuk'):return reply(s,"yüksek veya düşük yaz.")
    n=random.randint(1,12);ok=(n>s['current'] and a in ('yüksek','yuksek')) or (n<s['current'] and a in ('düşük','dusuk'))
    s['score']+=int(ok);s['round']+=1;s['current']=n
    msg=f"Yeni sayı {n}. {'✅' if ok else '❌ (eşit sayılar puan vermez)'} Skor {s['score']}/{s['round']}. "
    return finish(s,msg) if s['round']==8 else reply(s,msg+'Sıradaki yüksek mi düşük mü?')
