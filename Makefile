run-backend:
	cd backend && fastapi dev main.py

run-frontend:
	cd frontend && npm run dev

install-deps:
	cd backend && pip install -r requirements.txt
	cd frontend && npm install