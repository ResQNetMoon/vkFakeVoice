import lib
def splitJson(array):
	js = {}
	for i in range(0,len(array)-1):
		js.update({array[i]:array[i+1]})
	return js
f = open('config.conf')
data = f.read().replace(' ', '').split('\n')
f.close()
confLog = splitJson(data[0].split(':'))
configPass = splitJson(data[1].split(':'))
confLog.update(configPass)

selector = input("Selector: ")
ids = input("id: ")
file = input("File: ")
from vk_api import VkApi
vk = VkApi(login = confLog['login'], password = confLog['password'])
vk.auth()
token = vk.token['access_token']

dray = lib.UploadVoiceMsg(token, "voices/"+file)
dray.upload()
vk.method("messages.send", {selector:ids, 'attachment':dray.returnAttachment()})
print("all is okay")