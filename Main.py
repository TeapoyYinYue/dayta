from appJar import gui
#Constant---------------------------------------------------------

windowSize = "400x200"
LoginButton = "登录"

# title
LoginWindow = "login"
ModeWindow = "mode"
LookWindow = "look"
WriteWindow = "write"
SettingWindow = "setting"
WrongInfoWindow = "wrong"

# end of title
main = gui("MainPage",windowSize)


#---------------Function---------------------------------------------
def subWindow(name):# start window define, the name has to be unique, and better pre-defined
    main.startSubWindow(name)

def subWindowEnd(): # end of window define
    main.stopSubWindow()


def hideWindow(windowTitle):
    main.hideSubWindow(windowTitle, useStopFunction=False)

def showWindow(windowTitle): # this only shows the specified window
    main.showSubWindow(windowTitle, hide=False)

def showWindowHideOthers(windowTitle): # this will hide all other windows
    main.showSubWindow(windowTitle, hide=True)

def getLabelNameForWindow(windowName, labelName): # to obtain the unique id for the label in one specific window
    return windowName + labelName

#default argument    https://stackoverflow.com/questions/43279256/multiple-optional-arguments-python
def setButton(ButtonName, background, width, height, foreground="black", relief="sunken", state="normal"):
    main.setButtonFg(ButtonName, foreground)
    main.setButtonBg(ButtonName, background)
    main.setButtonWidth(ButtonName, width)
    main.setButtonHeight(ButtonName, height)
    main.setButtonRelief(ButtonName, relief)    # One of: "sunken", "raised", "groove", "ridge", "flat"
    main.setButtonState(ButtonName,state)       # One of: "normal", "active", "disabled"
#--------------------------------------------------------------------

main.setBg("white")
main.setFont(18)

#Login Window

LoginPageTitle = "Main"
LoginPageColor = "blue"

def check_user(userName,Password):
    return True

def loginButtonPress(button):
    usr = main.getEntry("用户名")
    pwd = main.getEntry("密码")
    if check_user(usr, pwd):
        showWindow(ModeWindow)
    else:
        #showWindow(WrongInfoWindow)
        main.errorBox('Error','Invalid password')

#def MessageWindowDefine(MessageTitle,Message):

def loginWindowDefine():
    subWindow(LoginWindow)
    main.addLabel(LoginWindow+"title", LoginPageTitle)
    main.setLabelBg(LoginWindow+"title", LoginPageColor)

    main.addLabelEntry("用户名")
    main.addLabelSecretEntry("密码")

    main.addButtons([LoginButton],loginButtonPress)
    setButton(LoginButton,"white",200,100)
    subWindowEnd()


#---endof Login window

#Mode Window

ModePageTitle = "模式"
ModePageColor = "bule"
Modecolor1 = "white"
Modewidth1 = 300
Modehigh1 = 200

WriteButton = "write"
LookButton = "Look"
SettingButton = "setting"
ReturnButton = "return"
def WriteButtonPress(button):
    showWindow(WriteWindow)

def LookButtonPress(button):
    showWindow(LookWindow)

def SettingButtonPress(button):
    showWindow(SettingWindow)

def Return1ButtonPress(button):
    showWindowHideOthers(LoginWindow)

def ModeWindowDefine():
    subWindow(ModeWindow)
    main.addLabel(ModeWindow+"title",ModePageTitle)
    main.setLabelBg(ModeWindow+"title", ModePageColor)

    main.addButtons([WriteButton],WriteButtonPress)
    main.addButtons([LookButton],LookButtonPress)
    main.addButtons([SettingButton],SettingButtonPress)
    main.addButtons([ReturnButton],Return1ButtonPress)

    setButton(WriteButton,Modecolor1,Modewidth1,Modehigh1)
    setButton(LookButton,Modecolor1,Modewidth1,Modehigh1)
    setButton(SettingButton,Modecolor1,Modewidth1,Modehigh1)
    setButton(ReturnButton, Modecolor1, Modewidth1, Modehigh1)

    subWindowEnd()
#---endof Mode window

# Write window

WritePageTitle = "写一写"
WritePageColor = "yellow"
Writecolor1 = "white"
Writewidth1 = 100
Writehigh1 = 100

# ADD
def SubButtonPress(button):
    pass

def ClosePress(button):
    main.hideWindow(ADD)

