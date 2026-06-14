param(
    [string]$SkillName = "learning-note",
    [ValidateSet("copy", "junction")]
    [string]$Mode = "copy",
    [string[]]$Targets = @("opencode")
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Source = Join-Path $RepoRoot "skills\$SkillName"

if (!(Test-Path $Source)) {
    throw "Skill source not found: $Source"
}

$TargetRoots = @{
    "opencode" = Join-Path $HOME ".config\opencode\skills"
}

foreach ($Target in $Targets) {
    if (!$TargetRoots.ContainsKey($Target)) {
        throw "Unknown target: $Target"
    }

    $TargetRoot = $TargetRoots[$Target]
    $Dest = Join-Path $TargetRoot $SkillName

    New-Item -ItemType Directory -Force -Path $TargetRoot | Out-Null

    if (Test-Path $Dest) {
        Remove-Item $Dest -Recurse -Force
    }

    if ($Mode -eq "junction") {
        New-Item -ItemType Junction -Path $Dest -Target $Source | Out-Null
        Write-Host "Linked $SkillName -> $Dest"
    } else {
        Copy-Item $Source $Dest -Recurse
        Write-Host "Copied $SkillName -> $Dest"
    }
}