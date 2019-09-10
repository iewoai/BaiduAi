from aip import AipSpeech
from playsound import playsound

def get_mp3(message, mp3):
	APP_ID = '11601536'
	API_KEY = ''
	SECRET_KEY = ''

	client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

	result  = client.synthesis(message, 'zh', 1, {
		'vol': 5,
		'spd': 4,
		'plt': 6,
		'per': 4,
	})

	# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
	if not isinstance(result, dict):
		with open(mp3, 'wb') as f:
			f.write(result)
	else:
		print('错误码：'+result['error_code'])
		print('错误描述：'+result['error_msg'])


if __name__ == '__main__':
	message = '我回去了'
	mp3 = 't1.mp3'
	
	get_mp3(message, mp3)
	# 播放MP3文件
	playsound(mp3)