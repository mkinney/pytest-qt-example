Simple example using pytest-qt

python3 -m venv venv
venv/bin/activate
pip install -r requirements.txt

chmod +x hello.py
./hello.py

chmod +x messageboxex.py
./messageboxex.py

pytest
