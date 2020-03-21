$sTextFile = "D:\SOUL System\GUI 3-2-18\Arrival\Folder_name.txt"
;$sFolderPath = "D:\\SOUL System\\GUI 3-2-18\\ImageDB\\"
Local $arr = Fileread($sTextFile)
;$sFolderPath = $sFolderPath + $arr
Global $mylist[3] = ["4","5","6"]
run("D:\\SOUL System\\GUI 3-2-18\\Arrival\\SFGDemo.exe")
WinWaitActive("SFG Demo")
Send("+o")
WinWaitActive("Open Device")
Send("{TAB}")
Send("{TAB}")
Send("{DOWN}")
Send("{DOWN}")
;Send("{DOWN}")
Send("{TAB}")
Send("{ENTER}")
Send("{TAB 24}")
Send("{SPACE}")
WinWaitActive("Capture fingerprint")
Send("{TAB}")
Send("3")
Send("{TAB}")
Send($arr)
Send("{TAB 4}")
For $i = 0 to 3 - 1
;Sleep(20000)
Send($mylist[$i])
Send("{TAB}")
Send("{ENTER}")
Sleep(15000)
Send("{TAB 8}")
Next
Sleep(15000)
WinWaitActive("Capture fingerprint")
WinClose("Capture fingerprint")
WinWaitActive("SFG Demo")
WinClose("SFG Demo")







