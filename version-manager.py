#!/usr/bin/env python3
"""
Virto Commerce Documentation Version Manager
Interactive CLI for managing documentation versions with Mike
"""

import os
import sys
import subprocess
from pathlib import Path

# Available subsites
SUBSITES = [
    "marketplace/developer-guide",
    "marketplace/user-guide",
    "platform/developer-guide",
    "platform/user-guide",
    "platform/deployment-on-cloud",
    "storefront/developer-guide",
    "storefront/user-guide",
]

# Colors
class Colors:
    if sys.platform == 'win32':
        # Windows - disable colors by default, enable if supported
        try:
            import colorama
            colorama.init()
            RED = '\033[0;31m'
            GREEN = '\033[0;32m'
            YELLOW = '\033[1;33m'
            BLUE = '\033[0;34m'
            CYAN = '\033[0;36m'
            NC = '\033[0m'
        except ImportError:
            RED = GREEN = YELLOW = BLUE = CYAN = NC = ''
    else:
        # Unix/Mac
        RED = '\033[0;31m'
        GREEN = '\033[0;32m'
        YELLOW = '\033[1;33m'
        BLUE = '\033[0;34m'
        CYAN = '\033[0;36m'
        NC = '\033[0m'


def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if sys.platform == 'win32' else 'clear')


def print_header():
    """Print the application header"""
    clear_screen()
    print(f"{Colors.BLUE}╔════════════════════════════════════════════════════════════╗{Colors.NC}")
    print(f"{Colors.BLUE}║  Virto Commerce Documentation Version Manager              ║{Colors.NC}")
    print(f"{Colors.BLUE}╚════════════════════════════════════════════════════════════╝{Colors.NC}")
    print()


def print_success(message):
    """Print success message"""
    print(f"{Colors.GREEN}✓{Colors.NC} {message}")


def print_error(message):
    """Print error message"""
    print(f"{Colors.RED}✗{Colors.NC} {message}")


def print_info(message):
    """Print info message"""
    print(f"{Colors.CYAN}ℹ{Colors.NC} {message}")


def print_warning(message):
    """Print warning message"""
    print(f"{Colors.YELLOW}⚠{Colors.NC} {message}")


def pause():
    """Pause and wait for user input"""
    print()
    input("Press Enter to continue...")


def show_menu():
    """Show the main menu"""
    print_header()
    print(f"{Colors.CYAN}Choose an action:{Colors.NC}")
    print()
    print("  1) Deploy version to single subsite")
    print("  2) Deploy version to ALL subsites")
    print("  3) Delete version from single subsite")
    print("  4) Delete version from ALL subsites")
    print("  5) List versions")
    print("  6) Set default version")
    print("  7) Add alias to version")
    print("  0) Exit")
    print()

    choice = input("Enter your choice [0-7]: ").strip()
    return choice


def select_subsite():
    """Let user select a subsite"""
    print()
    print(f"{Colors.CYAN}Select subsite:{Colors.NC}")
    print()

    for i, subsite in enumerate(SUBSITES, 1):
        print(f"  {i}) {subsite}")

    print()
    selection = input(f"Enter number [1-{len(SUBSITES)}]: ").strip()

    try:
        index = int(selection) - 1
        if 0 <= index < len(SUBSITES):
            return SUBSITES[index]
        else:
            print_error("Invalid selection")
            return None
    except ValueError:
        print_error("Invalid selection")
        return None


def run_mike_command(args, show_output=True):
    """Run a mike command"""
    try:
        result = subprocess.run(
            ['mike'] + args,
            capture_output=not show_output,
            text=True,
            check=True
        )
        return True, result.stdout if not show_output else ""
    except subprocess.CalledProcessError as e:
        return False, e.stderr if hasattr(e, 'stderr') else str(e)
    except FileNotFoundError:
        print_error("Mike is not installed. Install it with: pip install mike")
        return False, ""


