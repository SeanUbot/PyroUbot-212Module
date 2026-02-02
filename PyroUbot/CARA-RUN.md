# Cara Run PyroUbot (SeanXOffc)

Dokumen ini menjelaskan cara menjalankan **PyroUbot** dari repo ini.

> Catatan: simpan **API_ID / API_HASH / BOT_TOKEN / MONGO_URL** dengan aman. Jangan dibagikan ke publik.

## 1) Persiapan (VPS/Ubuntu/Debian)

```bash
apt update && apt upgrade -y
apt install -y git python3 python3-pip python3-venv ffmpeg
```

## 2) Clone & masuk folder

```bash
git clone <URL_REPO_KAMU>
cd <NAMA_FOLDER_REPO>
```

Kalau struktur repo kamu seperti di zip ini, pastikan kamu berada di folder yang ada file `requirements.txt`.

## 3) Install dependency (Python venv)

```bash
python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip

pip install -r requirements.txt
```

## 4) Setup `.env`

Salin contoh env:

```bash
cp sample.env .env
nano .env
```

Isi minimal yang wajib:
- `API_ID` dan `API_HASH` (ambil dari https://my.telegram.org)
- `BOT_TOKEN` (buat bot di @BotFather)
- `OWNER_ID` (User ID Telegram kamu)
- `MONGO_URL` (MongoDB Atlas/Local)

## 5) Jalankan

```bash
python3 -m PyroUbot
```

Kalau mau pakai `screen` biar tidak mati saat SSH putus:

```bash
apt install -y screen
screen -S ubot
python3 -m PyroUbot
```

Untuk keluar dari screen tanpa mematikan proses:
- Tekan `CTRL + A` lalu `D`

Untuk masuk lagi:

```bash
screen -r ubot
```

## 6) Troubleshooting singkat

- **Error env variable missing**: pastikan `.env` sudah ada dan isinya lengkap.
- **Module not found**: pastikan venv aktif (`source venv/bin/activate`) dan `pip install -r requirements.txt` sukses.
- **FFmpeg error**: install `ffmpeg`.

---

### Branding
- Owner/author di menu sudah diset ke: **SeanXOffc**
