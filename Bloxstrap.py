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
downloadninstall("https://download.visualstudio.microsoft.com/download/pr/17089bd5-7875-4a3f-a430-5da3bc2dd57e/33acf480233bfb3fca383fb664fc8981/dotnet-runtime-6.0.31-win-x64.exe")
downloadninstall("https://github.com/pizzaboxer/bloxstrap/releases/download/v2.6.1/Bloxstrap-v2.6.1.exe")
