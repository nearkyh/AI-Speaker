import os
import random

def media_player(text):
    media_dir = './media'
    classical_music_dir = '/classical_music'
    jazz_music_dir = '/jazz_music'
    pop_music_dir = '/pop_music'

    if '클래식' in text:
        music_list = os.listdir(media_dir + classical_music_dir)
        random_music = random.choice(music_list)
        return media_dir + '/' + classical_music_dir + '/' + random_music

    elif '재즈' in text:
        music_list = os.listdir(media_dir + jazz_music_dir)
        random_music = random.choice(music_list)
        return media_dir + '/' + jazz_music_dir + '/' + random_music

    elif '팝송' in text:
        music_list = os.listdir(media_dir + pop_music_dir)
        random_music = random.choice(music_list)
        return media_dir + '/' + pop_music_dir + '/' + random_music

    elif '노래' in text:
        music_list = os.listdir(media_dir)
        dir_choice = random.choice(music_list)
        choice_music = os.listdir(media_dir + '/' + dir_choice)
        random_music = random.choice(choice_music)
        return media_dir + '/' + dir_choice + '/' + random_music

    else:
        pass
