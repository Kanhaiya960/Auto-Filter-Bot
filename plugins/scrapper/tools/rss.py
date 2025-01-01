import re, os
import time
import asyncio
import requests
from bs4 import BeautifulSoup
from pyrogram import Client
from database.users_chats_db import db as u_db
from info import TAMILMV_LOG, TAMILBLAST_LOG, TAMILROCKERS_LOG

# TamilMV RSS Feed Scraper Function
async def tamilmv(bot: Client):
    tamilmv_url = await u_db.get_domain("1TamilMV")
    if not tamilmv_url:
        print("Error: TamilMV domain not found in the database.")
        return
    main_link = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Connection': 'Keep-alive',
        'sec-ch-ua-platform': '"Windows"',
    }

    global movie_dict
    movie_dict = {}
    global real_dict
    real_dict = {}
    web = requests.request("GET", tamilmv_url, headers=headers)
    soup = BeautifulSoup(web.text, 'lxml')
    linker = []
    bad_titles = []
    real_titles = []
    global movie_list
    movie_list = []

    num = 0

    temps = soup.find_all('div', {'class': 'ipsType_break ipsContained'})

    for i in range(21):
        title = temps[i].findAll('a')[0].text
        bad_titles.append(title)
        links = temps[i].find('a')['href']
        content = str(links)
        linker.append(content)

    for element in bad_titles:
        real_titles.append(element.strip())
        movie_dict[element.strip()] = None

    movie_list = list(movie_dict)

    for url in linker:
        html = requests.request("GET", url, headers=headers)
        soup = BeautifulSoup(html.text, 'lxml')
        pattern = re.compile(r"magnet:\?xt=urn:[a-z0-9]+:[a-zA-Z0-9]{40}")
        big_title = soup.find_all('a')
        all_titles = []
        file_link = []
        mag = []
        for i in soup.find_all('a', href=True):
            if i['href'].startswith('magnet'):
                mag.append(i['href'])

        for a in soup.findAll('a', {"data-fileext": "torrent", 'href': True}):
            file_link.append(a['href'])

        for title in big_title:
            if title.find('span') == None:
                pass
            else:
                if title.find('span').text.endswith('torrent'):
                    all_titles.append(title.find('span').text[19:-8])

        for p in range(0, len(mag)):
            try:
                real_dict.setdefault(movie_list[num], [])
                real_dict[movie_list[num]].append((f"/ql {file_link[p]} \n\n **{all_titles[p]}**"))
                if not await u_db.is_tamilmv_exist(all_titles[p], file_link[p], mag[p]):
                    await bot.send_message(chat_id=TAMILMV_LOG,
                        text=f"<b>/qbleech {file_link[p]}\n🧲 Magnet Link :- <a href='https://t.me/share/url?url={mag[p]}'>Click here</a>\n\n{all_titles[p]}</b>\n<b>📥 Updated By <a href='https://t.me/DP_BOTZ'>1TamilMV</a></b>", disable_web_page_preview=True)
                    print(f"added working...")
                    await u_db.add_tamilmv(all_titles[p], file_link[p], mag[p])
                    await asyncio.sleep(300)
            except Exception as e:
                print(e)
                pass

        num = num + 1
    return real_dict

# tamilblasters rss feed function

