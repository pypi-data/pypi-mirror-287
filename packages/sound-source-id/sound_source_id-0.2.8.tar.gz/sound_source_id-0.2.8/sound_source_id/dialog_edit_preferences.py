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

from .pyqtver import*

if pyqtversion == 5:
    from PyQt5 import QtGui, QtCore
    from PyQt5.QtCore import QLocale, QThread, pyqtSignal
    from PyQt5.QtWidgets import QApplication, QCheckBox, QColorDialog, QComboBox, QDialog, QDialogButtonBox, QFileDialog, QFontDialog, QGridLayout, QLabel, QLayout, QLineEdit, QMessageBox, QPushButton, QSizePolicy, QSpacerItem, QStyleFactory, QWidget, QTabWidget, QVBoxLayout
    from PyQt5.QtGui import QColor, QFont, QIntValidator, QDoubleValidator
elif pyqtversion == 6:
    from PyQt6 import QtGui, QtCore
    from PyQt6.QtCore import QLocale, QThread, pyqtSignal
    from PyQt6.QtWidgets import QApplication, QCheckBox, QColorDialog, QComboBox, QDialog, QDialogButtonBox, QFileDialog, QFontDialog, QGridLayout, QLabel, QLayout, QLineEdit, QMessageBox, QPushButton, QSizePolicy, QSpacerItem, QStyleFactory, QWidget, QTabWidget, QVBoxLayout
    from PyQt6.QtGui import QColor, QFont, QIntValidator, QDoubleValidator
    
QtCore.Signal = QtCore.pyqtSignal
QtCore.Slot = QtCore.pyqtSlot
    
import copy, pickle, hashlib, base64, platform, sys 

if platform.system() == "Linux":
    try:
        import alsaaudio
    except ImportError:
        pass
try:
    import pyaudio
except ImportError:
    pass

