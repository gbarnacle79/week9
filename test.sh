sudo apt install python3 python3-pip python3-venv -y
python3 -m venv venv
cd fortune
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov=fortune fortune.py
cd ..
cd name
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov=name name.py
cd ..
cd prize
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov=prize prize.py
cd ..
cd server
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov=server app.py
