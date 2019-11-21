import eyed3

audiofile = eyed3.load("M:\\Projects\\MP3Player\\Songs\\Sugar.mp3")

print(audiofile.tag.artist)
audiofile.tag.artist = u"Maroon 5"
#audiofile.tag.save()
print(audiofile.tag.artist)
audiofile.tag.album_artist = u"Maroon 5"
audiofile.tag.title = u"Sugar"
#audiofile.tag.track_num = 2

audiofile.tag.save(version=(2,3,0))
#audiofile.tag.save()

#audiofile.tag.save()
