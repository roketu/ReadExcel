import os

def getOpenAIkey():
    '''open()関数でファイルを開きます。'''
    fileobj = open("key.txt")

    '''read()メソッドでファイルを読み込みます。'''
    key = fileobj.read()
    
    '''close()メソッドでファイルを閉じます。'''
    fileobj.close()

    return key
 