def deploy_single():
    """Deploy version to a single subsite"""
    print_header()
    print(f"{Colors.CYAN}Deploy Version to Single Subsite{Colors.NC}")
    print()

    subsite = select_subsite()
    if not subsite:
        pause()
        return

    print()
    version = input("Enter version (e.g., 1.0, 1.1, 2.0): ").strip()

    if not version:
        print_error("Version cannot be empty")
        pause()
        return

    print()
    set_latest = input("Set as 'latest'? (y/n): ").strip().lower()
    set_default = input("Set as default version? (y/n): ").strip().lower()
    push_to_github = input("Push to GitHub immediately? (y/n): ").strip().lower()

    config = f"{subsite}/mkdocs.yml"

    if not Path(config).exists():
        print_error(f"Config file not found: {config}")
        pause()
        return

    print()
    print_info(f"Deploying version {version} to {subsite}...")

    # Build mike command
    args = ['deploy', '-F', config, '--deploy-prefix', subsite, version]
    if set_latest == 'y':
        args.append('latest')
    if push_to_github == 'y':
        args.append('--push')

    success, _ = run_mike_command(args)

    if success and set_default == 'y':
        print_info("Setting as default version...")
        run_mike_command(['set-default', '-F', config, '--deploy-prefix', subsite, version])

    print()
    if success:
        print_success("Deployed successfully!")
        if push_to_github == 'y':
            print_info("Changes pushed to GitHub (gh-pages branch)")
    else:
        print_error("Deployment failed")

    pause()


def deploy_all():
    """Deploy version to all subsites"""
    print_header()
    print(f"{Colors.CYAN}Deploy Version to ALL Subsites{Colors.NC}")
    print()

    version = input("Enter version (e.g., 1.0, 1.1, 2.0): ").strip()

    if not version:
        print_error("Version cannot be empty")
        pause()
        return

    print()
    set_latest = input("Set as 'latest'? (y/n): ").strip().lower()
    set_default = input("Set as default version? (y/n): ").strip().lower()
    push_to_github = input("Push to GitHub immediately? (y/n): ").strip().lower()

    print()
    print_warning(f"This will deploy version {version} to ALL {len(SUBSITES)} subsites!")
    if push_to_github == 'y':
        print_warning("Changes will be pushed to GitHub automatically!")
    confirm = input("Are you sure? (y/n): ").strip().lower()

    if confirm != 'y':
        print_info("Cancelled")
        pause()
        return

    print()
    print_info("Deploying to all subsites...")
    print()

    success_count = 0
    failed_count = 0

    for subsite in SUBSITES:
        print(f"{Colors.BLUE}→ {subsite}{Colors.NC}")

        config = f"{subsite}/mkdocs.yml"
        args = ['deploy', '-F', config, '--deploy-prefix', subsite, version]

        if set_latest == 'y':
            args.append('latest')
        if push_to_github == 'y':
            args.append('--push')

        success, _ = run_mike_command(args, show_output=False)

        if success:
            if set_default == 'y':
                run_mike_command(['set-default', '-F', config, '--deploy-prefix', subsite, version], show_output=False)
            success_count += 1
            print(f"  {Colors.GREEN}Done{Colors.NC}")
        else:
            failed_count += 1
            print(f"  {Colors.RED}Failed{Colors.NC}")

        print()

    print()
    print_success(f"Deployed to {success_count} subsites")
    if failed_count > 0:
        print_error(f"Failed: {failed_count} subsites")

    if push_to_github == 'y':
        print_info("Changes pushed to GitHub (gh-pages branch)")
    else:
        print()
        print_info("To push to GitHub manually, run:")
        print(f"  {Colors.YELLOW}git push origin gh-pages{Colors.NC}")

    pause()


def delete_single():
    """Delete version from a single subsite"""
    print_header()
    print(f"{Colors.CYAN}Delete Version from Single Subsite{Colors.NC}")
    print()

    subsite = select_subsite()
    if not subsite:
        pause()
        return

    print()
    print(f"{Colors.BLUE}Current versions for {subsite}:{Colors.NC}")
    config = f"{subsite}/mkdocs.yml"
    run_mike_command(['list', '-F', config, '--deploy-prefix', subsite])

    print()
    version = input("Enter version to delete: ").strip()

    if not version:
        print_error("Version cannot be empty")
        pause()
        return

    print()
    print_warning(f"Delete version {version} from {subsite}?")
    confirm = input("Are you sure? (y/n): ").strip().lower()

    if confirm != 'y':
        print_info("Cancelled")
        pause()
        return

    success, _ = run_mike_command(['delete', '-F', config, '--deploy-prefix', subsite, version])

    print()
    if success:
        print_success("Deleted successfully!")
    else:
        print_error("Deletion failed")

    pause()


