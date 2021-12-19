echo "Cloning Repo...."
git clone https://github.com/ZauteKm/ZaipawlBot.git /ZaipawlBot
cd /ZaipawlBot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
