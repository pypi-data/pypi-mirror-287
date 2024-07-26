# -*- coding: utf-8 -*-

#   Copyright (C) 2022-2024 Samuele Carcagno <sam.carcagno@gmail.com>
#   This file is part of sound_source_id

#    sound_source_id is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    sound_source_id is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with sound_source_id.  If not, see <http://www.gnu.org/licenses/>.


import matplotlib
matplotlib.rcParams['path.simplify'] = False

from .pyqtver import*

if pyqtversion == 5:
    
    from PyQt5 import QtGui, QtCore
    from PyQt5.QtGui import QFont
    from PyQt5.QtWidgets import QApplication
    matplotlib.rcParams['backend'] = "Qt5Agg"
elif pyqtversion == 6:
    from PyQt6 import QtGui, QtCore
    from PyQt6.QtGui import QFont
    from PyQt6.QtWidgets import QApplication
    matplotlib.rcParams['backend'] = "QtAgg"
    

import platform, os, pickle

if platform.system() == "Linux":
    try:
        import alsaaudio
        alsaaudioAvailable = True
    except ImportError:
        alsaaudioAvailable = False
        pass
else:
    alsaaudioAvailable = False


try:
    import pyaudio
    pyaudioAvailable = True
except ImportError:
    pyaudioAvailable = False
    pass


def global_parameters(prm):

    prm['backupDirectoryName'] = os.path.expanduser("~") +'/.local/share/data/sound_source_id/data_backup/'
    if os.path.exists(prm['backupDirectoryName']) == False:
        os.makedirs(prm['backupDirectoryName'])

    prm['appData']['alsaaudioAvailable'] = alsaaudioAvailable
    prm['appData']['pyaudioAvailable'] = pyaudioAvailable

    if platform.system() == 'Linux':
        prm['appData']['available_play_commands'] = []
        if os.system("which aplay") == 0:
            prm['appData']['available_play_commands'].append("aplay")
        if os.system("which play") == 0:
            prm['appData']['available_play_commands'].append("play")
        if os.system("which sndfile-play") == 0:
            prm['appData']['available_play_commands'].append("sndfile-play")
    elif platform.system() == 'Windows':
        prm['appData']['available_play_commands'] = ["winsound"]
        if os.system("where sndfile-play") == 0:
            prm['appData']['available_play_commands'].append("sndfile-play")
    elif platform.system() == 'Darwin': #that should be the MAC
        prm['appData']['available_play_commands'] = ["afplay"]
    elif platform.system() == 'FreeBSD':
        prm['appData']['available_play_commands'] = ["wavplay"]
    if alsaaudioAvailable == True:
        prm['appData']['available_play_commands'].append("alsaaudio")
    if pyaudioAvailable == True:
        prm['appData']['available_play_commands'].append("pyaudio")
    prm['appData']['available_play_commands'].append(QApplication.translate("","custom",""))

    prm['appData']['wavmanagers'] = ["wavpy", "wavpy_sndf"]

    prm['appData']['available_languages'] = ["System Settings",
                                             "en",
                                             "it",
                                             "fr",
                                             "es",
                                             "el"]
    prm['appData']['available_countries'] = {}
    prm['appData']['available_countries']['System Settings'] = ["System Settings"]
    prm['appData']['available_countries']['en'] = ["US",
                                                   "GB"]

    prm['appData']['available_countries']['it'] = ["IT",
                                                   "CH"]
    prm['appData']['available_countries']['fr'] = ["FR",
                                                   "CA"]

    prm['appData']['available_countries']['es'] = ["ES",
                                                   "BO",
                                                   "CL"]

    prm['appData']['available_countries']['el'] = ["GR",
                                                   "CY"]



    return prm


