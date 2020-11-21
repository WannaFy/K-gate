from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import os
import datetime
import time
import pygame
import schedule

pygame.init()

import data

from PIL import ImageTk, Image

notice_board = ['这里是点歌板😍', '需要删除，更改，添加等功能']

being_played = ''


def warning(string):
    warning_top = Tk()
    warning_top.geometry('400x200')
    warning_top.option_add("*Font", "Georgia")
    warning_label = Label(warning_top, text=string)
    warning_label.pack()
    confirm_button = Button(warning_top, text='confirm!', command=warning_top.destroy)
    confirm_button.pack()
    warning_top.mainloop()


def initial():
    cls = os.system("cls")
    print(f'welcome to the "K 号房", {name}                                         ', end='')
    print(f'您已于{datetime.datetime.today()}登录或执行操作')


def play_songs():
    path = askopenfilename()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(-1)


# 放歌 自动播放
def play_musics(song_name):
    initial()
    # 存储播放歌曲名
    being_played = song_name
    # 用于存储每个用户的听歌记录
    '''data.frequent[name]=data.frequent.get(name,[])+[song_name]
    #data.frequent[name] += [song_name]
    with open('听歌记录.txt', 'r') as fp:
        a = []
        m = 1
        for t in fp.readlines():
            if name == t.split(',')[0]:
                a.append(t[:-1] + ',' + song_name + '\n')
                m = 0
            else:
                a.append(t)
        if m:
            a.append(name + ',' + song_name + '\n')
        with open('听歌记录.txt', 'w') as fp:
            fp.writelines(a)'''
    # 播放歌曲
    f = 1
    for i in data.songs:
        if i[1] == song_name:
            # 用于存储每个用户的听歌记录
            data.frequent[name]=data.frequent.get(name,[])+[song_name]
            #data.frequent[name] += [song_name]
            with open('听歌记录.txt', 'r') as fp:
                a = []
                m = 1
                for t in fp.readlines():
                    if name == t.split(',')[0]:
                        a.append(t[:-1] + ',' + song_name + '\n')
                        m = 0
                    else:
                        a.append(t)
                if m:
                    a.append(name + ',' + song_name + '\n')
                    with open('听歌记录.txt', 'w') as fp:
                        fp.writelines(a)
            f = 0
            if i[4] == 'NA' or i[4] == '  ' or i[4].rstrip()=='':
                print('sorry, but this song has no lyrics or the lyrics have been destroyed!')
            else:
                c = 0
                for j in i[4].split():
                    print(j, end=' ')
                    c += 1
                    if c % 10 == 0:
                        print('')
                        time.sleep(1)
    if f:
        warning('没有找到您要播放的歌曲')
        return
        # 每隔一段时间输出一次可以利用time.sleep(1)
    if len(notice_board) >= 3:
        temp = notice_board[2]
        del notice_board[2]
        waiting_board['text'] = '\n'.join(notice_board)
        play_musics(temp)


def update_timeText():
    # Get the current time, note you can change the format as you wish
    current = time.strftime("%H:%M:%S")  # 获取当前时间

    # Update the timeText Label box with the current time
    timeText.configure(text='本地时间:' + current)

    # Call the update_timeText() function after 1 second
    window.after(1000, update_timeText)


def print_played_songs():
    initial()
    print('您最近收听的一百首歌曲名:')
    if data.frequent.get(name) == None:
        print("你还没有听过歌哦！")
    else:
        print(data.frequent.get(name)[-100:])