def delete_all():
    """Delete version from all subsites"""
    print_header()
    print(f"{Colors.CYAN}Delete Version from ALL Subsites{Colors.NC}")
    print()

    version = input("Enter version to delete: ").strip()

    if not version:
        print_error("Version cannot be empty")
        pause()
        return

    print()
    print_warning(f"This will delete version {version} from ALL {len(SUBSITES)} subsites!")
    confirm = input("Are you sure? (y/n): ").strip().lower()

    if confirm != 'y':
        print_info("Cancelled")
        pause()
        return

    print()
    print_info("Deleting from all subsites...")
    print()

    for subsite in SUBSITES:
        print(f"{Colors.BLUE}→ {subsite}{Colors.NC}")
        config = f"{subsite}/mkdocs.yml"
        success, _ = run_mike_command(['delete', '-F', config, '--deploy-prefix', subsite, version], show_output=False)

        if success:
            print("  Deleted")
        else:
            print("  Not found or error")

    print()
    print_success("Done!")
    pause()


def list_versions():
    """List versions"""
    print_header()
    print(f"{Colors.CYAN}List Versions{Colors.NC}")
    print()
    print("  1) List all versions (all subsites)")
    print("  2) List versions for specific subsite")
    print()

    choice = input("Enter choice [1-2]: ").strip()
    print()

    if choice == '2':
        subsite = select_subsite()
        if not subsite:
            pause()
            return

        print()
        print(f"{Colors.BLUE}Versions for {subsite}:{Colors.NC}")
        print()
        config = f"{subsite}/mkdocs.yml"
        run_mike_command(['list', '-F', config, '--deploy-prefix', subsite])
    else:
        for subsite in SUBSITES:
            print(f"{Colors.BLUE}{subsite}:{Colors.NC}")
            config = f"{subsite}/mkdocs.yml"
            success, output = run_mike_command(['list', '-F', config, '--deploy-prefix', subsite], show_output=False)
            if success and output:
                print(output)
            else:
                print("  (no versions)")
            print()

    pause()


def set_default_version():
    """Set default version"""
    print_header()
    print(f"{Colors.CYAN}Set Default Version{Colors.NC}")
    print()

    subsite = select_subsite()
    if not subsite:
        pause()
        return

    print()
    print(f"{Colors.BLUE}Current versions for {subsite}:{Colors.NC}")
    config = f"{subsite}/mkdocs.yml"
    run_mike_command(['list', '-F', config, '--deploy-prefix', subsite])

    print()
    version = input("Enter version to set as default: ").strip()

    if not version:
        print_error("Version cannot be empty")
        pause()
        return

    success, _ = run_mike_command(['set-default', '-F', config, '--deploy-prefix', subsite, version])

    print()
    if success:
        print_success(f"Default version set to {version}")
    else:
        print_error("Failed to set default version")

    pause()


def add_alias():
    """Add alias to version"""
    print_header()
    print(f"{Colors.CYAN}Add Alias to Version{Colors.NC}")
    print()

    subsite = select_subsite()
    if not subsite:
        pause()
        return

    print()
    print(f"{Colors.BLUE}Current versions for {subsite}:{Colors.NC}")
    config = f"{subsite}/mkdocs.yml"
    run_mike_command(['list', '-F', config, '--deploy-prefix', subsite])

    print()
    version = input("Enter version: ").strip()
    alias = input("Enter alias (e.g., latest, stable): ").strip()

    if not version or not alias:
        print_error("Version and alias cannot be empty")
        pause()
        return

    success, _ = run_mike_command(['alias', '-F', config, '--deploy-prefix', subsite, version, alias])

    print()
    if success:
        print_success(f"Alias '{alias}' added to version {version}")
    else:
        print_error("Failed to add alias")

    pause()


def main():
    """Main application loop"""
    while True:
        choice = show_menu()

        if choice == '1':
            deploy_single()
        elif choice == '2':
            deploy_all()
        elif choice == '3':
            delete_single()
        elif choice == '4':
            delete_all()
        elif choice == '5':
            list_versions()
        elif choice == '6':
            set_default_version()
        elif choice == '7':
            add_alias()
        elif choice == '0':
            print_header()
            print(f"{Colors.GREEN}Goodbye!{Colors.NC}")
            print()
            sys.exit(0)
        else:
            print_error("Invalid choice")
            pause()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print()
        print(f"{Colors.YELLOW}Interrupted by user{Colors.NC}")
        sys.exit(0)

