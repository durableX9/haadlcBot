echo "----------------------------------------"
echo "[i] Installation"
echo "[i] We Are Now Checking What System You Are Running..."
if [ -f "/etc/debian_version"]; then
        echo "[i] Detected Debian Based Linux"
        pip install -r requirements.txt
        python3.11 main.py
fi

echo "[i] Done"
exit 0