def songs_group(factor):
    initial()
    if factor not in ['name', 'artist', 'year', 'source']:
        warning('''您的输入有问题哦.\n 必须输入name , artist , year , source''')
        raise ValueError('''you can only use 'name' or 'artist' or 'year' or 'source' to set these songs in group''')
    elif factor == 'name':
        t = sorted(data.songs, key=lambda x: x[1])
        print(f'{"name":50}{"artist":50}{"year":50}')
        for i in t:
            print(f'{i[1]:50}{i[2]:50}{i[3]:50}')
    elif factor == 'artist':
        t = sorted(data.songs, key=lambda x: x[2])
        print(f'{"name":50}{"artist":50}{"year":50}')
        for i in t:
            print(f'{i[1]:50}{i[2]:50}{i[3]:50}')
    elif factor == 'year':
        t = sorted(data.songs, key=lambda x: x[3])
        s = t[0][3]
        print(s + ':')
        for i in t:
            if s == i[3]:
                print(i[1], end=',')
            else:
                print('')
                s = i[3]
                print(s + ':')
                print(i[1], end=',')
    elif factor == 'source':
        t = sorted(data.songs, key=lambda x: x[5])
        s = t[0][5]
        print('source :' + s)
        c = 0
        for i in t:
            if i[5] == s:
                if c % 10 != 0 and c != 0:
                    print(i[1], end=',')
                    c += 1
                else:
                    print(i[1])
                    c += 1
            else:
                print('')
                c = 1
                s = i[5]
                print('source :' + s)
                print(i[1], end=',')


# 用lambda实现传递参数
def print_songs(left, right):
    if right.isdigit() == 0 or left.isdigit() == 0 or int(left) < 0:
        warning('请正确输入，左右都为int类型哦！')
    else:
        initial()
        print(f'{"name":50}{"artist":50}{"year":50}')
        for i in data.songs[int(left):int(right)]:
            print(f'{i[1]:50}{i[2]:50}{i[3]:50}')


def next_song():
    initial()
    if len(notice_board) < 3:
        print('没有要播放的歌曲了哦！请输入歌曲名加入等待播放。')
        warning('''没有要播放的歌曲了哦！\n 请输入歌名等待播放''')
    else:
        temp = notice_board[2]
        del notice_board[2]
        waiting_board['text'] = '\n'.join(notice_board)
        # play_musics(temp)
        for i in data.songs:
            if i[1] == temp:
                being_played = temp
                # 用于存储每个用户的听歌记录
                data.frequent[name]=data.frequent.get(name,[])+[temp]
                with open('听歌记录.txt', 'r') as fp:
                    a = []
                    f = 1
                    for t in fp.readlines():
                        if name == t.split(',')[0]:
                            a.append(t[:-1] + ',' + temp + '\n')
                            f = 0
                        else:
                            a.append(t)
                    if f:
                        a.append(name + ',' + temp + '\n')
                    with open('听歌记录.txt', 'w') as fp:
                        fp.writelines(a)
                if i[4] == 'NA' or i[4] == '  ':
                    print('sorry, but this song has no lyrics or the lyrics have been destroyed!')
                else:
                    c = 0
                    for j in i[4].split():
                        print(j, end=' ')
                        c += 1
                        if c % 10 == 0:
                            print('')
                            time.sleep(1)


def songs_waiting(song_name):
    f = 1
    for i in data.songs:
        if i[1] == song_name:
            f = 0
            notice_board.append(song_name)
            waiting_board['text'] = '\n'.join(notice_board)
            break
    else:
        warning('没要找到您要添加的歌曲')


def songs_addition(string):
    if (string.count(',') != 5 or ',,' in string or ',,,' in string or ',,,,' in string or ',' * 5 in string in string):
        warning('请正确输入，每个信息之间由逗号隔开!\n 依次位:序号(可任意)、姓名、歌手、年份、歌词、来源（数字：1，2，3······）\n 缺损信息输入NA')
    else:
        warning('恭喜您！您已成功添加歌曲到曲库中，可以打开musiclyrics-master-billboard翻至页底直接查看')
        data.songs.append(string.split(','))
        with open('musiclyrics-master/billboard_lyrics_1964-2015.csv', 'a') as fp:
            fp.write(string)


def songs_delete(string):
    f = 1
    with open('musiclyrics-master/billboard_lyrics_1964-2015.csv', 'r') as fp:
        lines = fp.readlines()
    with open('musiclyrics-master/billboard_lyrics_1964-2015.csv', 'w') as fp:
        for line in lines:
            if line.split(',')[1] != string:
                fp.write(line)
            else:
                f = 0
    if f:
        warning('没有找到您想删除的歌曲，\n 请检查您的拼写')
    else :
        warning('已成功删除歌曲')


