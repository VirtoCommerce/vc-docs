# List all versions for documentation subsites
#
# Usage:
#   .\scripts\list-versions.ps1
#   .\scripts\list-versions.ps1 -SubsitePath "marketplace/developer-guide"
#
# Parameters:
#   -SubsitePath: Optional path to specific subsite to list versions for

param(
    [Parameter(Mandatory=$false)]
    [ValidateSet(
        "marketplace/developer-guide",
        "marketplace/user-guide",
        "platform/developer-guide",
        "platform/user-guide",
        "platform/deployment-on-cloud",
        "storefront/developer-guide",
        "storefront/user-guide"
    )]
    [string]$SubsitePath = ""
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

function Write-ErrorMsg {
    param([string]$Message)
    Write-Host $Message -ForegroundColor Red
}

function Write-Header {
    param([string]$Message)
    Write-Host "`n$Message" -ForegroundColor Yellow
    Write-Host ("=" * $Message.Length) -ForegroundColor Yellow
}

# Validate mike is installed
$mikeInstalled = Get-Command mike -ErrorAction SilentlyContinue
if (-not $mikeInstalled) {
    Write-ErrorMsg "Error: mike is not installed. Please install it using: pip install mike"
    exit 1
}

# Define all subsites
$subsites = @(
    "marketplace/developer-guide",
    "marketplace/user-guide",
    "platform/developer-guide",
    "platform/user-guide",
    "platform/deployment-on-cloud",
    "storefront/developer-guide",
    "storefront/user-guide"
)

# If specific subsite is requested, use only that one
if ($SubsitePath -ne "") {
    $subsites = @($SubsitePath)
}

Write-Info "`nListing versions for documentation subsites..."
Write-Host ""

foreach ($subsite in $subsites) {
    $configPath = "$subsite/mkdocs.yml"

    # Check if config exists
    if (-not (Test-Path $configPath)) {
        Write-ErrorMsg "Warning: Configuration not found at $configPath - skipping"
        continue
    }

    Write-Header $subsite

    # Get versions using mike list
    $mikeCmd = "mike list -F $configPath --deploy-prefix $subsite"

    try {
        $output = Invoke-Expression $mikeCmd 2>&1

        if ($LASTEXITCODE -eq 0) {
            if ($output) {
                Write-Host $output
            } else {
                Write-Host "  No versions deployed yet" -ForegroundColor Gray
            }
        } else {
            Write-Host "  No versions deployed yet" -ForegroundColor Gray
        }
    } catch {
        Write-Host "  No versions deployed yet" -ForegroundColor Gray
    }
}

Write-Host ""
Write-Info "To deploy a new version, use:"
Write-Host "  .\scripts\deploy-version.ps1 -SubsitePath <path> -Version <version> -Alias <alias>" -ForegroundColor Gray
Write-Host ""