def ADDWindowDefine():
    subWindow(ADD)
    main.addLabel(getLabelNameForWindow(ADD,"title"),"ADD")
    main.setLabelBg(getLabelNameForWindow(ADD, "title"), "green")


    main.addLabelEntry("时间")
    main.addLabelEntry("地点")
    main.addLabelEntry("事件")
    main.addLabelEntry("备注")

    main.addButtons([SubButton],SubButtonPress)
    main.addButtons([Close], ClosePress)

    subWindowEnd()

def ADDButtonPress(button):
    subWindow(ADD)
    main.addLabel(button+"title", "ADD")
    main.setLabelBg(button+"title", "green")

    main.addLabelEntry("时间")
    main.addLabelEntry("地点")
    main.addLabelEntry("事件")
    main.addLabelEntry("备注")

    main.addButtons([SubButton],SubButtonPress)
    main.addButtons([Close],SubButtonPress)
#---endof ADD window

# DEL
def DELButtonPress(button):
    pass
#---endof DEL window

# Change
def ChangeButtonPress(button):
    pass
#---endof Change window

# New label
def NLButtonPress(button):
    pass
#---endof New label window

def ReturnWButtonPress(button):
    subWindowEnd()
    subWindow(ModeWindow)

def WriteWindowDefine():
    subWindow(WriteWindow)
    main.addLabel(WriteWindow+"title",WritePageTitle)
    main.setLabelBg(WriteWindow+"title", WritePageColor)

    main.addButtons([ADDButton],ADDButtonPress)
    main.addButtons([DELButton],DELButtonPress)
    main.addButtons([ChangeButton],ChangeButtonPress)
    main.addButtons([NLButton],NLButtonPress)
    main.addButtons([ReturnButton],ReturnWButtonPress)

    setButton(ADDButton,Writecolor1,Writewidth1,Writehigh1)
    setButton(DelButton,Writecolor1,Writewidth1,Writehigh1)
    setButton(ChangeButton,Writecolor1,Writewidth1,Writehigh1)
    setButton(NLButton,Writecolor1,Writewidth1,Writehigh1)
    setButton(ReturnWButton, Writecolor1,Writewidth1, Writehigh1)

    subWindowEnd()

#---endof Write window

# Look window

LookPageTitle = "看一看"
LookPageColor = "yellow"
Lookcolor1 = "white"
Lookwidth1 = 100
Lookhigh1 = 100

def SearchButtonPress(button):
    pass

def ReturnLButtonPress(button):
    subWindowEnd()
    subWindow(ModeWindow)

def LookWindowDefine():
    subWindow(LookWindow)
    main.addLabel(LookWindow+"title",LookPageTitle)
    main.setLabelBg(LookWindow+"title", LookPageColor)

    main.addLabelEntry("个人/群组")
    main.addLabelEntry("时间")
    main.addLabelEntry("地点")
    main.addLabelEntry("事件")
    main.addLabelEntry("备注")

    main.addButtons([SearchButton],SearchButtonPress)
    setButton(SearchButton,Lookcolor1,Lookwidth1,Lookhigh1)

    main.addButtons([ReturnButton],ReturnLButtonPress)
    setButton(ReturnLButton)

#---endof Look window

# Setting window

SettingPageTitle = "设置"
SettingPageColor = "yellow"
Settingcolor1 = "white"
Settingwidth1 = 100
Settinghigh1 = 100

def GroupButtonPress(button):
    pass

def ReturnSButtonPress(button):
    subWindowEnd()
    subWindow(ModeWindow)

def SettingWindowDefine():
    subWindow(SettingWindow)
    main.addLabel(SettingWindow+"title",SettingPageTitle)
    main.setLabelBg(SettingWindow+"title", SettingPageColor)

    main.addButtons([GroupButton],GroupButtonPress)
    setButton(GroupButton,Settingcolor1,Settingwidth1,Settinghigh1)

    main.addButtons([ReturnButton],ReturnSButtonPress)
    setButton(ReturnSButton)

#---endof Setting window



def InitWindow():
    loginWindowDefine()
    ModeWindowDefine()
    WriteWindowDefine()
    LookWindowDefine()
    SettingWindowDefine()













#--------end of gui defination---------------ModeWindow-------------------


InitWindow()
main.go()
showWindow(LoginWindow)
