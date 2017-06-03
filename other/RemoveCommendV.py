#! C:\python3.6\python.exe
# -*- coding: utf-8 -*-

import sys
import os
import re

class RemoveCommendV(object) :
    def _ErrorPrint(self, ErrorInfo = None, ErrorLevel = None, ErrorInfoSuffix = "\nplease check!!!") :
        if ErrorLevel == None :
            ErrorLevel = "SPRD_Error>>>"
        else :
            ErrorLevel = "SPRD_Error" + str(ErrorLevel) + ">>>"

        info = ErrorLevel + str(ErrorInfo)
        if ErrorInfoSuffix == None :
            info = info + "\n"
        else :
            info = info + str(ErrorInfoSuffix) + "\n"
        if ErrorLevel not in self.ErrorInfo.keys() :
            self.ErrorInfo[ErrorLevel] = []
        self.ErrorInfo[ErrorLevel].append(ErrorInfo)
        print (info)
    def __init__(self, FileName, WriteOut = True, WriteOutName = None, InsteadOfSpace = False,PrintOutCommend = True, WriteOutCommend = False, WriteOutCommendName = None) :
        self.FileName = FileName
        self.WriteOut = WriteOut
        self.WriteOutName = WriteOutName
        self.InsteadOfSpace = InsteadOfSpace
        self.PrintOutCommend = PrintOutCommend
        self.WriteOutCommend = WriteOutCommend
        self.WriteOutCommendName = WriteOutCommendName
        self.ErrorInfo = {}

        if self.WriteOut and self.WriteOutName == None :
            self.WriteOutName = "Output.v"
            info = "please give me WriteOutName when __init__ instead of " + self.WriteOutName
            self._ErrorPrint(ErrorInfo = info, ErrorLevel = None, ErrorInfoSuffix = None)
        if self.WriteOutCommend and self.WriteOutCommendName == None :
            self.WriteOutCommendName = "OutputCommmend.v"
            info = "please give me WriteOutCommendName when __init__ instead of " + self.WriteOutCommendName
            self._ErrorPrint(ErrorInfo = inof, ErrorLevel = None, ErrorInfoSuffix = None)
    def ReadFileByLine(self) :
        with open(self.WriteOutName, "w") as OutputFile :
            with open(self.FileName, "r") as InputFile :
                print ("-------------start remove commend------------------")
                SSbetweenSSFlag = False # SlashStarBetweenStarSlashFlag
                while True :
                    InputFileLine = InputFile.readline()
                    if InputFileLine == "" :
                        break
                    EnableLoop = True
                    while EnableLoop :
                        EnableLoop = False
                        DoubleSlashPoint = InputFileLine.find("//")
                        SlashStarPoint   = InputFileLine.find("/*")
                        StarSlashPoint   = InputFileLine.find("*/")
                        if (DoubleSlashPoint != -1) and ((SlashStarPoint == -1) or (DoubleSlashPoint <= SlashStarPoint))  and (not SSbetweenSSFlag) :
                            InputFileLine = InputFileLine[:DoubleSlashPoint]
                        elif ((DoubleSlashPoint == -1) or (DoubleSlashPoint > SlashStarPoint)) and (not SSbetweenSSFlag) and (SlashStarPoint != -1) :
                            print ("SlashStarPoint+2 =", SlashStarPoint+2)
                            StarSlashPoint = InputFileLine[SlashStarPoint+2:].find("*/")
                            if StarSlashPoint == -1 :
                                SSbetweenSSFlag = True
                                InputFileLine = InputFileLine[:SlashStarPoint]
                            else :
                                InputFileLine = InputFileLine[:SlashStarPoint] + InputFileLine[SlashStarPoint+StarSlashPoint+4:]
                                EnableLoop = True
                        elif (SSbetweenSSFlag) :
                            if StarSlashPoint != -1 :
                                SSbetweenSSFlag = False
                                EnableLoop = True
                                InputFileLine = InputFileLine[StarSlashPoint+2:]
                            else :
                                InputFileLine = ""
                    if InputFileLine != "" :
                        OutputFile.write(InputFileLine + "\n")
            print ("-------------end remove commend--------------------")
if __name__ == "__main__" :
    print("-------------python code start---------------------")
    RemoveCommendV_C = RemoveCommendV("example.v")
    RemoveCommendV_C.ReadFileByLine()
    print("-------------python code end-----------------------")
