def make_album(artist, album, songs):
  album = {
      "arstist_name": artist,
      "album_name": album,
      "songs_number": songs
    }
  return album

while True:
  art_name = input("Enter artist's name:")
  if art_name =="q":
    break
  alb_name = input("Enter album name:")
  if alb_name =="q":
    break
  song_num = input("Enter the number of songs:")
  if song_num =="q":
    break

  if art_name == "q" or alb_name == "q" or song_num =="q":
    break

  x = make_album(art_name, alb_name, song_num)
  print(x)

