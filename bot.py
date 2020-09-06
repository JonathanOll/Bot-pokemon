import time
import json
from urllib import request
from urllib.error import HTTPError
import random
from captcha_solver import CaptchaSolver

run = True

def last_message_name(id, token):
    WEBHOOK_URL = 'https://discord.com/api/v8/channels/' + str(id) + '/messages?limit=1'

    # Les paramètres d'en-tête de la requête
    headers = {
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11',
        'authorization': token
    }

    # Enfin on construit notre requête
    req = request.Request(url=WEBHOOK_URL, headers=headers, method='GET')

    # Puis on l'émet !
    try:
        response = request.urlopen(req)
        resp = str(response.read()).split('"username": ')
        resp = resp[1].split('"')[1]
        return resp
    except HTTPError as e:
        print('ERROR')
        print(e.reason)
        print(e.hdrs)
        print(e)

def sendMessage(message, id, token):
    WEBHOOK_URL = 'https://discord.com/api/v8/channels/' + str(id) + '/messages'

    # La payload
    payload = {
        'content': message
    }

    # Les paramètres d'en-tête de la requête
    headers = {
        'Content-Type': 'application/json',
        'user-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11',
        'authorization': token
    }

    # Enfin on construit notre requête
    req = request.Request(url=WEBHOOK_URL,
                          data=json.dumps(payload).encode('utf-8'),
                          headers=headers,
                          method='POST')
    # Puis on l'émet !
    try:
        response = request.urlopen(req)
        resp = str(response.read()).split('"content": ')
        resp = resp[1].split('"')[1]
        return resp
    except HTTPError as e:
        print('ERROR')
        print(e.reason)
        print(e.hdrs)
        print(e)

def last_response_embeds(id, token):
    if not last_message_name('752105251145908285', lashox).__contains__("Pok"):
        return "none"

    WEBHOOK_URL = 'https://discord.com/api/v8/channels/' + str(id) + '/messages?limit=1'

    # Les paramètres d'en-tête de la requête
    headers = {
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11',
        'authorization': token
    }

    # Enfin on construit notre requête
    req = request.Request(url=WEBHOOK_URL, headers=headers, method='GET')

    # Puis on l'émet !
    try:
        response = request.urlopen(req)
        resp = str(response.read()).split('{"name": ')
        resp = resp[1].split('"')[1]
        return resp
    except HTTPError as e:
        print('ERROR')
        print(e.reason)
        print(e.hdrs)
        print(e)


def last_reponse_message(id, token):
    WEBHOOK_URL = 'https://discord.com/api/v8/channels/' + str(id) + '/messages?limit=1'

    # Les paramètres d'en-tête de la requête
    headers = {
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11',
        'authorization': token
    }

    # Enfin on construit notre requête
    req = request.Request(url=WEBHOOK_URL, headers=headers, method='GET')

    # Puis on l'émet !
    try:
        response = request.urlopen(req)
        resp = str(response.read()).split('"content": ')
        resp = resp[1].split('"')[1]
        return resp
    except HTTPError as e:
        print('ERROR')
        print(e.reason)
        print(e.hdrs)
        print(e)

def last_pokemon_rarity(id, token):
    if not last_message_name(id, lashox).__contains__("Pok"):
        return "none"

    WEBHOOK_URL = 'https://discord.com/api/v8/channels/' + str(id) + '/messages?limit=1'

    # Les paramètres d'en-tête de la requête
    headers = {
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11',
        'authorization': token
    }

    # Enfin on construit notre requête
    req = request.Request(url=WEBHOOK_URL, headers=headers, method='GET')

    # Puis on l'émet !
    try:
        response = request.urlopen(req)
        resp = str(response.read()).split('"text": ')
        resp = resp[1].split('"')[1]
        return resp.split("(")[0].replace("Rarity: ", "")
    except HTTPError as e:
        print('ERROR')
        print(e.reason)
        print(e.hdrs)
        print(e)

def last_pokemon_name(id, token):
    if not last_message_name(id, lashox).__contains__("Pok"):
        return "none"

    WEBHOOK_URL = 'https://discord.com/api/v8/channels/' + str(id) + '/messages?limit=1'

    # Les paramètres d'en-tête de la requête
    headers = {
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11',
        'authorization': token
    }

    # Enfin on construit notre requête
    req = request.Request(url=WEBHOOK_URL, headers=headers, method='GET')

    # Puis on l'émet !
    try:
        response = request.urlopen(req)
        resp = str(response.read()).split('> **')
        resp = resp[1].split('**')[0]
        return resp
    except HTTPError as e:
        print('ERROR')
        print(e.reason)
        print(e.hdrs)
        print(e)

def launch(id, token):
    while(run):
        sendMessage(";p", id, token)
        time.sleep(4)
        if not last_reponse_message(id, token).__contains__("wild"):
            continue
        if last_reponse_message(id, token).__contains__("captcha"):
            sendMessage("<@!351069423303655435> captcha", id, token)
            continue
        rarity = last_pokemon_rarity(id, token).strip()
        name = last_pokemon_name(id, token)
        if rarity == "Common":
            pokeball = 'pb'
        elif rarity == "Uncommon":
            pokeball = 'pb'
        elif rarity == "Rare":
            pokeball = 'pb'
        elif rarity == "Super Rare":
            pokeball = 'gb'
        elif rarity == "Legendary":
            pokeball = 'mb'
        elif rarity == "Gold":
            pokeball = 'mb'
        else:
            pokeball = 'pb'

        if name.startswith("Shiny") and pokeball != 'mb':
            pokeball = 'ub'

        print("recognized %s rarity %s so I'll use %s" % (
        last_pokemon_name(id, token), last_pokemon_rarity(id, token), pokeball))

        sendMessage(pokeball, id, token)
        time.sleep(10)

launch('id du channel', 'votre token discord')
