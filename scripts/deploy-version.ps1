# Deploy specific version for a documentation subsite using Mike
#
# Usage:
#   .\scripts\deploy-version.ps1 -SubsitePath "marketplace/developer-guide" -Version "1.0" -Alias "latest"
#   .\scripts\deploy-version.ps1 -SubsitePath "platform/user-guide" -Version "2.5"
#
# Parameters:
#   -SubsitePath: Path to subsite (e.g., "marketplace/developer-guide")
#   -Version: Version number (e.g., "1.0", "2.5", "3.2025-S13")
#   -Alias: Optional alias (e.g., "latest", "stable")
#   -SetDefault: Optional switch to set this version as default

param(
    [Parameter(Mandatory=$true)]
    [ValidateSet(
        "marketplace/developer-guide",
        "marketplace/user-guide",
        "platform/developer-guide",
        "platform/user-guide",
        "platform/deployment-on-cloud",
        "storefront/developer-guide",
        "storefront/user-guide"
    )]
    [string]$SubsitePath,

    [Parameter(Mandatory=$true)]
    [string]$Version,

    [Parameter(Mandatory=$false)]
    [string]$Alias = "",

    [Parameter(Mandatory=$false)]
    [switch]$SetDefault = $false,

    [Parameter(Mandatory=$false)]
    [switch]$UpdateAliases = $false
)

# Color output functions
function Write-Success {
    param([string]$Message)
    Write-Host $Message -ForegroundColor Green
}

function Write-Info {
    param([string]$Message)
    Write-Host $Message -ForegroundColor Cyan
}

function Write-Warning {
    param([string]$Message)
    Write-Host $Message -ForegroundColor Yellow
}

function Write-ErrorMsg {
    param([string]$Message)
    Write-Host $Message -ForegroundColor Red
}

# Validate mike is installed
Write-Info "Checking if mike is installed..."
$mikeInstalled = Get-Command mike -ErrorAction SilentlyContinue
if (-not $mikeInstalled) {
    Write-ErrorMsg "Error: mike is not installed. Please install it using: pip install mike"
    exit 1
}
Write-Success "✓ Mike is installed"

# Validate mkdocs.yml exists for subsite
$configPath = "$SubsitePath/mkdocs.yml"
if (-not (Test-Path $configPath)) {
    Write-ErrorMsg "Error: Configuration file not found at $configPath"
    exit 1
}
Write-Success "✓ Configuration file found: $configPath"

# Build the mike deploy command
$mikeCmd = "mike deploy -F $configPath --deploy-prefix $SubsitePath"

# Add version
$mikeCmd += " $Version"

# Add alias if provided
if ($Alias -ne "") {
    $mikeCmd += " $Alias"
}

# Add update aliases flag if set
if ($UpdateAliases) {
    $mikeCmd += " --update-aliases"
}

# Execute mike deploy
Write-Info "`nDeploying version $Version for $SubsitePath..."
Write-Host "Command: $mikeCmd" -ForegroundColor Gray
Write-Host ""

Invoke-Expression $mikeCmd

if ($LASTEXITCODE -eq 0) {
    Write-Success "`n✓ Successfully deployed version $Version for $SubsitePath"

    # Set as default if requested
    if ($SetDefault) {
        Write-Info "`nSetting version $Version as default..."
        $setDefaultCmd = "mike set-default -F $configPath --deploy-prefix $SubsitePath $Version"
        Invoke-Expression $setDefaultCmd

        if ($LASTEXITCODE -eq 0) {
            Write-Success "✓ Successfully set version $Version as default"
        } else {
            Write-ErrorMsg "✗ Failed to set default version"
            exit 1
        }
    }

    Write-Info "`nDeployment Summary:"
    Write-Host "  Subsite:  $SubsitePath" -ForegroundColor White
    Write-Host "  Version:  $Version" -ForegroundColor White
    if ($Alias -ne "") {
        Write-Host "  Alias:    $Alias" -ForegroundColor White
    }
    if ($SetDefault) {
        Write-Host "  Default:  Yes" -ForegroundColor White
    }
    Write-Host ""
    Write-Info "To test locally:"
    Write-Host "  1. Development (without versions): cd $SubsitePath && mkdocs serve" -ForegroundColor Gray
    Write-Host "  2. View deployed versions: git checkout gh-pages && python -m http.server 8000" -ForegroundColor Gray
    Write-Host "     Then open: http://localhost:8000/$SubsitePath" -ForegroundColor Gray
    Write-Host ""
} else {
    Write-ErrorMsg "`n✗ Failed to deploy version $Version for $SubsitePath"
    exit 1
}