class preferencesDialog(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.tmpPref = {}
        self.tmpPref['pref'] = copy.deepcopy(self.parent().prm['pref'])
        self.currLocale = self.parent().prm['appData']['currentLocale']
        self.currLocale.setNumberOptions(self.currLocale.NumberOption.OmitGroupSeparator | self.currLocale.NumberOption.RejectGroupSeparator)
       
        
        self.tabWidget = QTabWidget()
        self.tabWidget.currentChanged.connect(self.tabChanged)
        self.appPrefWidget = QWidget()
        self.soundPrefWidget = QWidget()

        #GENERAL PREF
        appPrefGrid = QGridLayout()
        n = 0

        self.languageChooserLabel = QLabel(self.tr('Language (requires restart):'))
        appPrefGrid.addWidget(self.languageChooserLabel, n, 0)
        self.languageChooser = QComboBox()
        self.languageChooser.addItems(self.parent().prm['appData']['available_languages'])
        self.languageChooser.setCurrentIndex(self.languageChooser.findText(self.tmpPref['pref']['language']))
        self.languageChooser.currentIndexChanged[int].connect(self.onLanguageChooserChange)
        appPrefGrid.addWidget(self.languageChooser, n, 1)
        n = n+1
        self.countryChooserLabel = QLabel(self.tr('Country (requires restart):'))
        appPrefGrid.addWidget(self.countryChooserLabel, n, 0)
        self.countryChooser = QComboBox()
        self.countryChooser.addItems(self.parent().prm['appData']['available_countries'][self.tmpPref['pref']['language']])
        self.countryChooser.setCurrentIndex(self.countryChooser.findText(self.tmpPref['pref']['country']))
        appPrefGrid.addWidget(self.countryChooser, n, 1)
        n = n+1


        self.defPrmLabel = QLabel(self.tr('Default PRM File:'))
        appPrefGrid.addWidget(self.defPrmLabel, n, 0)
        self.defPrmWidget = QLineEdit(self.tmpPref["pref"]["default_prm_file"])
        appPrefGrid.addWidget(self.defPrmWidget, n, 1)
        self.defPrmButton = QPushButton("Choose")
        self.defPrmButton.clicked.connect(self.onClickDefPrmButton)
        appPrefGrid.addWidget(self.defPrmButton, n, 2)
        n = n+1
        
        self.csvSeparatorLabel = QLabel(self.tr('CSV separator:'))
        appPrefGrid.addWidget(self.csvSeparatorLabel, n, 0)
        self.csvSeparatorWidget = QLineEdit(self.tmpPref["pref"]["csvSeparator"])
        appPrefGrid.addWidget(self.csvSeparatorWidget, n, 1)

        n = n+1

     
        self.appPrefWidget.setLayout(appPrefGrid)
        self.appPrefWidget.layout().setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        
        
        #SOUND PREF
        soundPrefGrid = QGridLayout()

        n = 0
        self.transducersChooser = QComboBox()
        self.transducersChooser.addItems(self.parent().prm["transducers"]["transducersChoices"])
        currTransducerIdx = self.transducersChooser.findText(self.tmpPref['pref']['sound']['transducers'])
        if currTransducerIdx == -1:
            currTransducerIdx = 0
        self.transducersChooser.setCurrentIndex(currTransducerIdx)
        self.transducersChooserLabel = QLabel(self.tr('Transducers:'))
        soundPrefGrid.addWidget(self.transducersChooserLabel, n, 0)
        soundPrefGrid.addWidget(self.transducersChooser, n, 1)
        n = n+1
        
        self.playChooser = QComboBox()
        self.playChooser.addItems(self.parent().prm['appData']['available_play_commands'])
        self.playChooser.setCurrentIndex(self.playChooser.findText(self.tmpPref['pref']['sound']['playCommandType']))
        self.playChooser.currentIndexChanged[int].connect(self.onPlayChooserChange)
        self.playChooserLabel = QLabel(self.tr('Play Command:'))
        soundPrefGrid.addWidget(self.playChooserLabel, n, 0)
        soundPrefGrid.addWidget(self.playChooser, n, 1)
        n = n+1

        self.playCommandLabel = QLabel(self.tr('Command:'))
        soundPrefGrid.addWidget(self.playCommandLabel, n, 0)
        self.playCommandWidget = QLineEdit(self.tmpPref['pref']['sound']['playCommand'])
        if self.playChooser.currentText() != self.tr('custom'):
            self.playCommandWidget.setReadOnly(True)
        soundPrefGrid.addWidget(self.playCommandWidget, n, 1)
        n = n+1
        foo = self.playChooser.currentText()
        if self.tr(foo) != self.tr('custom'):
            self.playCommandLabel.hide()
            self.playCommandWidget.hide()

        #if alsaaudio is selected, provide device list chooser
        if self.parent().prm["appData"]["alsaaudioAvailable"] == True:
            self.alsaaudioPlaybackCardList = self.listAlsaaudioPlaybackCards()
            self.alsaaudioDeviceLabel = QLabel(self.tr('Device:'))
            soundPrefGrid.addWidget(self.alsaaudioDeviceLabel, n, 0)
            self.alsaaudioDeviceChooser = QComboBox()
            self.alsaaudioDeviceChooser.addItems(self.alsaaudioPlaybackCardList)
            self.alsaaudioDeviceChooser.setCurrentIndex(self.alsaaudioDeviceChooser.findText(self.tmpPref["pref"]["sound"]["alsaaudioDevice"]))
            soundPrefGrid.addWidget(self.alsaaudioDeviceChooser, n, 1)
            n = n+1
            if self.tmpPref['pref']['sound']['playCommandType'] != "alsaaudio":
                self.alsaaudioDeviceLabel.hide()
                self.alsaaudioDeviceChooser.hide()

        #if pyaudio is selected, provide device list chooser
        if self.parent().prm["appData"]["pyaudioAvailable"] == True:
            self.listPyaudioPlaybackDevices()
            self.pyaudioDeviceLabel = QLabel(self.tr('Device:'))
            soundPrefGrid.addWidget(self.pyaudioDeviceLabel, n, 0)
            self.pyaudioDeviceChooser = QComboBox()
            self.pyaudioDeviceChooser.addItems(self.pyaudioDeviceListName)
            try:
                self.pyaudioDeviceChooser.setCurrentIndex(self.pyaudioDeviceListIdx.index(self.tmpPref["pref"]["sound"]["pyaudioDevice"]))
            except:
                self.tmpPref["pref"]["sound"]["pyaudioDevice"] = self.pyaudioDeviceListIdx[0]
                self.parent().prm["pref"]["sound"]["pyaudioDevice"] = self.pyaudioDeviceListIdx[0]
                self.pyaudioDeviceChooser.setCurrentIndex(self.pyaudioDeviceListIdx.index(self.tmpPref["pref"]["sound"]["pyaudioDevice"]))
            soundPrefGrid.addWidget(self.pyaudioDeviceChooser, n, 1)
            n = n+1
            if self.tmpPref['pref']['sound']['playCommandType'] != "pyaudio":
                self.pyaudioDeviceLabel.hide()
                self.pyaudioDeviceChooser.hide()

        if self.parent().prm["appData"]["alsaaudioAvailable"] == True or self.parent().prm["appData"]["pyaudioAvailable"] == True:
            self.bufferSizeLabel = QLabel(self.tr('Buffer Size (samples):'))
            soundPrefGrid.addWidget(self.bufferSizeLabel, n, 0)
            self.bufferSizeWidget =  QLineEdit(self.currLocale.toString(self.tmpPref["pref"]["sound"]["bufferSize"]))
            self.bufferSizeWidget.setValidator(QIntValidator(self))
            soundPrefGrid.addWidget(self.bufferSizeWidget, n, 1)
            n = n+1
            if self.tmpPref['pref']['sound']['playCommandType'] not in ["alsaaudio", "pyaudio"]:
                self.bufferSizeLabel.hide()
                self.bufferSizeWidget.hide()

        # self.samplerateLabel = QLabel(self.tr('Default Sampling Rate:'))
        # soundPrefGrid.addWidget(self.samplerateLabel, n, 0)
        # self.samplerateWidget = QLineEdit(self.tmpPref["pref"]["sound"]["defaultSampleRate"])
        # #self.samplerateWidget.setValidator(QIntValidator(self))
        # soundPrefGrid.addWidget(self.samplerateWidget, n, 1)
        # n = n+1

        self.wavmanagerLabel = QLabel(self.tr('WAV Manager (requires restart):'))
        self.wavmanagerChooser = QComboBox()
        self.wavmanagerChooser.addItems(self.parent().prm['appData']['wavmanagers'])
        self.wavmanagerChooser.setCurrentIndex(self.wavmanagerChooser.findText(self.tmpPref['pref']['sound']['wavmanager']))
        soundPrefGrid.addWidget(self.wavmanagerLabel, n, 0)
        soundPrefGrid.addWidget(self.wavmanagerChooser, n, 1)
        # n = n+1
        
        # self.writewav = QCheckBox(self.tr('Write WAV file'))
        # self.writewav.setChecked(self.tmpPref["pref"]["sound"]["writewav"])
        # soundPrefGrid.addWidget(self.writewav, n, 0)
        # n = n+1
        # self.writeParticipantWAVs = QCheckBox(self.tr('Write numbered WAVs for each trial'))
        # self.writeParticipantWAVs.setChecked(self.tmpPref["pref"]["sound"]["writeParticipantWAVs"])
        # soundPrefGrid.addWidget(self.writeParticipantWAVs, n, 0)
        n = n+1

        self.appendSilenceLabel = QLabel(self.tr('Append silence to each sound (ms):'))
        soundPrefGrid.addWidget(self.appendSilenceLabel, n, 0)
        self.appendSilenceWidget = QLineEdit(self.currLocale.toString(self.tmpPref["pref"]["sound"]["appendSilence"]))
        soundPrefGrid.addWidget(self.appendSilenceWidget, n, 1)

        n = n+1
        self.prependSilenceLabel = QLabel(self.tr('Prepend silence to each sound (ms):'))
        soundPrefGrid.addWidget(self.prependSilenceLabel, n, 0)
        self.prependSilenceWidget = QLineEdit(self.currLocale.toString(self.tmpPref["pref"]['sound']["prependSilence"]))
        soundPrefGrid.addWidget(self.prependSilenceWidget, n, 1)
        
        
        self.soundPrefWidget.setLayout(soundPrefGrid)
        self.soundPrefWidget.layout().setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
      
      
        # ........................
        self.tabWidget.addTab(self.appPrefWidget, self.tr("Genera&l"))
        self.tabWidget.addTab(self.soundPrefWidget, self.tr("Soun&d"))

        buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Apply|QDialogButtonBox.StandardButton.Ok|QDialogButtonBox.StandardButton.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        buttonBox.button(QDialogButtonBox.StandardButton.Apply).clicked.connect(self.permanentApply)
        
        layout = QVBoxLayout()
        layout.addWidget(self.tabWidget)
        layout.addWidget(buttonBox)
        self.setLayout(layout)

    def onLanguageChooserChange(self):
        for i in range(self.countryChooser.count()):
            self.countryChooser.removeItem(0)
        self.countryChooser.addItems(self.parent().prm['appData']['available_countries'][self.languageChooser.currentText()])

    def onClickDefPrmButton(self):
        fName = QFileDialog.getOpenFileName(self, self.tr("Find file"), "", self.tr(""))
        if fName[0] != "":
            self.defPrmWidget.setText(fName[0])

    def onPlayChooserChange(self):
        foo = self.playChooser.currentText()
        if self.tr(foo) != self.tr('custom'):
            self.playCommandLabel.hide()
            self.playCommandWidget.hide()
            self.playCommandWidget.setText(foo)
            self.playCommandWidget.setReadOnly(True)
        else:
            self.playCommandWidget.show()
            self.playCommandLabel.show()
            self.playCommandWidget.setReadOnly(False)

        if self.parent().prm["appData"]["alsaaudioAvailable"] == True:
            if foo == "alsaaudio":
                self.alsaaudioDeviceLabel.show()
                self.alsaaudioDeviceChooser.show()
               
            else:
                self.alsaaudioDeviceLabel.hide()
                self.alsaaudioDeviceChooser.hide()
             

        if self.parent().prm["appData"]["pyaudioAvailable"] == True:
            if foo == "pyaudio":
                self.pyaudioDeviceLabel.show()
                self.pyaudioDeviceChooser.show()
            else:
                self.pyaudioDeviceLabel.hide()
                self.pyaudioDeviceChooser.hide()


        if self.parent().prm["appData"]["alsaaudioAvailable"] == True or self.parent().prm["appData"]["pyaudioAvailable"] == True:
            if foo in ["alsaaudio", "pyaudio"]:
                self.bufferSizeLabel.show()
                self.bufferSizeWidget.show()
            else:
                self.bufferSizeLabel.hide()
                self.bufferSizeWidget.hide()
            
    def tryApply(self):

        self.tmpPref['pref']['default_prm_file'] = self.defPrmWidget.text()
        self.tmpPref['pref']['csvSeparator'] = self.csvSeparatorWidget.text()

        self.tmpPref['pref']['sound']['transducers'] = self.transducersChooser.currentText()
        self.tmpPref['pref']['sound']['playCommand'] = self.tr(self.playCommandWidget.text())
        self.tmpPref['pref']['sound']['playCommandType'] = self.tr(self.playChooser.currentText())
        if self.parent().prm["appData"]["alsaaudioAvailable"] == True:
            self.tmpPref['pref']['sound']['alsaaudioDevice'] = self.alsaaudioDeviceChooser.currentText()
        if self.parent().prm["appData"]["pyaudioAvailable"] == True:
            self.tmpPref['pref']['sound']['pyaudioDevice'] =  self.pyaudioDeviceListIdx[self.pyaudioDeviceChooser.currentIndex()]
        self.tmpPref['pref']['sound']['wavmanager'] = str(self.wavmanagerChooser.currentText())
        if self.parent().prm["appData"]["alsaaudioAvailable"] == True or self.parent().prm["appData"]["pyaudioAvailable"] == True:
            self.tmpPref['pref']['sound']['bufferSize'] = self.currLocale.toInt(self.bufferSizeWidget.text())[0]
        ##self.tmpPref['pref']['sound']['defaultSampleRate'] = self.samplerateWidget.text()
        self.tmpPref['pref']['sound']['appendSilence'] = self.currLocale.toInt(self.appendSilenceWidget.text())[0]

        self.tmpPref['pref']['sound']['prependSilence'] = self.currLocale.toInt(self.prependSilenceWidget.text())[0]

        self.tmpPref['pref']['language'] = self.languageChooser.currentText()
        self.tmpPref['pref']['country'] = self.countryChooser.currentText()

        
            
    def revertChanges(self):

        self.defPrmWidget.setText(self.tmpPref['pref']['default_prm_file'])
        self.csvSeparatorWidget.setText(self.tmpPref['pref']['csvSeparator'])
        self.playChooser.setCurrentIndex(self.playChooser.findText(self.tmpPref['pref']['sound']['playCommandType']))
        self.transducersChooser.setCurrentIndex(self.transducersChooser.findText(self.tmpPref['pref']['sound']['transducers']))
        if self.parent().prm["appData"]["alsaaudioAvailable"] == True:
            self.alsaaudioDeviceChooser.setCurrentIndex(self.alsaaudioDeviceChooser.findText(self.tmpPref['pref']['sound']['alsaaudioDevice']))
        if self.parent().prm["appData"]["pyaudioAvailable"] == True:
            self.pyaudioDeviceChooser.setCurrentIndex(self.pyaudioDeviceListIdx.index(self.tmpPref['pref']['sound']['pyaudioDevice']))
        self.wavmanagerChooser.setCurrentIndex(self.wavmanagerChooser.findText(self.tmpPref['pref']['sound']['wavmanager']))
        self.playCommandWidget.setText(self.tmpPref['pref']['sound']['playCommand'])
        if self.parent().prm["appData"]["alsaaudioAvailable"] == True or self.parent().prm["appData"]["pyaudioAvailable"] == True:
            self.bufferSizeWidget.setText(self.currLocale.toString(self.tmpPref['pref']['sound']['bufferSize']))

        self.appendSilenceWidget.setText(self.currLocale.toString(self.tmpPref['pref']['sound']['appendSilence']))
        self.prependSilenceWidget.setText(self.currLocale.toString(self.tmpPref['pref']['sound']['prependSilence']))

        if self.playChooser.currentText() != self.tr('custom'):
            self.playCommandWidget.setReadOnly(True)
       
        self.languageChooser.setCurrentIndex(self.languageChooser.findText(self.tmpPref['pref']['language']))
        self.countryChooser.setCurrentIndex(self.countryChooser.findText(self.tmpPref['pref']['country']))
        
        
    def permanentApply(self):
        self.tryApply()
        
        self.parent().prm['pref'] = copy.deepcopy(self.tmpPref['pref'])
        f = open(self.parent().prm['prefFile'], 'wb')
        pickle.dump(self.parent().prm['pref'], f)
        f.close()
        
    def tabChanged(self):
        self.tryApply()
        if self.tmpPref['pref'] != self.parent().prm['pref']:
            ##print(self.tmpPref['pref'])
            ##print(self.parent().prm['pref'])
            reply = QMessageBox.warning(self, self.tr("Warning"), self.tr('There are unsaved changes. Apply Changes?'), QMessageBox.StandardButton.Yes | 
                                            QMessageBox.StandardButton.No, QMessageBox.StandardButton.Yes)
            if reply == QMessageBox.StandardButton.Yes:
                self.permanentApply()
            else:
                self.tmpPref['pref'] = copy.deepcopy(self.parent().prm['pref'])
                self.revertChanges()


    def listAlsaaudioPlaybackCards(self):
        playbackCardList = alsaaudio.pcms(alsaaudio.PCM_PLAYBACK)
        return playbackCardList
    
    def listPyaudioPlaybackDevices(self):
        self.pyaudioHostApiListName = []
        self.pyaudioHostApiListIdx = []
        self.pyaudioDeviceListName = []
        self.pyaudioDeviceListIdx = []
        paManager = pyaudio.PyAudio()
        nDevices = paManager.get_device_count()
        nApi = paManager.get_host_api_count()
        for i in range(nApi):
            self.pyaudioHostApiListName.append(paManager.get_host_api_info_by_index(i)['name'])
            self.pyaudioHostApiListIdx.append(paManager.get_host_api_info_by_index(i)['index'])
        for i in range(nDevices):
            thisDevInfo = paManager.get_device_info_by_index(i)
            if thisDevInfo["maxOutputChannels"] > 0:
                self.pyaudioDeviceListName.append(thisDevInfo["name"] + ' - ' + self.pyaudioHostApiListName[thisDevInfo["hostApi"]])
                self.pyaudioDeviceListIdx.append(thisDevInfo["index"])
        return 
                
