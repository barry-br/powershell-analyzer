#Variables
$Date = Get-Date
$TempReport = $env:TEMP + "\\temp.csv"
$FinalReport = $env:USERPROFILE + "\\" + $Date.Year + "_" + $Date.Month + "_" + $Date.Day + "_" + $Date.Hour + ":" + $Date.Minute + "_Scheduled_Task_Report.csv"

$title = Write-Host "Scheduled Task Reporter" -ForegroundColor green
$message = Write-Host "Which servers would you like to report on?" -ForegroundColor yellow

$EXIT = New-Object System.Management.Automation.Host.ChoiceDescription "&Exit", `
    "Exits the script. . . "

$ALL = New-Object System.Management.Automation.Host.ChoiceDescription "&All Server Report", `
    "Queries for all SERVERS in the domain and reports on their scheduled tasks."

$SRV = New-Object System.Management.Automation.Host.ChoiceDescription "&Single Host Report", `
    "Queries for the exact server or workstation name entered."

$OTHR = New-Object System.Management.Automation.Host.ChoiceDescription "A&NR Report", `
    "Peforms an ANR (Ambiguous Name Request) lookup.  ANR allows you to do a report against one or more computers by typing part of the computer name."

$options = [System.Management.Automation.Host.ChoiceDescription[]]($EXIT, $ALL, $SRV, $OTHR)

$result = $host.ui.PromptForChoice($title, $message, $options, 0) 

switch ($result)
    {
        0	{Write-Host "No selection made. Exiting script. . ."}
		1	{Get-QADComputer -sizelimit 0| Where {$_.osname -like "*Server*"} | Sort | % {schtasks /query /s $_.name /FO CSV /V | where {$_.length -gt 0} > $TempReport }}
        2	{$Computer = Read-Host -Prompt "Enter the server name"
			 Get-QADComputer $Computer | Sort | % {schtasks /query /s $_.name /FO CSV /V | where {$_.length -gt 0} > $TempReport}} # | set-content 'export-csv $outputdestination'}}
		3	{$Search = Read-Host -Prompt "Type all or part of the computer name"
			 Get-QADComputer -ANR $Search | ForEach-Object {schtasks /query /s $_.name /FO CSV /V | where {$_.length -gt 0} > $TempReport}}
