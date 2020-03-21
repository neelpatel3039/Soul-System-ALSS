#include <AutoItConstants.au3>
#include <FileConstants.au3>
#include <MsgBoxConstants.au3>
#include <WinAPIFiles.au3>
$sFilePath = "D:\\SOUL System\\GUI 3-2-18\\Arrival\\Bag_check.txt"
Local $hFileOpen = FileOpen($sFilePath, 2)
run("D:\\SOUL System\\GUI 3-2-18\\Arrival\\Decoder\\Decoder.exe")
MouseClick($MOUSE_CLICK_LEFT, 580, 150)
; 464, 90 fro webcam scan
Sleep(10000)
MouseClick($MOUSE_CLICK_LEFT, 860, 222)
Sleep(1000)
MouseClick($MOUSE_CLICK_LEFT, 1111, 647))
$svalue = ClipGet()
  ; Write data to the file using the handle returned by FileOpen.
    FileWrite($hFileOpen, $svalue)

    ; Close the handle returned by FileOpen.
    FileClose($hFileOpen)
WinWaitActive("CodeTwo QR Code Desktop Reader & Generator 1.1.1.17")
WinClose("CodeTwo QR Code Desktop Reader & Generator 1.1.1.17")
