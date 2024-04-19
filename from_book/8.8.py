def make_album(singer_name,name):
    album = {'album':name,'singer name':singer_name}
    return album

while True:
    x,y=input('Please input singer name and album name:')
    if (x or y)=='q':
        break
    else:
        print(make_album(x,y))
    
