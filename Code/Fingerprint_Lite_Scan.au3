$sTextFile = "D:\SOUL System\GUI 3-2-18\Arrival\RowID.txt"
Local $arr = Fileread($sTextFile)
run("D:\\SOUL System\\GUI 3-2-18\\Arrival\\SFGDemoV2.0\\SFGDemo.exe")
winwaitactive("SFG Demo")
send("+O")
winwaitactive("Open Device")
send("{TAB}")
send("{TAB}")
send("{DOWN}")
send("{DOWN}")
;send("{DOWN}")
send("{TAB}")
send("{ENTER}")
winwaitactive("SFG Demo")
send("{TAB 24}")
send("{SPACE}")
winwaitactive("Capture fingerprint")
send("{TAB}")
send("1")
send("{TAB}")
send("D:\SOUL System\GUI 3-2-18\ImageDB\Sample")
send("{TAB 4}")
send($arr)
send("{TAB}")
send("{ENTER}")
sleep(20000)
send("{TAB}")
send("{TAB}")
send("{ENTER}")
WinWaitActive("SFG Demo")
WinClose ("SFG Demo")