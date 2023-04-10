# Prune of PlatformOperationLog and NotificationMessage tables

The recommended retention period for PlatformOperationLog and NotificationMessage is 45 days. This is usually enough to find the reason for the issues. Create a task and run it either nightly or weekly.

```sql
param(
    [parameter(Mandatory=$True)]
	[string] $SqlServer,

    [parameter(Mandatory=$True)]
	[string] $Database,

	[parameter(Mandatory=$False)]
	[string] $SQLCredentialName = 'sqlcreds',
		
	[parameter(Mandatory=$False)]
	[int] $daysBefore = 730,

    [parameter(Mandatory=$False)]
	[int] $processRowsCount = 100,

	[parameter(Mandatory=$False)]
	[int] $SqlServerPort = 1433,

    [parameter(Mandatory=$False)]
	[int] $tableNames = 'PlatformOperationLog,NotificationMessage',

    [parameter(Mandatory=$False)]
	[int] $VerboseOutput = 0,

	[parameter(Mandatory=$False)]
	[int] $ConnectionTimeout = 120
)

$SqlCredential = Get-AutomationPSCredential -Name $SQLCredentialName

if ($null -eq $SqlCredential)
{
    throw "Could not retrieve '$SQLCredentialName' credential asset. Check that you created this first in the Automation service."
}

$SqlUsername = $SqlCredential.UserName 
$SqlPass = $SqlCredential.GetNetworkCredential().Password

$sw = [Diagnostics.Stopwatch]::StartNew()
#Install-Module SqlServer -Scope CurrentUser -force -allowClobber
$tableNameArray = $tableNames.Split(',')
foreach ($tableName in $tableNameArray) {
    $thresholdDate = (get-date).AddDays(-$daysBefore)
    $sqlQuery = @"
SELECT TOP $processRowsCount Id FROM [dbo].[$tableName] WHERE CreatedDate < '$thresholdDate' ORDER BY CreatedDate
"@
    Write-Output "Parameters set to remove $processRowsCount rows from $tableName table in $Database database with created date < $thresholdDate"
    $records = @()
    try {
        $records = Invoke-Sqlcmd -ServerInstance $SqlServer -Database $Database -Username $SqlUsername -Password $SqlPass -Query $sqlQuery -ConnectionTimeout $ConnectionTimeout
    } catch {
        Write-Error "$error"
        throw "$error"
    }
    if ($records.count -eq 0) { Write-Output "No records found fitting the parameters"}
    $c = 0
    foreach ($entry in $records) {
        if ($VerboseOutput -eq 1){Write-Output "Removing record with Id $($records[$c].Id)"}
        $sqlQuery2 = @"
DELETE FROM [dbo].[$tableName] WHERE Id = '$($records[$c].Id)'
"@
        try {
            Invoke-Sqlcmd -ServerInstance $SqlServer -Database $Database -Username $SqlUsername -Password $SqlPass -Query $sqlQuery2 -ConnectionTimeout $ConnectionTimeout
        } catch {
            Write-Error "$error"
            throw "$error"
        }
        $c = $c + 1
    }
    Write-Output "Removed $c rows"
}
$sw.Stop()
Write-Output "Total Run Time: $($sw.Elapsed.ToString('hh\:mm\:ss\.fff'))"
```