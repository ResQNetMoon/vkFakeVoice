from requests import post,get
class UploadVoiceMsg:
	def __init__(self,token, oggFile):
		self.ex = open(oggFile, 'rb')
		self.token = token
	def upload (self):
		uploadServers = get("https://api.vk.com/method/docs.getUploadServer?access_token={}&type=audio_message&v=5.63".format(self.token)).json()
		uploadServer = uploadServers['response']['upload_url']
		data = post(uploadServer+"?access_token="+self.token, files={'file':self.ex}).json()
		self.ex.close()
		dds = get("https://api.vk.com/method/docs.save?file={0}&access_token={1}&v=5.63".format(data['file'], self.token))
		
		self.data = dds.json()
	def returnAttachment(self):
		arr = self.data['response'][0]
		return 'doc{0}_{1}'.format(arr['owner_id'], arr['id'])
class UploadPhoto:
	def __init__(self, photo, token):
		f = open(photo, 'rb')
		self.photo = f.read()
		f.close()
		self.token = token

	def upload(self):
		tok = get("https://api.vk.com/method/photos.getMessagesUploadServer?access_token={}".format(self.token)).json()
		url = tok['response']['upload_url']
		data = post(url, files={'file':self.photo}).json()
		print(data)

		server = data['server']
		photo_hash = data['hash']
		photos_uploaded = data['photo']
		data = get("https://api.vk.com/method/photos.saveMessagesPhoto?access_token={0}&photo={1}&server={2}&hash={3}".format(self.token, photos_uploaded, server, photo_hash)).json()
		print(data)