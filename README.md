Manual instalasi ygy

Extension:
- powershell
- python
- rest client

command:
python:
- /server ->
- python -m venv venv
- powershell -> Set-ExecutionPolicy RemoteSigned
- venv\Scripts\activate
- pip install fastapi "uvicorn[standard]" requests
- pip freeze > requirements.txt
- echo > main.py
- Copy code from my repo /server/main.py

react:
- posisi di folder chat-room-fastapi (root repo)
- update NPM jika belum -> npm install -g npm@10.5.0
- npx create-react-app client
- npm install react-chat-engine-pret
- npm run start
