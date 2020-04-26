def make_album(artist,album_title,track_number=''):
    while True:
        artist = input('enter artist')
        if artist == 'q':
            break
        album_title = input('enter album name')
        if album_title == 'q':
            break
        track_number = input('enter number of tracks')
        if track_number == 'q':
            break
    
    album = {'artist': artist, 'album': album_title}
    if track_number:
        album['track_number'] = track_number
        return album

album_info = make_album(input('This program will store Music albums'),input('Press Enter'))
print(album_info)
