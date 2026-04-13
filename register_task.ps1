$action   = New-ScheduledTaskAction -Execute 'C:\Python312\python.exe' `
                -Argument 'C:\Users\marc0\win-monitor\agent.py' `
                -WorkingDirectory 'C:\Users\marc0\win-monitor'

$trigger  = New-ScheduledTaskTrigger -AtLogOn -User 'marc0'

$settings = New-ScheduledTaskSettingsSet `
                -ExecutionTimeLimit ([TimeSpan]::Zero) `
                -RestartCount 5 `
                -RestartInterval (New-TimeSpan -Minutes 1) `
                -StartWhenAvailable

Register-ScheduledTask `
    -TaskName    'WinMonitorAgent' `
    -Action      $action `
    -Trigger     $trigger `
    -Settings    $settings `
    -Description 'Windows Event Log Monitor — envía errores al servidor corillo' `
    -RunLevel    Highest `
    -Force

Write-Host "Tarea registrada OK"
