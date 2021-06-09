import pafy

def getMetaData(video):
	print("Video Details are ----")
	print("Video Title: " , video.title)
	print(f"Total views: { video.viewcount } | video Length: { video.length } seconds ")
	print("Channel Name : " , video.author)

def download_as_video(video):
	getMetaData(video)
	best=video.getbest()
	print(f"video Resolution : {best.resolution} \n Video Extension : {best.extension}")
	best.download()
	print("Video is Downloaded...")

def download_as_audio(video):
	getMetaData(video)
	bestaudio=video.getbestaudio()
	bestaudio.download()


url=input("Enter Video Url :")

video=pafy.new(url)

choice=input("Press 'V' for video download and ' A' for audio: ")

if choice.upper()== "V":
	download_as_video(video)
elif choice.upper()== "A":
	download_as_audio(video)
else:
	print(" Wrong Key Value")