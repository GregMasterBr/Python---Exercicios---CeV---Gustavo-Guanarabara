import vlc
import time
import random
import emoji

musics = ['Giant.mp3','Rize_Up.mp3','Birds_in_Flight.mp3']
musica = random.choice(musics)
s = vlc.MediaPlayer(("./mp3/{}".format(musica)))
print(emoji.emojize(':speaker: :musical_note: Dança ai Galera, a musica que está tocando é: {}',use_aliases=True).format(musica))

s.play()

time.sleep(20)
s.stop()
