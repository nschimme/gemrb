#character generation (GUICG 0)
import GemRB

CharGenWindow = 0
TextAreaControl = 0

def OnLoad():
	global CharGenWindow, TextAreaControl

	GemRB.LoadWindowPack("GUICG", 640, 480)
	CharGenWindow = GemRB.LoadWindow(0)
	PortraitButton = GemRB.GetControl(CharGenWindow, 12)
	GemRB.SetButtonFlags(CharGenWindow, PortraitButton, IE_GUI_BUTTON_PICTURE|IE_GUI_BUTTON_NO_IMAGE,OP_SET)
	PortraitName = GemRB.GetToken ("LargePortrait")
	GemRB.SetButtonPicture (CharGenWindow,PortraitButton,PortraitName,"NOPORTMD")

	RaceTable = GemRB.LoadTable("races")
	ClassTable = GemRB.LoadTable("classes")
	KitTable = GemRB.LoadTable("kitlist")
	AlignmentTable = GemRB.LoadTable("aligns")
	AbilityTable = GemRB.LoadTable("ability")

	GenderButton = GemRB.GetControl(CharGenWindow,0)
	GemRB.SetText(CharGenWindow,GenderButton,11956)
	GemRB.SetButtonState(CharGenWindow,GenderButton,IE_GUI_BUTTON_DISABLED)

	RaceButton = GemRB.GetControl(CharGenWindow,1)
	GemRB.SetText(CharGenWindow,RaceButton, 11957)
	GemRB.SetButtonState(CharGenWindow,RaceButton,IE_GUI_BUTTON_DISABLED)

	ClassButton = GemRB.GetControl(CharGenWindow,2)
	GemRB.SetText(CharGenWindow,ClassButton, 11959)
	GemRB.SetButtonState(CharGenWindow,ClassButton,IE_GUI_BUTTON_DISABLED)

	AlignmentButton = GemRB.GetControl(CharGenWindow,3)
	GemRB.SetText(CharGenWindow,AlignmentButton, 11958)
	GemRB.SetButtonState(CharGenWindow,AlignmentButton,IE_GUI_BUTTON_DISABLED)

	AbilitiesButton = GemRB.GetControl(CharGenWindow,4)
	GemRB.SetText(CharGenWindow,AbilitiesButton, 11960)
	GemRB.SetButtonState(CharGenWindow,AbilitiesButton,IE_GUI_BUTTON_DISABLED)

	SkillButton = GemRB.GetControl(CharGenWindow,5)
	GemRB.SetText(CharGenWindow,SkillButton, 17372)
	GemRB.SetButtonState(CharGenWindow,SkillButton,IE_GUI_BUTTON_DISABLED)

	AppearanceButton = GemRB.GetControl(CharGenWindow,6)
	GemRB.SetText(CharGenWindow,AppearanceButton, 11961)
	GemRB.SetButtonState(CharGenWindow,AppearanceButton,IE_GUI_BUTTON_ENABLED)
	GemRB.SetButtonFlags(CharGenWindow,AppearanceButton, IE_GUI_BUTTON_DEFAULT,OP_OR)

	NameButton = GemRB.GetControl(CharGenWindow,7)
	GemRB.SetText(CharGenWindow,NameButton, 11963)
	GemRB.SetButtonState(CharGenWindow,NameButton,IE_GUI_BUTTON_DISABLED)

	BackButton = GemRB.GetControl(CharGenWindow, 11)
	GemRB.SetText(CharGenWindow, BackButton, 15416)
	GemRB.SetButtonState(CharGenWindow,BackButton,IE_GUI_BUTTON_ENABLED)

	AcceptButton = GemRB.GetControl(CharGenWindow, 8)
	GemRB.SetText(CharGenWindow, AcceptButton, 11962)
	GemRB.SetButtonState(CharGenWindow,AcceptButton,IE_GUI_BUTTON_DISABLED)

	ImportButton = GemRB.GetControl(CharGenWindow, 13)
	GemRB.SetText(CharGenWindow, ImportButton, 13955)
	GemRB.SetButtonState(CharGenWindow,ImportButton,IE_GUI_BUTTON_DISABLED)

	CancelButton = GemRB.GetControl(CharGenWindow, 15)
	GemRB.SetText(CharGenWindow, CancelButton, 8159)
	GemRB.SetButtonState(CharGenWindow,CancelButton,IE_GUI_BUTTON_ENABLED)

	BiographyButton = GemRB.GetControl(CharGenWindow, 16)
	GemRB.SetText(CharGenWindow, BiographyButton, 18003)
	GemRB.SetButtonState(CharGenWindow,BiographyButton,IE_GUI_BUTTON_DISABLED)
	TextAreaControl= GemRB.GetControl(CharGenWindow,9)
	GemRB.SetText(CharGenWindow, TextAreaControl, "[capital=0]" + GemRB.GetString(12135))
	GemRB.TextAreaAppend(CharGenWindow, TextAreaControl,": ")
	if GemRB.GetVar("Gender") == 1:
		GemRB.TextAreaAppend(CharGenWindow, TextAreaControl, 1050)
	else:
		GemRB.TextAreaAppend(CharGenWindow, TextAreaControl, 1051)
	GemRB.TextAreaAppend(CharGenWindow, TextAreaControl,1048,-1) # new line
	GemRB.TextAreaAppend(CharGenWindow, TextAreaControl,": ")
	GemRB.TextAreaAppend(CharGenWindow, TextAreaControl,GemRB.GetTableValue(RaceTable,GemRB.GetVar("Race")-1,2))
	GemRB.TextAreaAppend(CharGenWindow, TextAreaControl,12136, -1)
	GemRB.TextAreaAppend(CharGenWindow, TextAreaControl,": ")
	KitIndex = GemRB.GetVar("Class Kit")
	if KitIndex == 0:
		GemRB.TextAreaAppend(CharGenWindow, TextAreaControl,GemRB.GetTableValue(ClassTable,GemRB.GetVar("Class")-1,2))
	else:
		GemRB.TextAreaAppend(CharGenWindow, TextAreaControl, GemRB.GetTableValue(KitTable, KitIndex,2) )
	GemRB.TextAreaAppend(CharGenWindow, TextAreaControl,1049, -1)
	GemRB.TextAreaAppend(CharGenWindow, TextAreaControl,": ")
	v = GemRB.FindTableValue(AlignmentTable,3,GemRB.GetVar("Alignment"))
	GemRB.TextAreaAppend(CharGenWindow, TextAreaControl,GemRB.GetTableValue(AlignmentTable,v,2))
	for i in range(6):
		v = GemRB.GetTableValue(AbilityTable, i,2)
		GemRB.TextAreaAppend(CharGenWindow, TextAreaControl, v, -1)
		GemRB.TextAreaAppend(CharGenWindow, TextAreaControl,": "+str(GemRB.GetVar("Ability "+str(i))))

	GemRB.SetEvent(CharGenWindow, CancelButton, IE_GUI_BUTTON_ON_PRESS, "CancelPress")
	GemRB.SetEvent(CharGenWindow, BackButton, IE_GUI_BUTTON_ON_PRESS, "BackPress")
	GemRB.SetEvent(CharGenWindow, AppearanceButton, IE_GUI_BUTTON_ON_PRESS, "NextPress")
	GemRB.SetVisible(CharGenWindow,1)
	return
	
def NextPress():
	GemRB.UnloadWindow(CharGenWindow)
	GemRB.SetNextScript("GUICG13") #colors
	return

def CancelPress():
	GemRB.UnloadWindow(CharGenWindow)
	GemRB.SetNextScript("CharGen")
	return

def BackPress():
	GemRB.UnloadWindow(CharGenWindow)
	GemRB.SetNextScript("CharGen6") #skills
	return

