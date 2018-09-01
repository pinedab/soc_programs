# Exercise 40 - Modules, Classes, and Objects
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Feliz Cumpleanos a ti",
                   "No quiero que me demanden",
                   "Asi que parare alli"])

make_someone_happy = Song(["One smile that cheers you",
	"One face that lights when it nears you",
	"One girl you're ev'rything to."])

happy_bday.sing_me_a_song()

make_someone_happy.sing_me_a_song()

a = "If you're happy and you know it"
b = "Clap your hands"
c = "And you really wanna show it"

if_you_re_happy = Song([a, b, a, b, a, c, a, b])

if_you_re_happy.sing_me_a_song()