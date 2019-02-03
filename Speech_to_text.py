from selenium import webdriver
import time

#For system speaking
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

browser = webdriver.Chrome("G:/Python_Prog_Examples/chromedriver.exe")
##Hitting the url
browser.get("https://dictation.io/speech")
time.sleep(12)
clear_text=browser.find_element_by_xpath('//a[@class="btn btn--sm btn-clear btn--primary" and @data-tooltip="Clear Dictation Notepad"]//span[@class="btn__text"]')
#clear the editor window
clear_text.click()
#system speech
speak.Speak("Please click on 'Allow' button and start saying: ")

start_mic=browser.find_element_by_xpath('//a[@class="btn-mic btn btn--primary-1"]//span[@class="btn__text listen"]')
#click on start mic button
start_mic.click()
#Capturing speech upto 20 seconds
time.sleep(20)
#clicking stop mic button
stop_mic=browser.find_element_by_xpath('//a[@class="btn-mic btn bg--pinterest"]')
stop_mic.click()

#Capturing all voice comands into text format
elem=browser.find_element_by_xpath('//div[@class="ql-editor"]//p')
voice_command=elem.text
# print(voice_command)
#System speech
speak.Speak(voice_command)
print("Transcripted text is: " + voice_command)
#Writting Transcripted text into file.
f= open("Transcription.txt","w+")
f.write(voice_command)

