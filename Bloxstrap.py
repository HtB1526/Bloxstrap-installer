import requests,subprocess,os,ctypes
def downloadninstall(url):
    fn = url.split("/")[-1]
    with open(fn, "wb") as f:
        f.write(requests.get(url).content)
    subprocess.run(fn, shell=True)
    if "visualstudio.microsoft.com" in url:
        os.remove(fn)
#If you arent skid, dont change title plz
ctypes.windll.kernel32.SetConsoleTitleW("Semi-Automated bloxstrap installer | By @HtB1526 (telegram & discord) | t.me/arceusxscripts")
downloadninstall("https://download.visualstudio.microsoft.com/download/pr/fb0630a0-d5e7-43a6-92eb-1e114de80a5b/a43563f0a5c6ca71005d8ffe5de1bd88/dotnet-runtime-6.0.28-win-x64.exe")
downloadninstall("https://github.com/pizzaboxer/bloxstrap/releases/download/v2.5.4/Bloxstrap-v2.5.4.exe")