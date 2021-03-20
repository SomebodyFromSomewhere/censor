#To choose your mic uncomment 3 lines below and run code
#Example: https://youtu.be/YeS755SPSI8?list=WL&t=207

# import speech_recognition as sr
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


import speech_recognition as sr
import time
import pyglet

r = sr.Recognizer()
m = sr.Microphone(device_index=1)

opts = {
    "alias": (
        'сука', 'нахуй', 'нубля', 'б**', 'б****', 'уебок', 'хуясе', 'еблан', 'блядина', 'п****', 'pidor', 'пидорас',
        'гандон', 'сучара', 'з*****', 'сукко', 'уёбак', 'ёбанный', 'м****', 'блять', 'е****', 'з*****', 'п*****',
        'х****', 'ёб твою мать', 'г*****', 'х**', 'хуйне', 'п******', 'долбаёб', 'долбаёбы', 'н****', 'з******', 'с***', 'ахуел', 'чмо')
}

with m as source:
    r.adjust_for_ambient_noise(source)
    print("Now you can talk")
    audio = r.listen(source)


def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="ru-RU").lower()
        print("[log] Распознано: " + voice)
        if set(opts["alias"]) & set(voice.split()):
            print('Мат')
            audio = pyglet.media.load("air_horn.wav")
            audio.play()

    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")


stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1)
