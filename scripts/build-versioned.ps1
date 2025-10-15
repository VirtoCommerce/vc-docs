# Build and deploy all versioned documentation subsites using Mike
#
# This script is for production deployment with versioning.
# For development builds without versioning, use the root build.ps1 script.
#
# Usage:
#   .\scripts\build-versioned.ps1 -Version "3.2025-S13"
#   .\scripts\build-versioned.ps1 -Version "3.2025-S13" -SetAsLatest
#   .\scripts\build-versioned.ps1 -Version "3.2025-S13" -SetAsLatest -SetAsDefault
#
# Parameters:
#   -Version: Version number to deploy (e.g., "3.2025-S13", "1.0", "2.5")
#   -SetAsLatest: Set this version as 'latest' alias
#   -SetAsDefault: Set this version as default version
#   -SubsitesOnly: Deploy only subsites (skip root and intermediate sites)

param(
    [Parameter(Mandatory=$true)]
    [string]$Version,

    [Parameter(Mandatory=$false)]
    [switch]$SetAsLatest = $false,

    [Parameter(Mandatory=$false)]
    [switch]$SetAsDefault = $false,

    [Parameter(Mandatory=$false)]
    [switch]$SubsitesOnly = $false
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

function Write-Step {
    param([string]$Message)
    Write-Host "`n═══════════════════════════════════════════════════" -ForegroundColor Blue
    Write-Host "  $Message" -ForegroundColor White
    Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Blue
}

# Validate mike is installed
Write-Info "Validating prerequisites..."
$mikeInstalled = Get-Command mike -ErrorAction SilentlyContinue
if (-not $mikeInstalled) {
    Write-ErrorMsg "Error: mike is not installed. Please install it using: pip install mike"
    exit 1
}

$mkdocsInstalled = Get-Command mkdocs -ErrorAction SilentlyContinue
if (-not $mkdocsInstalled) {
    Write-ErrorMsg "Error: mkdocs is not installed. Please install it using: pip install mkdocs-material"
    exit 1
}

Write-Success "✓ Prerequisites validated"

# Define all versioned subsites
$versionedSubsites = @(
    @{ Path = "marketplace/developer-guide"; Name = "Marketplace Developer Guide" },
    @{ Path = "marketplace/user-guide"; Name = "Marketplace User Guide" },
    @{ Path = "platform/developer-guide"; Name = "Platform Developer Guide" },
    @{ Path = "platform/user-guide"; Name = "Platform User Guide" },
    @{ Path = "platform/deployment-on-cloud"; Name = "Platform Deployment on Cloud" },
    @{ Path = "storefront/developer-guide"; Name = "Storefront Developer Guide" },
    @{ Path = "storefront/user-guide"; Name = "Storefront User Guide" }
)

# Counter for tracking
$totalSubsites = $versionedSubsites.Count
$deployedCount = 0
$failedCount = 0
$failedSubsites = @()

Write-Info "`nDeployment Plan:"
Write-Host "  Version:        $Version"
Write-Host "  Set as latest:  $SetAsLatest"
Write-Host "  Set as default: $SetAsDefault"
Write-Host "  Subsites:       $totalSubsites"
Write-Host ""

# Build non-versioned sites first (if not subsites only)
if (-not $SubsitesOnly) {
    Write-Step "Building Non-Versioned Sites"

    Write-Info "Building root site..."
    mkdocs build -d ./site
    if ($LASTEXITCODE -eq 0) {
        Write-Success "✓ Root site built"
    } else {
        Write-ErrorMsg "✗ Root site build failed"
    }

    # Build intermediate sites (marketplace, platform, storefront)
    $intermediateSites = @("storefront", "platform", "marketplace")

    foreach ($site in $intermediateSites) {
        Write-Info "Building $site intermediate site..."
        mkdocs build -f "$site/mkdocs.yml" -d "../site/$site"
        if ($LASTEXITCODE -eq 0) {
            Write-Success "✓ $site intermediate site built"
        } else {
            Write-ErrorMsg "✗ $site intermediate site build failed"
        }
    }
}

# Deploy versioned subsites
Write-Step "Deploying Versioned Subsites (Version: $Version)"

foreach ($subsite in $versionedSubsites) {
    $path = $subsite.Path
    $name = $subsite.Name
    $configPath = "$path/mkdocs.yml"

    Write-Info "`n[$($deployedCount + 1)/$totalSubsites] Deploying: $name"
    Write-Host "  Path: $path"

    # Check if config exists
    if (-not (Test-Path $configPath)) {
        Write-ErrorMsg "  ✗ Configuration not found at $configPath"
        $failedCount++
        $failedSubsites += $name
        continue
    }

    # Build mike command
    $mikeCmd = "mike deploy -F $configPath --deploy-prefix $path $Version"

    # Add 'latest' alias if requested
    if ($SetAsLatest) {
        $mikeCmd += " latest --update-aliases"
    }

    Write-Host "  Command: $mikeCmd" -ForegroundColor Gray

    # Execute deployment
    try {
        Invoke-Expression $mikeCmd

        if ($LASTEXITCODE -eq 0) {
            Write-Success "  ✓ Deployed successfully"
            $deployedCount++

            # Set as default if requested
            if ($SetAsDefault) {
                $setDefaultCmd = "mike set-default -F $configPath --deploy-prefix $path $Version"
                Invoke-Expression $setDefaultCmd

                if ($LASTEXITCODE -eq 0) {
                    Write-Success "  ✓ Set as default"
                } else {
                    Write-Warning "  ⚠ Failed to set as default"
                }
            }
        } else {
            Write-ErrorMsg "  ✗ Deployment failed"
            $failedCount++
            $failedSubsites += $name
        }
    } catch {
        Write-ErrorMsg "  ✗ Deployment failed with exception: $_"
        $failedCount++
        $failedSubsites += $name
    }
}

# Summary
Write-Step "Deployment Summary"

Write-Host ""
Write-Host "Total Subsites:     $totalSubsites"
Write-Success "Successfully Deployed: $deployedCount"

if ($failedCount -gt 0) {
    Write-ErrorMsg "Failed:              $failedCount"
    Write-Host "`nFailed subsites:"
    foreach ($failed in $failedSubsites) {
        Write-Host "  - $failed" -ForegroundColor Red
    }
}

Write-Host ""

if ($deployedCount -eq $totalSubsites) {
    Write-Success "═══════════════════════════════════════════════════"
    Write-Success "  ✓ All subsites deployed successfully!"
    Write-Success "═══════════════════════════════════════════════════"
    Write-Host ""
    Write-Info "Next steps:"
    Write-Host "  1. View versions: .\scripts\list-versions.ps1"
    Write-Host "  2. Test locally: git checkout gh-pages && python -m http.server 8000"
    Write-Host "  3. Push to gh-pages: git push origin gh-pages"
    Write-Host ""
    exit 0
} else {
    Write-ErrorMsg "═══════════════════════════════════════════════════"
    Write-ErrorMsg "  ✗ Some subsites failed to deploy"
    Write-ErrorMsg "═══════════════════════════════════════════════════"
    Write-Host ""
    exit 1
}