# 如何支持模糊搜索？
def songs_search(string):
    f = 1
    for i in data.songs:
        if i[1] == string or i[2] == string:
            warning(f'''查询到歌曲信息：\n name: {i[1]} \n artist: {i[2]} \n  year: {i[3]} \n source: {i[5]} ''')
            f = 0
    if f:
        warning('没有搜索到您需要的歌曲信息！\n 请输入歌名或歌手名，\n 暂不支持模糊查询，抱歉！')


def rating_dispaly():
    # warning('欢迎浏览rating！')
    if name == '临时用户':
        warning('您是临时用户，不能查看哦！')
    else:
        rating_window = Toplevel()
        rating_window.geometry('960x540')
        rating_window.option_add("*Font", "Georgia")
        rating_window.iconbitmap('图标.ico')
        rating_window.title('rating of K')
        rating_window.wm_resizable(0, 0)
        bg_photo = Image.open('bg.png')
        bg_photo = ImageTk.PhotoImage(bg_photo)
        bg_label = Label(rating_window, image=bg_photo)
        bg_label.place(x=0, y=0)
        title_label = Label(rating_window, text='欢迎来到排行榜', bg='black', fg='white')
        title_label.pack()
        other_data_button = Button(rating_window, text='更多信息')

        song_number = len(data.songs)
        song = {}
        for i in data.frequent.values():
            for j in i:
                song[j.strip()] = song.get(j.strip(), 0) + 1
        best_songs = list(map(lambda x: x[0][:10] + ' ' * (30 - len(x[0][:10])) + str(x[1]),
                              sorted(song.items(), key=lambda x: x[1], reverse=True)))
        best_songs.insert(0, '热歌榜🎵')
        best_listeners_number = list(
            map(lambda x: x[0][:20] + ' ' * (30 - len(x[0][:20])) + str(len(x[1])),
                sorted(data.frequent.items(), key=lambda x: len(x[1]), reverse=True)))
        best_listeners_type = list(map(lambda x: f'{x[0][:20]:>}{len(set(x[1][:20])):>30}',
                                       sorted(data.frequent.items(), key=lambda x: len(set(x[1])), reverse=True)))
        # 用map得到想要的形式
        best_listeners_number.insert(0, '听歌次数排行榜🎤')
        best_listeners_type.insert(0, '听歌种类排行榜🎤')
        song_number_label = Label(rating_window, text=f'曲库中共有{song_number}首歌曲', bg='black', fg='white')
        best_listeners_number_label = Label(rating_window, text='\n'.join(best_listeners_number[:10]), bg='black',
                                            fg='white')
        best_listeners_type_label = Label(rating_window, text='\n'.join(best_listeners_type[:10]), bg='black',
                                          fg='white')
        best_songs_label = Label(rating_window, text='\n'.join(best_songs[:10]), bg='black', fg='white')
        song_number_label.pack()
        best_listeners_number_label.place(relx=0.01, rely=0.1)
        best_listeners_type_label.place(relx=0.01, rely=0.5)
        best_songs_label.place(relx=0.7, rely=0.3)
        rating_window.mainloop()


window = Tk()
window.option_add("*Font", "Georgia")
window.iconbitmap('图标.ico')
window.title('K号房')
window.geometry('1300x800')
window.wm_resizable(0, 0)
bg_photo = Image.open('bg2.png')
bg_photo = ImageTk.PhotoImage(bg_photo)
bg_label = Label(window, image=bg_photo)
bg_label.place(x=0, y=0)

# 虚假的音乐播放
play_songs_label = Button(window, text='虚假的歌曲播放按钮', command=play_songs, bg='black', fg='white')
pause_songs_label = Button(window, text='虚假的暂停键', bg='black', fg='white', command=pygame.mixer.music.pause)
unpause_songs_label = Button(window, text='继续键', bg='black', fg='white', command=pygame.mixer.music.unpause)
stop_songs_label = Button(window, text='停止播放', bg='black', fg='white', command=pygame.mixer.music.stop)

play_songs_label.pack()
pause_songs_label.pack()
unpause_songs_label.pack()
stop_songs_label.pack()
# 真实的音乐播放

