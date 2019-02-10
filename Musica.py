from winsound import PlaySound, SND_FILENAME, SND_LOOP, SND_ASYNC
class Musica:   
	def play_sound(self):
		PlaySound('resources/music/tili.wav', SND_FILENAME|SND_LOOP|SND_ASYNC)
	def stop_sound(self):
		PlaySound(None, SND_FILENAME)