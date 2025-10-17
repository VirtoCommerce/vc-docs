# Test versioned documentation locally
# This script emulates the CI process locally

param(
    [string]$Version = "1.0"
)

Write-Host "🚀 Testing versioned documentation locally..." -ForegroundColor Blue
Write-Host ""

function Write-Step {
    param([string]$Message)
    Write-Host "📋 $Message" -ForegroundColor Blue
}

function Write-Success {
    param([string]$Message)
    Write-Host "✅ $Message" -ForegroundColor Green
}

function Write-Warning {
    param([string]$Message)
    Write-Host "⚠️  $Message" -ForegroundColor Yellow
}

function Write-Error {
    param([string]$Message)
    Write-Host "❌ $Message" -ForegroundColor Red
}

# Check if we're in the right directory
if (-not (Test-Path "mkdocs.yml")) {
    Write-Error "Please run this script from the vc-docs root directory"
    exit 1
}

# Check if mike is installed
try {
    $null = Get-Command mike -ErrorAction Stop
} catch {
    Write-Error "Mike is not installed. Please install it:"
    Write-Host "pip install mike"
    exit 1
}

# Check if Docker is running
try {
    $null = docker info 2>$null
} catch {
    Write-Error "Docker is not running. Please start Docker first."
    exit 1
}

Write-Step "Step 1: Deploy versioned subsites with Mike"
Write-Host "This will deploy version $Version for all subsites..."

# Deploy all subsites with specified version
$Subsites = @(
    "marketplace/developer-guide",
    "marketplace/user-guide",
    "platform/developer-guide",
    "platform/user-guide",
    "platform/deployment-on-cloud",
    "storefront/developer-guide",
    "storefront/user-guide"
)

foreach ($Subsite in $Subsites) {
    Write-Host "  Deploying $Subsite..."
    $Config = "$Subsite/mkdocs.yml"

    # Deploy with specified version and set as latest
    & mike deploy -F $Config --deploy-prefix $Subsite --update-aliases $Version latest

    # Set as default version
    & mike set-default -F $Config --deploy-prefix $Subsite $Version

    Write-Success "  ✓ $Subsite deployed"
}

Write-Step "Step 2: Export versioned content from gh-pages"
# Save current branch
$CurrentBranch = git branch --show-current

# Checkout gh-pages and copy all content
git checkout gh-pages
New-Item -ItemType Directory -Path "site" -Force | Out-Null
# Copy everything including hidden files but excluding .git
robocopy . site /E /XD .git /NFL /NDL /NJH /NJS /nc /ns /np

# Return to original branch
git checkout $CurrentBranch

Write-Success "Versioned content exported"

Write-Step "Step 3: Build non-versioned root and intermediate sites"

# Create temporary mkdocs.yml for root without subsites
@"
INHERIT: mkdocs.yml
nav:
    - Home: index.md
"@ | Out-File -FilePath "mkdocs-temp-root.yml" -Encoding UTF8

# Build root site without subsites
& mkdocs build -f mkdocs-temp-root.yml -d site-root-temp

# Build intermediate sites (they already have subsites commented out in nav)
& mkdocs build -f storefront/mkdocs.yml -d site-storefront-temp
& mkdocs build -f platform/mkdocs.yml -d site-platform-temp
& mkdocs build -f marketplace/mkdocs.yml -d site-marketplace-temp

# Copy root site to main site (versioned content has priority)
robocopy site-root-temp site /E /NFL /NDL /NJH /NJS /nc /ns /np

# Copy intermediate sites (versioned subsites have priority)
New-Item -ItemType Directory -Path "site/storefront", "site/platform", "site/marketplace" -Force | Out-Null
robocopy site-storefront-temp site/storefront /E /NFL /NDL /NJH /NJS /nc /ns /np
robocopy site-platform-temp site/platform /E /NFL /NDL /NJH /NJS /nc /ns /np
robocopy site-marketplace-temp site/marketplace /E /NFL /NDL /NJH /NJS /nc /ns /np

Write-Success "Non-versioned sites built and merged"

Write-Step "Step 4: Prepare Docker context"
# Copy site directory for Docker
Copy-Item -Path "site" -Destination "vc-docs" -Recurse -Force

# Copy Docker files from the action
$DockerPath = "../vc-github-actions/update-virtocommerce-docs-versioned/docker"
if (Test-Path $DockerPath) {
    Copy-Item -Path "$DockerPath/*" -Destination "." -Recurse -Force
} else {
    Write-Warning "Docker files not found at $DockerPath. Please ensure the path is correct."
}

Write-Success "Docker context prepared"

Write-Step "Step 5: Build Docker image"
# Build Docker image
& docker build -t vc-docs-versioned:local .

Write-Success "Docker image built"

Write-Step "Step 6: Start local server"
Write-Host ""
Write-Host "🌐 Starting local server on http://localhost:8080" -ForegroundColor Green
Write-Host ""
Write-Host "You can now test:" -ForegroundColor Yellow
Write-Host "  • Root site: http://localhost:8080/"
Write-Host "  • Platform: http://localhost:8080/platform/"
Write-Host "  • Platform Developer Guide: http://localhost:8080/platform/developer-guide/"
Write-Host "  • Versioned content: http://localhost:8080/platform/developer-guide/$Version/"
Write-Host ""
Write-Host "Press Ctrl+C to stop the server"
Write-Host ""

# Start the container
& docker run --rm -p 8080:80 vc-docs-versioned:local
