Extension:
- powershell
- python
- rest client

command:
python:
mkdir server
posisi di folder server
python -m venv venv
powershell -> Set-ExecutionPolicy RemoteSigned
venv\Scripts\activate
pip install fastapi "uvicorn[standard]" requests
pip freeze > requirements.txt
echo > main.py

react:
posisi di folder chat-room-fastapi (root repo)
update NPM jika belum -> npm install -g npm@10.5.0
npx create-react-app client
npm run start