def def_prefs(prm):
    prm["pref"] = {}
    prm["pref"]["sound"] = {}

    ## system
    prm['pref']['language'] = 'System Settings'
    prm['pref']['country'] = 'System Settings'

    prm["pref"]["csvSeparator"] = ";"
    prm["pref"]["precision"] = 12

    ##prm["pref"]["default_prm_file"] = prm['data']['appDir'] + "prm.ploc"
    prm["pref"]["default_prm_file"] = prm['rootDirectory'] + '/prm_files/' + "prm.txt"


    ## response 
    prm["pref"]["correctLightColor"] = (0,255,0)
    prm["pref"]["incorrectLightColor"] = (255,0,0)
    prm["pref"]["neutralLightColor"] = (255,255,255)
    prm["pref"]["offLightColor"] = (0,0,0)
    prm["pref"]["responseLightFont"] = QFont('Sans Serif', 30, QFont.Weight.Bold, False).toString()

    prm["pref"]["correctTextFeedback"] = "CORRECT" #QApplication.translate("","Yes","") #self.tr("CORRECT")
    prm["pref"]["incorrectTextFeedback"] = "INCORRECT"
    prm["pref"]["neutralTextFeedback"] = "DONE"
    prm["pref"]["offTextFeedback"] = ""
    prm["pref"]["correctTextColor"] = (255,255,255)
    prm["pref"]["incorrectTextColor"] = (255,255,255)
    prm["pref"]["neutralTextColor"] = (255,255,255)
    prm["pref"]["offTextColor"] = (255,255,255)

    prm["pref"]["responseLightDuration"] = 1000
    
    ## Sound
    prm["pref"]["sound"]["wavmanager"] = "wavpy"
    prm["pref"]["sound"]["bufferSize"] = 1024
    prm["pref"]["sound"]["appendSilence"] = 0
    prm["pref"]["sound"]["prependSilence"] = 0
    prm["pref"]["sound"]["transducers"] = "Transducers 1"
    
    if platform.system() == 'Windows':
        prm["pref"]["sound"]["playCommand"] = "winsound"
        prm["pref"]["sound"]["playCommandType"] = "winsound"
    elif platform.system() == 'Darwin':
        prm["pref"]["sound"]["playCommand"] = "afplay"
        prm["pref"]["sound"]["playCommandType"] = QApplication.translate("","custom","")
    else:
        prm["pref"]["sound"]["playCommand"] = "aplay"
        prm["pref"]["sound"]["playCommandType"] = QApplication.translate("","custom","")
    if alsaaudioAvailable == True:
        prm["pref"]["sound"]["alsaaudioDevice"] = "default"
    if pyaudioAvailable == True:
        prm["pref"]["sound"]["pyaudioDevice"] = 0


    #prm["pref"]["transducers"] = "Transducers 1"

    # Transducers
    prm["transducers"] = {}
    prm["transducers"]["transducersChoices"] = ["Transducers 1", "Transducers 2"]
    prm["transducers"]["transducersMaxLevel"] = [100, 100]
    prm["transducers"]["transducersID"] = ['0', '1']
    
    # Figure preferences
    prm['pref']['grid'] = True
    prm['pref']['dpi'] = 80
    #range is 0--255
    prm['pref']['lineColor1'] = (0,0,0)
    prm['pref']['line_width'] = 1
    prm['pref']['backgroundColor'] = (250,250,250)
    prm['pref']['canvasColor'] = (200, 200, 200)
    prm['pref']['axes_color'] = (0,0,0)
    prm['pref']['grid_color'] = (0,0,0)
    prm['pref']['tick_label_color'] = (0,0,0)
    prm['pref']['axes_label_color'] = (0,0,0)
    prm['pref']['label_font_family'] = 'sans-serif'
    prm['pref']['label_font_weight'] = 'normal'
    prm['pref']['label_font_style'] = 'normal' #italics, oblique
    prm['pref']['label_font_size'] = 12
    prm['pref']['label_font_stretch'] = 'normal'
    prm['pref']['label_font_variant'] = 'normal'
    prm['pref']['major_tick_length'] = 5
    prm['pref']['major_tick_width'] = 1
    prm['pref']['minor_tick_length'] = 3
    prm['pref']['minor_tick_width'] = 0.8

    prm['pref']['grid_line_width'] = 0.5
    prm['pref']['spines_line_width'] = 1

    prm['pref']['tick_label_font_family'] = 'sans-serif'
    prm['pref']['tick_label_font_weight'] = 'normal'
    prm['pref']['tick_label_font_style'] = 'normal' #italics, oblique
    prm['pref']['tick_label_font_size'] = 12
    prm['pref']['tick_label_font_stretch'] = 'normal'
    prm['pref']['tick_label_font_variant'] = 'normal'

    return prm



def get_prefs(prm):
    prm = def_prefs(prm)
    prm['prefFile'] = os.path.expanduser("~") +'/.config/sound_source_id/preferences'
    prm['transducersPrefFile'] = os.path.expanduser("~") +'/.config/sound_source_id/transducers.py'

    if os.path.exists(os.path.expanduser("~") +'/.config/') == False:
        os.mkdir(os.path.expanduser("~") +'/.config/')
    if os.path.exists(os.path.expanduser("~") +'/.config/sound_source_id/') == False:
        os.mkdir(os.path.expanduser("~") +'/.config/sound_source_id/')
    if os.path.exists(prm['prefFile']):
        fIn = open(prm['prefFile'], 'rb')
        prm['tmp'] = pickle.load(fIn)
        fIn.close()
        for k in prm['pref'].keys():
            if k in prm['tmp']:
                prm['pref'][k] = prm['tmp'][k]

    # if there are transducers settings stored, load them
    if os.path.exists(prm['transducersPrefFile']):
        fIn = open(prm['transducersPrefFile'], 'rb')
        prm['tmp'] = pickle.load(fIn)
        fIn.close()
        for k in prm['transducers'].keys():
            if k in prm['tmp']:
                prm['transducers'][k] = prm['tmp'][k]
                
    return prm
