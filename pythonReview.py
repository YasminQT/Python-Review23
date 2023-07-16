def create_youtube_video(title,description):
	video={'title':title,'description':description,'likes':0,'dislikes':0, 'comments': {}}
    return video

def like(video):
	if 'likes' in video:
			'likes'+1
	return video

def dislike(video):
	if 'dislikes' in video:
			'dislikes'+1
	return video

def add_comment(video,username,comment_text):
	video['comments']['username']=['comment_text']


vid1 = create_youtube_video()

add_comment(vid1)