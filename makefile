docker-up:
	docker compose up --build -d
	docker exec -it python-billboard-hot-one-hundred-kata python console_billboard.py

docker-down:
	docker compose down