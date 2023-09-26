import random, time, requests, re, os

from bs4 import BeautifulSoup as bs4
from colorama import Fore, Back, Style, init
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
init()
print("[!] Proxyを取得しています...")

h = {
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 Chrome/109.0.0.0 Safari/537.36'
}

p_html = requests.get("https://free-proxy-list.net/", headers=h).text
get_proxy_tr = bs4(p_html, 'html.parser').find_all('tr')

proxies = []
for tr in get_proxy_tr:
    td = tr.find_all('td')
    if len(td) >= 2:
        ip = td[0].text
        port = td[1].text
        if (re.search(r'\.', ip)):
            proxies.append(f"{ip}:{port}")
print("[!] 取得完了")

ip_port = random.choice(proxies)
print(f"[!] ip:port = {ip_port}")

print("[!] Chromeを起動しています")
chrome_options = Options().add_argument(f"--proxy-server=http://{ip_port}")
d = webdriver.Chrome(options=chrome_options)
os.system("cls")


def get_temp_mail():
    d.get("https://mail.tm/en/")

    d.implicitly_wait(6)

    mail = d.find_element(By.ID, "DontUseWEBuseAPI")
    mailAd = mail.get_attribute('value')
    print("Email: " + mailAd)

    return mailAd


def gen_user_name():
    user_name = ''
    verbs = ['awkward','thin','thick','happy','sad','tall','short','malious','ravenous','smooth','loving','mean','weird','high','sober',"smart",'dumb','rich','poor','mega','music','lord']
    nouns = ['hacker','lumberjack','horse','unicorn','guy','girl','man','woman','male','female','men','women','duck','dog','sheep','zombie','tennis','doctor']
    starts = ['Touches_','Loves_','Hates_','Licks_','Feels_']

    user_name = random.choice(starts) + random.choice(verbs) + '_' + random.choice(nouns) + 's'

    replace_char = random.randint(1,10)
    if replace_char == 1:
        user_name = user_name.replace('i', '1')
        user_name = user_name.replace('a', '4')
        user_name = user_name.replace('e', '3')
        user_name = user_name.replace('l','|')
    elif replace_char == 2:
        user_name = user_name.replace('_', '-')
    elif replace_char == 3:
        user_name = user_name.replace('_', '7')
    elif replace_char == 4:
        user_name = user_name.replace('m','nn')
    else:
        user_name = user_name

    return user_name


def password_gen(r):
	data = "qwerioplkjhgvbnm12345890QWJHGFDSAZXCVBNM@!"
	result = ""
	while r >= 1:
		c = random.choice(data)
		result += c
		r -= 1
	return result


def ymd_select():
    year_drop = d.find_element(By.CLASS_NAME, "year-3_SRuv")
    year_drop.click()
    time.sleep(2)
    year_char = random.randint(20,40)
    year = d.find_element(By.ID, f"react-select-2-option-{year_char}")
    year.click()
    time.sleep(2)

    mounts_drop = d.find_element(By.CLASS_NAME, "month-1Z2bRu")
    mounts_drop.click()
    time.sleep(2)
    mounts_char = random.randint(0,11)
    mounts = d.find_element(By.ID, f"react-select-3-option-{mounts_char}")
    mounts.click()
    time.sleep(2)

    days_drop = d.find_element(By.CLASS_NAME, "day-1uOKpp")
    days_drop.click()
    time.sleep(2)
    days_char = random.randint(0,27)
    days = d.find_element(By.ID, f"react-select-4-option-{days_char}")
    days.click()
    time.sleep(2)


smss = []
def get_sms():
    sms_html = requests.get("https://receive-smss.com/", headers=h).text
    get_sms_div = bs4(sms_html, 'html.parser').find('div', attrs={ 'class': 'number-boxes'})

    get_sms_a = get_sms_div.find_all('a')
    for sms in get_sms_a:
        sms = sms.get('href').replace('/sms/', '').replace('/', '')
        smss.append(sms)
    
def verif_sms():
    get_sms()
    r_sms = random.choice(smss)
    r = requests.get(f"https://receive-smss.com/sms/{r_sms}/", headers=h).text
    sms_where = bs4(r, 'html.parser').find('h3').text.replace(' mobile phone number.', '')
    print(f"{r_sms}:{sms_where}")

    v_button = d.find_element(By.CLASS_NAME, "marginBottom20-315RVT button-ejjZWC lookFilled-1H2Jvj colorBrand-2M3O3N sizeMedium-2oH5mg grow-2T4nbg")
    v_button.click()

    c_button = d.find_element(By.CLASS_NAME, 'countryButton-1cNDvB button-ejjZWC lookFilled-1H2Jvj colorPrimary-2-Lusz sizeSmall-3R2P2p grow-2T4nbg')
    c_button.click()

    sms_input = d.find_element(By.CLASS_NAME, 'input-2m5SfJ')
    sms_input.send_keys(sms_where)


mailAd = ""
passw = ""
def discord_regist():
    print("Emailを取得しています")
    mailAd = "huqj4d987y@gmail.com" # get_temp_mail()

    d.get("https://discord.com/register")
    WebDriverWait(d, 30).until(EC.presence_of_element_located((By.NAME, 'email')))

    print("情報を入力しています")
    mail_input = d.find_element(By.NAME, "email")
    for char in mailAd:
        mail_input.send_keys(char)
        time.sleep(0.5)

    time.sleep(2)

    name_input = d.find_element(By.NAME, "global_name")
    for char in f"! {gen_user_name()}":
        name_input.send_keys(char)
        time.sleep(0.5)

    time.sleep(2)

    name_input = d.find_element(By.NAME, "username")
    for char in gen_user_name():
        name_input.send_keys(char)
        time.sleep(0.5)

    time.sleep(2)

    pass_input = d.find_element(By.NAME, "password")
    passw = password_gen(16)
    for char in passw:
        pass_input.send_keys(char)
        time.sleep(0.5)
    print("Password: " + passw)

    time.sleep(2)

    ymd_select()
    time.sleep(1.4)

    submit_button = d.find_element(By.CLASS_NAME, "button-1cRKG6")
    submit_button.click()

    option = input("Use Option?: ")
    if option == "sms":
        verif_sms()


    

print(
f"""{Fore.CYAN}

██████╗░██╗░██████╗░█████╗░░█████╗░░█████╗░██╗░░██╗
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
██║░░██║██║╚█████╗░██║░░╚═╝██║░░██║██║░░██║█████═╝░
██║░░██║██║░╚═══██╗██║░░██╗██║░░██║██║░░██║██╔═██╗░
██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝╚█████╔╝██║░╚██╗
╚═════╝░╚═╝╚═════╝░░╚════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝
"""
)

discord_regist()
with open("./ac-token.txt", "w") as f:
    f.write(f"{mailAd} | {passw}")
input()