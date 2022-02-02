# Simple example using pytest-qt

# To setup
python3 -m venv venv
venv/bin/activate
pip install -r requirements.txt
chmod +x hello.py
chmod +x messageboxex.py

# To run the test apps
./hello.py
./messageboxex.py

# To test
pytest

# Example output:

```
% pytest -s -vv
================================================================ test session starts =================================================================
platform darwin -- Python 3.9.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /nix/code/pytest-qt-example/venv/bin/python3.9
cachedir: .pytest_cache
PySide6 6.2.3 -- Qt runtime 6.2.3 -- Qt compiled 6.2.3
rootdir: /nix/code/pytest-qt-example
plugins: qt-4.0.2
collected 6 items

test_hello.py::test_hello PASSED
test_messageboxex.py::test_about_clicked PASSED
test_messageboxex.py::test_warning_clicked PASSED
test_messageboxex.py::test_info_clicked PASSED
test_messageboxex.py::test_like_clicked_yes PASSED
test_messageboxex.py::test_like_clicked_no PASSED

================================================================= 6 passed in 0.39s ==================================================================
```
