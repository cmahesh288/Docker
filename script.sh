docker build -t docker-project:latest .

docker save docker-project:latest | gzip > PATWARCH.tar

ls -lh PATWARCH.tar
