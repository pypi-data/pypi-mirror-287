!pip install simpleaudio
!pip install keyboard
!pip install pydub
import simpleaudio as sa
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import speech_recognition as sr
import webbrowser
import time
import datetime
import requests
import keyboard
hi = (["Привет","привет","Добрый вечер","Доброе утро","Доброй ночи","Здорово","Здарова","Здравстуй","Здравствуйте","Привет Джарвис","Джарвис Привет","Добрый вечер Джарвис","Доброе утро Джарвис","Доброй ночи Джарвис","Здорово Джарвис","Здарова Джарвис","Здравстуй Джарвис","Здравствуйте Джарвис"])


def pusk():
    global text
    text = "пусто"
    hour = int(datetime.datetime.now().hour)
    slushayu_name = 'slushayu.wav'
    wave_obj = sa.WaveObject.from_wave_file(slushayu_name)
    play = wave_obj.play()
    play.wait_done()
    play.stop()
    recording = sd.rec(int(5 * 44100), samplerate=44100, channels=2)
    sd.wait(2)
    write("recording.wav", 44100, recording)
    wv.write("recording.wav", recording, 44100, sampwidth=2)
    r = sr.Recognizer()
    with sr.AudioFile("recording.wav") as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio, language="ru-RU")
        print("Text: "+text)
    except Exception as e:
        print("Exception: "+str(e))


    if hour>=0 and hour<12 and text in hi:
        zvuk = 'morning.wav'
        wave_obj = sa.WaveObject.from_wave_file(zvuk)
        play = wave_obj.play()
        play.wait_done()
        play.stop()
        pusk()
    elif hour>=12 and hour<18 and text in hi:
        zvuk = 'day.wav'
        wave_obj = sa.WaveObject.from_wave_file(zvuk)
        play = wave_obj.play()
        play.wait_done()
        play.stop()
        pusk()
    elif hour>=18 and hour<24 and text in hi:
        zvuk = 'evening.wav'
        wave_obj = sa.WaveObject.from_wave_file(zvuk)
        play = wave_obj.play()
        play.wait_done()
        play.stop()
        pusk()

    elif "погода " in text:
        zvuk = 'open.wav'
        wave_obj = sa.WaveObject.from_wave_file(zvuk)
        play = wave_obj.play()
        play.wait_done()
        play.stop()
        pogoda_fact, city = text.split('погода ')
        webbrowser.open_new_tab('https://yandex.ru/pogoda/search?request=' +city)

    elif "поиск" in text:
        zvuk = 'poisk.wav'
        wave_obj = sa.WaveObject.from_wave_file(zvuk)
        play = wave_obj.play()
        play.wait_done()
        play.stop()
        poisk2, poisk = text.split('поиск ')
        webbrowser.open_new_tab('https://yandex.ru/search/?text=' +poisk)
    elif "Найди" in text:
        zvuk = 'poisk.wav'
        wave_obj = sa.WaveObject.from_wave_file(zvuk)
        play = wave_obj.play()
        play.wait_done()
        play.stop()
        poisk2, poisk = text.split('Найди ')
        webbrowser.open_new_tab('https://yandex.ru/search/?text=' +poisk)
    elif "найти" in text:
        zvuk = 'poisk.wav'
        wave_obj = sa.WaveObject.from_wave_file(zvuk)
        play = wave_obj.play()
        play.wait_done()
        play.stop()
        poisk_fakt, poisk = text.split('найти ')
        webbrowser.open_new_tab('https://yandex.ru/search/?text=' +poisk)

    elif "Включи " in text:
        zvuk = 'on.wav'
        wave_obj = sa.WaveObject.from_wave_file(zvuk)
        play = wave_obj.play()
        play.wait_done()
        play.stop()
        music_fact, music = text.split('Включи ')
        webbrowser.open_new_tab('https://music.yandex.ru/search?text=' + music)
    elif "Включи песню" in text:
        zvuk = 'on.wav'
        wave_obj = sa.WaveObject.from_wave_file(zvuk)
        play = wave_obj.play()
        play.wait_done()
        play.stop()
        music_fact, music = text.split('Включи песню ')
        webbrowser.open_new_tab('https://music.yandex.ru/search?text=' + music)
    elif "песня" in text:
        zvuk = 'on.wav'
        wave_obj = sa.WaveObject.from_wave_file(zvuk)
        play = wave_obj.play()
        play.wait_done()
        play.stop()
        music_fact, music = text.split('песня ')
        webbrowser.open_new_tab('https://music.yandex.ru/search?text=' + music)

    elif text == "отмена":
        zvuk = 'ponial.wav'
        wave_obj = sa.WaveObject.from_wave_file(zvuk)
        play = wave_obj.play()
        play.wait_done()
        play.stop()

    elif text == "пока":
        zvuk = 'godbie.wav'
        wave_obj = sa.WaveObject.from_wave_file(zvuk)
        play = wave_obj.play()
        play.wait_done()
        play.stop()

    else:
        zvuk = 'neponial.wav'
        wave_obj = sa.WaveObject.from_wave_file(zvuk)
        play = wave_obj.play()
        play.wait_done()
        play.stop()
        pusk()


def start():
    while True:
        if keyboard.is_pressed('Ctrl + Alt'):
            pusk()
        if text == "пока" or keyboard.is_pressed('Ctrl + Q'):
            break