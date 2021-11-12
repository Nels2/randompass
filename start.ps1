$usr= ((Get-WMIObject -ClassName Win32_ComputerSystem).Username).Split('\')[1]
Function pwrg {python C:\Users\$usr\Downloads\randompass-main\Rpass.py}
Set-Alias -Name pwg -Value pwrg
pwg
Start-Sleep -Seconds 120
