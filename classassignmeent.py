class Ronnie:
    def favorite_song(self):
        return "Ronnie said his favorite_song is 'Monalisa by Blaq tunez'"
class John(Ronnie):
    def favorite_song(self):
        return "John said his favorite_song is 'No time by Justine Bieber'"
class Aaron(Ronnie):
    def favorite_song(self):
        return "Aaron said his favorite_song is 'Let me love you by Mario'"
class Benjie(John, Aaron):
    def favorite_song(self):
        return "Benjie said his favorite_song is 'Shape of You by Ed Sheeran'"
b= Benjie()
j= John()
a= Aaron()
print(b.favorite_song())
print(j.favorite_song())
print(a.favorite_song())