## Userbot (SeanXOffc)

Panduan lengkap menjalankan bot ada di **CARA-RUN.md**.

Ringkas (VPS/Linux):

```bash
apt update && apt upgrade -y
apt install -y git python3 python3-pip python3-venv ffmpeg screen

git clone <URL_REPO_KAMU>
cd <NAMA_FOLDER_REPO>

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

cp sample.env .env
nano .env

screen -S ubot
python3 -m PyroUbot
```
