import pandas as pd
# 用户名和密码控制
account={}
with open('用户名和密码存储.txt','r') as fp:
    for line in fp.readlines():
        a,b=line.split()[:2]
        account[a]=b
#曲库控制
#songs=pd.read_csv('lastfm-dataset-1K/userid-timestamp-artid-artname-traid-traname.tsv',sep='\t',error_bad_lines=False)
songs_data=open('musiclyrics-master/billboard_lyrics_1964-2015.csv','a+')
songs_data.seek(0)
songs=[]
for line in songs_data.readlines()[1:]:
    songs.append(line.split(','))
for i in range(len(songs)):
    if songs[i][1][0]=='"' or songs[i][1][-1]=='"':
       songs[i][1],songs[i][2],songs[i][4]=songs[i][1][1:-1],songs[i][2][1:-1],songs[i][4][1:-1]
#临时变量
temp=''
#听过的歌
frequent={}
with open('听歌记录.txt','r') as fp:
    for line in fp.readlines():
        a,b=line.split(',')[0],line.split(',')[1:]
        frequent[a]=b


