from appJar import gui
#Constant---------------------------------------------------------

windowSize = "400x200"
LoginButton = "登录"

# title
LoginWindow = "login"
ModeWindow = "mode"
WrongInfoWindow = "wrong"


# end of title
main = gui("MainPage",windowSize)


#---------------Function---------------------------------------------
def subWindow(name):
    main.startSubWindow(name)

def subWindowEnd():
    main.stopSubWindow()


def hideWindow(windowTitle):
    main.hideSubWindow(windowTitle, useStopFunction=False)

def showWindow(windowTitle): // this only shows the specified window
    main.showSubWindow(windowTitle, hide=False)

def showWindowHideOthers(windowTitle): // this will hide all other windows
    main.showSubWindow(windowTitle, hide=True)


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
    main.addLabel("title", LoginPageTitle)
    main.setLabelBg("color", LoginPageColor)

    main.addLabelEntry("用户名")
    main.addLabelSecretEntry("密码")

    main.addButtons([LoginButton],loginButtonPress)
    setButton(LoginButton)
    subWindowEnd()


#---endof Login window

#Mode Window

ModePageTitle = "模式"
ModePageColor = "bule"
Mc1 = white
Mw1 = 300
Mh1 = 200

def WriteButtonPress(button):
    subWindow(WriteWindow)

def LookButtonPress(button):
    subWindow(LookWindow)

def SettingButtonPress(button):
    subWindow(SettingWindow)

def Return1ButtonPress(button):
    subWindowEnd()
    subWindow(LoginWindow)

def ModeWindowDefine():
    subWindow(ModeWindow)
    main.addLabel("title",ModePageTitle)
    main.setLabelBg("color", ModePageColor)

    main.addButtons([WriteButton],WriteButtonPress)
    main.addButtons([LookButton],LookButtonPress)
    main.addButtons([SettingButton],SettingButtonPress)
    main.addButtons([ReturnButton],Return1ButtonPress)

    setButton(WriteButton,Mc1,Mw1,Mh1)
    setButton(LookButton,Mc1,Mw1,Mh1)
    setButton(SettingButton,Mc1,Mw1,Mh1)
    setButton(Return1Button)

#---endof Mode window

# Write window

WritePageTitle = "写一写"
WritePageColor = "yellow"
Wc1 = "white"
Ww1 = 100
Wh1 = 100

# ADD
def SubButtonPress(button):
    pass

def ClosePress(button):
    main.hideWindow(ADD)

def ADDButtonPress(button):
    subWindow(ADD)
    main.addLabel("title", "ADD")
    main.setLabelBg("color", "green")

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
    main.addLabel("title",WritePageTitle)
    main.setLabelBg("color", WritePageColor)

    main.addButtons([ADDButton],ADDButtonPress)
    main.addButtons([DELButton],DELButtonPress)
    main.addButtons([ChangeButton],ChangeButtonPress)
    main.addButtons([NLButton],NLButtonPress)
    main.addButtons([ReturnButton],ReturnWButtonPress)

    setButton(ADDButton,Wc1,Ww1,Wh1)
    setButton(DelButton,Wc1,Ww1,Wh1)
    setButton(ChangeButton,Wc1,Ww1,Wh1)
    setButton(NLButton,Wc1,Ww1,Wh1)
    setButton(ReturnWButton)

#---endof Write window

# Look window

LookPageTitle = "看一看"
LookPageColor = "yellow"
Lc1 = "white"
Lw1 = 100
Lh1 = 100

def SearchButtonPress(button):
    pass

def ReturnLButtonPress(button):
    subWindowEnd()
    subWindow(ModeWindow)

def LookWindowDefine():
    subWindow(LookWindow)
    main.addLabel("title",LookPageTitle)
    main.setLabelBg("color", LookPageColor)

    main.addLabelEntry("个人/群组")
    main.addLabelEntry("时间")
    main.addLabelEntry("地点")
    main.addLabelEntry("事件")
    main.addLabelEntry("备注")

    main.addButtons([SearchButton],SearchButtonPress)
    setButton(SearchButton,Lc1,Lw1,Lh1)

    main.addButtons([ReturnButton],ReturnLButtonPress)
    setButton(ReturnLButton)

#---endof Look window

# Setting window

SettingPageTitle = "设置"
SettingPageColor = "yellow"
Sc1 = "white"
Sw1 = 100
Sh1 = 100

def GroupButtonPress(button):
    pass

def ReturnSButtonPress(button):
    subWindowEnd()
    subWindow(ModeWindow)

def SettingWindowDefine():
    subWindow(SettingWindow)
    main.addLabel("title",SettingPageTitle)
    main.setLabelBg("color", SettingPageColor)

    main.addButtons([GroupButton],GroupButtonPress)
    setButton(GroupButton,Sc1,Sw1,Sh1)

    main.addButtons([ReturnButton],ReturnSButtonPress)
    setButton(ReturnSButton)

#---endof Setting window
















#--------end of gui defination----------------------------------

main.go()
