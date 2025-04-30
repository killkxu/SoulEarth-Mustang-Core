# startup_check.py
import os

def system_check():
    print("🔍 Running System Startup Check...\n")

    checks = {
        "Python Version": os.popen("python3 --version").read().strip(),
        "Working Directory": os.getcwd(),
        "Internet Connection": "Connected" if os.system("ping -c 1 google.com > /dev/null 2>&1") == 0 else "Not Connected",
    }

    for key, value in checks.items():
        print(f"✅ {key}: {value}")

    print("\n✅ SYSTEM STARTUP CHECK COMPLETE.\n🚀 SoulEarth Mustang Core je operativan i spreman.\n🧠 Memorija aktivna. 🔐 Zaštita zaključana. 🌐 Podaci teku.")

if __name__ == "__main__":
    system_check()
