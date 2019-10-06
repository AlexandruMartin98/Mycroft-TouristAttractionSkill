import requests
import re
import wikipedia as wiki
from adapt.intent import IntentBuilder
from mycroft.skills.core import (MycroftSkill, intent_handler,
                                 intent_file_handler)

import random
from gtts import gTTS
import os


class Touristattraction(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('touristattraction.intent')
    def handle_touristattraction(self, message):
        # self.speak_dialog('touristattraction')
        google_places_api = 'https://calm-savannah-13967.herokuapp.com/ro/googleplaces/'
        # https: // calm - savannah - 13967.herokuapp.com / ro / googleplaces / timisoara
        city_name = 'timisoara'
        url = google_places_api + city_name
        json_data = requests.get(url).json()
        results = json_data['results']
        random_index = random.randint(0, len(results) - 1)
        # self.speak_dialog(results[random_index]['name'])

        self.speak({"utterance": "words to be spoken", "lang": "en-us"})


        s = "Poți să vizitezi:"
        s = s + results[random_index]['name']
        file = "file.mp3"
        # initialize tts, create mp3 and play
        tts = gTTS(s, 'ro')
        tts.save(file)
        os.system("mpg123 " + file)

        '''
        for i in range(len(results)):
            self.speak_dialog(results[i]['name'])
        '''
        # self.speak_dialog(json_data['results'][1]['name'])

    @intent_file_handler("touristattraction_summary.intent")
    def handle_all_dialog_intent(self, message):
        self.handle_dialog_intent(message)

    @intent_handler(IntentBuilder("").require("locatia"))
    def handle_dialog_intent(self, message):
        wiki.set_lang("ro")
        locatia = message.data.get('locatia')
        upper_locatia = locatia
        upper_locatia = ' '.join(word[0].upper() + word[1:] for word in upper_locatia.split())
        search_results = wiki.search(upper_locatia)
        # self.speak_dialog("searching", {"query": upper_locatia})
        self.speak_dialog("->>>>  <<<<-")


        '''
        begin_speak = "Folosirea diacriticelor poate ajuta la găsirea locației. "
        file = "file.mp3"
        # initialize tts, create mp3 and play
        tts = gTTS(begin_speak, 'ro')
        tts.save(file)
        os.system("mpg123 " + file)
        '''


        begin_speak = "O să caut cât de repede pot pentru" + upper_locatia
        file = "file.mp3"
        # initialize tts, create mp3 and play
        tts = gTTS(begin_speak, 'ro')
        tts.save(file)
        os.system("mpg123 " + file)

        end_speak = ""
        search_results = wiki.search(upper_locatia)
        upper_locatia = upper_locatia.strip()
        for i in range(len(search_results)):
            upper_search = search_results[i]
            upper_search = ' '.join(word[0].upper() + word[1:] for word in upper_search.split())

            if upper_locatia in upper_search:
                # self.speak_dialog(wiki.summary(search_results[i], sentences=1))
                end_speak = end_speak + wiki.summary(search_results[i], sentences=1)
                file = "file.mp3"
                # initialize tts, create mp3 and play
                tts = gTTS(end_speak, 'ro')
                tts.save(file)
                os.system("mpg123 " + file)
            elif upper_locatia in upper_search and "Timișoara" in upper_search:
                # self.speak_dialog(wiki.summary(search_results[i], sentences=1))
                end_speak = end_speak + wiki.summary(search_results[i], sentences=1)
                file = "file.mp3"
                # initialize tts, create mp3 and play
                tts = gTTS(end_speak, 'ro')
                tts.save(file)
                os.system("mpg123 " + file)
            elif upper_locatia in upper_search and "din" in upper_search and "Timișoara" in upper_search:
                # self.speak_dialog(wiki.summary(search_results[i], sentences=1))
                end_speak = end_speak + wiki.summary(search_results[i], sentences=1)
                file = "file.mp3"
                # initialize tts, create mp3 and play
                tts = gTTS(end_speak, 'ro')
                tts.save(file)
                os.system("mpg123 " + file)



        '''
        try:
            while True:
                data = input('prompt:')
                print('READ:', data)
                if data == "b":
                    print("yes")
                    break
                else:
                    print("no")
                    break
        except EOFError as e:
            print(e)
            
        '''

        special_case = ""
        if upper_locatia.find("Timișoara") is -1:
            '''
            self.speak_dialog("If don't look like description you want, maybe should try..."
                              + upper_locatia +
                              " din Timișoara or "
                              + upper_locatia +
                              " Timișoara.")
            '''

            special_case = special_case + "Dacă nu este locația dorită puteți încerca" \
                           + upper_locatia + " din Timișoara sau " \
                           + upper_locatia + "Timișoara."
            file = "file.mp3"
            # initialize tts, create mp3 and play
            tts = gTTS(special_case, 'ro')
            tts.save(file)
            os.system("mpg123 " + file)

        else:
            '''
            self.speak_dialog("If don't look like description you want, maybe should try "
                              + upper_locatia +
                              " without Timișoara")
            '''

            special_case = special_case + "Dacă nu este locația dorită puteți încerca" \
                           + upper_locatia + "fără Timișoara"
            file = "file.mp3"
            # initialize tts, create mp3 and play
            tts = gTTS(special_case, 'ro')
            tts.save(file)
            os.system("mpg123 " + file)



    '''    
    @intent_handler(IntentBuilder("").require("locatia"))
    def handle_dialog_intent(self, message):
        wiki.set_lang("ro")
        locatia = message.data.get('locatia')

        nume_locatie = locatia
        Lista_text = nume_locatie.split()
        # self.speak_dialog(random.choice(results[i]['name']))


        begin_speak = "O să caut cât de repede pot pentru" + nume_locatie
        file = "file.mp3"
        # initialize tts, create mp3 and play
        tts = gTTS(begin_speak, 'ro')
        tts.save(file)
        os.system("mpg123 " + file)

        end_speak = ""
        search_results = wiki.search(nume_locatie)
        self.speak_dialog(search_results[0])
        found = False
        for i in range(len(search_results)):

            self.speak_dialog("intraat in primul for")

            if nume_locatie in search_results[i]:
                self.speak_dialog("intraat in primul if")
                #self.speak_dialog(wiki.summary(search_result[i], sentences=1))
                end_speak = end_speak + wiki.summary(search_results[i], sentences=1)
                file = "file.mp3"
                # initialize tts, create mp3 and play
                tts = gTTS(end_speak, 'ro')
                tts.save(file)
                os.system("mpg123 " + file)
                found = True
                break

        for i in range(len(search_results)):
            if Lista_text[0] in search_results[i] and Lista_text[1] in search_results[i] \
                    and "Timișoara" in search_results[i] and found == False:
                self.speak_dialog("intraat in al doilea if")
                #self.speak_dialog(wiki.summary(search_result[i], sentences=1))
                end_speak = end_speak + wiki.summary(search_results[i], sentences=1)
                file = "file.mp3"
                # initialize tts, create mp3 and play
                tts = gTTS(end_speak, 'ro')
                tts.save(file)
                os.system("mpg123 " + file)
                found = True
                break
        for i in range(len(search_results)):
            if Lista_text[0] in search_results[i] and "Timișoara" in search_results[i] and found == False:
                #self.speak_dialog(wiki.summary(search_result[i], sentences=1))
                self.speak_dialog("intraat in al treile if")

                end_speak = end_speak + wiki.summary(search_results[i], sentences=1)
                file = "file.mp3"
                # initialize tts, create mp3 and play
                tts = gTTS(end_speak, 'ro')
                tts.save(file)
                os.system("mpg123 " + file)
                found = True
                break
    '''

    def stop(self):
        pass


def create_skill():
    return Touristattraction()
