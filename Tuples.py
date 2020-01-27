imelda = 'More Mayhem', "Imilda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"),(3, "Mayhem"), (4, "Kentish Town Waltz"))


title,artist,year,tracks = imelda

print(title)
print(artist)
print(year)
for i in tracks:
    print(i, end='\t')
    
    #2ga wersja
    
imelda = 'More Mayhem', "Imilda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"),(3, "Mayhem"), (4, "Kentish Town Waltz"))


title,artist,year,tracks = imelda

print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track,title))
