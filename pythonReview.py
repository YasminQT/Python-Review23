def create_youtube_video(title,description):

	video={'title':title,'description':description,'likes':0,'dislikes':0, 'comments': {}}
	return video

def like(video):
	if 'likes' in video:
		video['likes']+=1
	return video

def dislike(video):
	if 'dislikes' in video:
		video['dislikes']+=1
	return video

def add_comment(video,username,comment_text):
	video['comments'][username]=['comment_text']
	return video['comments']

vid1=create_youtube_video("Funny Cat Videos","Amazing")
like(vid1)
dislike(vid1)

for i in range(495):
	like(vid1)
	
print (vid1)

#vid1 = create_youtube_video()

#add_comment(vid1)