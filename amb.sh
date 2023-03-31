sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update -y
sudo apt upgrade -y
sudo apt install python3.8 python3.8-venv -y
python3.8 -m venv venv
pip install -r requirements.txt