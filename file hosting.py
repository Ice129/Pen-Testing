import requests
import json

#https://discord.com/api/webhooks/947495640177463396/hIwtUxPefHlQBMFtM6Gx2K0EahrVHUkqGC0c1wMgVGcBGwX_Cgdz73ODJ9GVr9RppfPH
#webhook^^^^

#https://gofile.io/api
#host website ^^^

request = requests.get("https://api.gofile.io/getServer").json()
server = request["data"]["server"]
# path = r"X:\Library\4.WIP\Screenshot 2021-03-22 153316.jpg"

# with open(path, "rb") as go_file_d:
#     filedata = go_file_d.read()

# request = requests.get(url=f"https://{server}.gofile.io/uploadFile", data=filedata)
# print(request)

def upload_file(path):

    request = requests.get("https://api.gofile.io/getServer").json()
    server = request["data"]["server"]

    url = f"https://{server}.gofile.io/uploadFile"
    files = {'fileUpload': open(path, 'rb')}

    response = requests.post(url, files=files)
    json_data = json.loads(response.text)

    link = json_data['data']["downloadPage"]
    name = json_data['data']["fileName"]
    return link,name

def webhook(link,name):
    webhook_url = "https://discord.com/api/webhooks/947495640177463396/hIwtUxPefHlQBMFtM6Gx2K0EahrVHUkqGC0c1wMgVGcBGwX_Cgdz73ODJ9GVr9RppfPH"
    requests.post(webhook_url, data={"content": name + "\n" + link})

def main():
    path = r"X:\Library\4.WIP\Screenshot 2021-03-22 153316.jpg"
    link,name = upload_file(path)
    webhook(link,name)


if __name__ == "__main__":
    main()