async def tamilblasters(bot: Client):
    tamilblasters_url = await u_db.get_domain("1TamilBlasters")
    if not tamilblasters_url:
        print("Error: TamilBlasters domain not found in the database.")
        return
    main_link = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Connection': 'Keep-alive',
        'sec-ch-ua-platform': '"Windows"',
    }

    global movie_dict
    movie_dict = {}
    global real_dict
    real_dict = {}
    web = requests.request("GET", tamilblasters_url, headers=headers)
    soup = BeautifulSoup(web.text, 'lxml')
    linker = []
    bad_titles = []
    real_titles = []
    global movie_list
    movie_list = []

    num = 0

    temps = soup.find_all('div', {'class': 'ipsType_break ipsContained'})

    for i in range(41):
        title = temps[i].findAll('a')[0].text
        bad_titles.append(title)
        links = temps[i].find('a')['href']
        content = str(links)
        linker.append(content)

    for element in bad_titles:
        real_titles.append(element.strip())
        movie_dict[element.strip()] = None

    movie_list = list(movie_dict)

    for url in linker:
        html = requests.request("GET", url, headers=headers)
        soup = BeautifulSoup(html.text, 'lxml')
        pattern = re.compile(r"magnet:\?xt=urn:[a-z0-9]+:[a-zA-Z0-9]{40}")
        big_title = soup.find_all('a')
        all_titles = []
        file_link = []
        mag = []
        for i in soup.find_all('a', href=True):
            if i['href'].startswith('magnet'):
                mag.append(i['href'])

        for a in soup.findAll('a', {"data-fileext": "torrent", 'href': True}):
            file_link.append(a['href'])
            all_titles.append(re.sub(r'www\.[a-z0-9.\-]+', '', a.text, flags=re.IGNORECASE).replace('.torrent', '').replace('-', '', 1).replace(' ', '', 2))

        for p in range(0, len(mag)):
            try:
                real_dict.setdefault(movie_list[num], [])
                real_dict[movie_list[num]].append((f"/ql {file_link[p]} \n\n **{all_titles[p]}**"))
                if not await u_db.is_tb_exist(all_titles[p], file_link[p], mag[p]):
                    await bot.send_message(chat_id=TAMILBLAST_LOG,
                        text=f"<b>/qbleech2 {file_link[p]}\n🧲 Magnet Link :- <a href='https://t.me/share/url?url={mag[p]}'>Click here</a>\n\n{all_titles[p]}</b>\n<b>📥 Updated By <a href='https://t.me/DP_BOTZ'>1TamilBlasters</a></b>", disable_web_page_preview=True)
                    print(f"added working...")
                    await u_db.add_tb(all_titles[p], file_link[p], mag[p])
                    await asyncio.sleep(300)
            except Exception as e:
                print(e)
                pass

        num = num + 1
    return real_dict


# TamilRockers RSS Feed Scraper Function

async def tamilrockers(bot: Client):
    tamilrockers_url = await u_db.get_domain("2TamilRockers")
    if not tamilrockers_url:
        print("Error: TamilRockers domain not found in the database.")
        return
    main_link = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Connection': 'Keep-alive',
        'sec-ch-ua-platform': '"Windows"',
    }

    global movie_dict
    movie_dict = {}
    global real_dict
    real_dict = {}
    web = requests.request("GET", tamilrockers_url, headers=headers)
    soup = BeautifulSoup(web.text, 'lxml')
    linker = []
    bad_titles = []
    real_titles = []
    global movie_list
    movie_list = []

    num = 0

    temps = soup.find_all('div', {'class': 'ipsType_break ipsContained'})

    for i in range(41):
        title = temps[i].findAll('a')[0].text
        bad_titles.append(title)
        links = temps[i].find('a')['href']
        content = str(links)
        linker.append(content)

    for element in bad_titles:
        real_titles.append(element.strip())
        movie_dict[element.strip()] = None

    movie_list = list(movie_dict)

    for url in linker:
        html = requests.request("GET", url, headers=headers)
        soup = BeautifulSoup(html.text, 'lxml')
        pattern = re.compile(r"magnet:\?xt=urn:[a-z0-9]+:[a-zA-Z0-9]{40}")
        big_title = soup.find_all('a')
        all_titles = []
        file_link = []
        mag = []
        for i in soup.find_all('a', href=True):
            if i['href'].startswith('magnet'):
                mag.append(i['href'])

        for a in soup.findAll('a', {"data-fileext": "torrent", 'href': True}):
            file_link.append(a['href'])
            all_titles.append(re.sub(r'www\.[a-z0-9.\-]+', '', a.text, flags=re.IGNORECASE).replace('.torrent', '').replace('-', '', 1).replace(' ', '', 2))

        for p in range(0, len(mag)):
            try:
                real_dict.setdefault(movie_list[num], [])
                real_dict[movie_list[num]].append((f"/ql {file_link[p]} \n\n **{all_titles[p]}**"))
                if not await u_db.is_tr_exist(all_titles[p], file_link[p], mag[p]):
                    await bot.send_message(chat_id=TAMILROCKERS_LOG,
                        text=f"<b>/qbleech {file_link[p]}\n🧲 Magnet Link :- <a href='https://t.me/share/url?url={mag[p]}'>Click here</a>\n\n{all_titles[p]}</b>\n<b>📥 Updated By <a href='https://t.me/DP_BOTZ'>2TamilRockers</a></b>", disable_web_page_preview=True)
                    print(f"added working...")
                    await u_db.add_tr(all_titles[p], file_link[p], mag[p])
                    await asyncio.sleep(300)
            except Exception as e:
                print(e)
                pass

        num = num + 1
    return real_dict
