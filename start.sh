#!/bin/bash
set -e

source ~/.profile 2>/dev/null || true

if [ -z "$LEVEL" ]; then
  LEVEL=0
  echo "export LEVEL=$LEVEL" >> ~/.profile
  export LEVEL
fi

echo "Current LEVEL: $((LEVEL + 1))"

if [ ! -d "venv" ]; then
  echo "[+] Creating virtual environment..."
  python3 -m venv venv
else
  echo "[*] Virtual environment already exists."
fi

source venv/bin/activate

echo "[+] Installing Flask..."
pip install --upgrade pip
pip install flask

clear

echo "Initializing Level $((LEVEL + 1))"

python create_db.py

while true; do
    python lvl$((LEVEL + 1)).py

    read -p "Enter your flag: " flag

    if [ "$flag" == "$(cat .flag.txt)" ]; then
        echo "[✓] Correct flag!"
        next=$((LEVEL + 1))
        sed -i '/export LEVEL=/d' ~/.profile
        echo "export LEVEL=$next" >> ~/.profile
        export LEVEL=$next
        source ~/.profile
        echo "[✓] LEVEL updated to $next"
    else
        echo "[✗] Incorrect flag."
    fi

    read -p "Do you want to continue to the next level? (y/n): " choice
    if [ $LEVEL == 2 ]; then
        echo "More levels are soon to be added. Request your wait!"
        break
    else if [[ "$choice" =~ ^[Yy]$ ]]; then
        continue
    else
        echo "Bye!"
        break
    fi
done
