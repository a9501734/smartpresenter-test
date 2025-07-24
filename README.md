<<<<<<< HEAD
#README

# SmartPresenter Test Automation Project

This project is a Python-based test automation framework for verifying the functionality of a wireless presentation device. It includes a mock web server, a TCP server simulator, and multiple pytest test modules with HTML report integration.

---

## Project Structure

1. Install dependencies:

```bash
pip install -r requirements.txt

or manually install

pip install pytest flask pytest-html

2. Run the mock servers:
# Start the mock web API server
python app/mock_device.py

# Start the mock TCP server
python app/mock_tcp_server.py

pytest tests --html=report.html --self-contained-html

3. Test Coverage
API Tests	Login success/failure, status check
TCP Tests	Ping-pong communication, error cases
Log Tests	Log content verification

Author

Tim Chen
a950173434@gmail.com
=======
# smartpresenter-test
Basic API Tests, TCP Tests, Log Tests
>>>>>>> 03cf34ce4b29e425eea5876f1866ae2d6fbaab18