left_entry = Entry(window, show=None, bd=5, bg='black', fg='white')
left_entry.insert(END, 'left')
right_entry = Entry(window, show=None, bd=5, bg='black', fg='white')
right_entry.insert(END, 'right')
factor = Entry(window, show=None, bd=5, bg='black', fg='white')
factor.insert(END, 'songs group by')
wait_songs = Entry(window, show=None, bd=5, bg='black', fg='white')
wait_songs.insert(END, 'add songs to notice board')
song_name = Entry(window, show=None, bd=5, bg='black', fg='white')
song_name.insert(END, 'name')
songs_addition_entry = Entry(window, show=None, bd=5, bg='black', fg='white')
songs_addition_entry.insert(END, 'song data')
songs_search_entry = Entry(window, show=None, bd=5, bg='black', fg='white')
songs_search_entry.insert(END, 'search')
play_songs_Button = Button(window, text='真正的歌曲播放按钮▶', command=lambda: play_musics(song_name.get()), bg='black',
                           fg='white')
play_next_Button = Button(window, text='下一首', command=next_song, bg='black', fg='white')
pause_songs_Button = Button(window, text='真正的暂停键', bg='black', fg='white', command=lambda: warning('单线程可实现不了这些(❤ ω ❤)'))
unpause_songs_Button = Button(window, text='继续播放', bg='black', fg='white', command=lambda: warning('单线程可实现不了这些(❤ ω ❤)'))
stop_songs_Button = Button(window, text='停止播放', bg='black', fg='white', command=lambda: warning('单线程可实现不了这些(❤ ω ❤)'))
print_songs_Button = Button(window, text='打印曲库', bg='black', fg='white',
                            command=lambda: print_songs(left_entry.get(), right_entry.get()))
songs_group_Button = Button(window, text='按照factor分组', bg='black', fg='white',
                            command=lambda: songs_group(factor.get()))
print_played_songs_Button = Button(window, text='最近播放的歌曲', bg='Black', fg='white', command=print_played_songs)
wait_songs_Button = Button(window, text='加入等待', bg='black', fg='white', command=lambda: songs_waiting(wait_songs.get()))
songs_addition_Button = Button(window, text='添加歌曲', bg='black', fg='white',
                               command=lambda: songs_addition(songs_addition_entry.get()))
songs_search_Button = Button(window, text='搜索歌曲信息', bg='black', fg='white',
                             command=lambda: songs_search(songs_search_entry.get()))
waiting_board = Label(window, text='\n'.join(notice_board), bg='black', fg='white')

songs_delete_entry = Entry(window, bd=5, bg='black', fg='white')
songs_delete_entry.insert(END, 'delete songs')

songs_delete_button = Button(window, text='删除歌曲', bg='black', fg='white',
                             command=lambda: songs_delete(songs_delete_entry.get()))

song_name.pack()
play_songs_Button.pack()
pause_songs_Button.pack()
unpause_songs_Button.pack()
stop_songs_Button.pack()
play_next_Button.pack()
left_entry.pack()
right_entry.pack()
print_songs_Button.pack()
wait_songs.pack()
wait_songs_Button.pack()
factor.pack()
songs_group_Button.pack()
print_played_songs_Button.pack()
waiting_board.place(relx=0.7, rely=0.4)
songs_addition_entry.place(relx=0.1, rely=0.2)
songs_addition_Button.place(relx=0.1, rely=0.3)
songs_search_entry.place(relx=0.1, rely=0.7)
songs_search_Button.place(relx=0.1, rely=0.8)
songs_delete_entry.place(relx=0.1, rely=0.5)
songs_delete_button.place(relx=0.1, rely=0.6)

# 排行榜设计即数据分析
rating_dispaly_Button = Button(window, text='查看听歌排行榜与歌曲数据分析', bg='black', fg='white', command=rating_dispaly)
rating_dispaly_Button.place(relx=0.1, rely=0.4)

# 时间更新
timeText = Label(window, text='本地时间', bg='black', fg='white')
timeText.place(relx=0.8, rely=0.1)
update_timeText()
name = data.temp
initial()
window.mainloop()
