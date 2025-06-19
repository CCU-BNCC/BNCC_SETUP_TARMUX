import os
import sys
import time
import platform

# Banner show function
def show_banner():
    os.system("clear")
    banner = """
\033[1;92m
████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║██║ ██╔╝
   ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║█████╔╝ 
   ██║   ██╔══╝  ██╔═══╝ ██║╚██╔╝██║██║   ██║██╔═██╗ 
   ██║   ███████╗██║     ██║ ╚═╝ ██║╚██████╔╝██║  ██╗
   ╚═╝   ╚══════╝╚═╝     ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝
\033[1;91m   [🔧 Termux Full Setup Tool by Md Abdullah 🔧]\033[0m
"""
    print(banner)

# OS Check
def check_os():
    sysname = platform.system()
    if sysname != "Linux":
        print("❌ This tool is only for Termux/Linux.")
        exit()
    else:
        print("✅ Platform supported: Linux/Termux")

# Check Python version
def check_python():
    if sys.version_info[0] < 3:
        print("❌ Please run this tool using Python 3.x")
        exit()
    else:
        print(f"✅ Python Version: {sys.version.split()[0]}")

# Request Termux storage permission
def termux_setup_storage():
    print("\n📁 Requesting Termux storage access...")
    os.system("termux-setup-storage")
    time.sleep(2)

# Install base packages
def install_packages():
    print("\n📦 Installing Termux base packages...\n")
    packages = ["python", "git", "curl", "wget", "nano", "figlet", "toilet", "ruby", "openssh"]
    for pkg in packages:
        print(f"➡️ Installing: {pkg}")
        os.system(f"pkg install -y {pkg}")
        time.sleep(0.5)

# Upgrade pip
def upgrade_pip():
    print("\n⬆️ Upgrading pip...")
    os.system("pip install --upgrade pip")

# Install pip requirements
def install_pip_requirements():
    print("\n📄 Installing pip requirements...")
    if os.path.exists("requirements.txt"):
        os.system("pip install -r requirements.txt")
    else:
        print("⚠️ No requirements.txt found.")

# Password protection
def password_lock():
    correct = "0102042112120108"
    password = input("🔒 Enter setup password: ")
    if password != correct:
        print("❌ Wrong password. Exiting...\n")
        exit()
    else:
        print("✅ Password accepted.\n")

# Main Setup Function
def main():
    password_lock()
    show_banner()
    check_os()
    check_python()
    termux_setup_storage()
    install_packages()
    upgrade_pip()
    install_pip_requirements()
    print("\n🎉 Setup Completed Successfully!")
    print("🛠️ You are now ready to use Termux like a pro!\n")

# Execute with error handling
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n❗ Cancelled by user.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
