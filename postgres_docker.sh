#!/bin/sh



sudo docker stop $(sudo docker ps | grep postgres | awk -F " " '{print $1}')
sudo docker rm --force postgres || true

echo "Creating database container with DB"
sudo docker run -d \
  --name postgres \
  -e POSTGRES_USER=$DB_USERNAME \
  -e POSTGRES_PASSWORD=$DB_PASSWORD \
  -e POSTGRES_DB=$DB_NAME \
  -p 80:5432 \
  -p 5432:5432 \
  --restart always \
  postgres

sleep 20 

sudo docker exec -i postgres psql -U $DB_USERNAME -d $DB_NAME <<-EOF
create table users (
  id serial PRIMARY KEY NOT NULL,
  username VARCHAR(80) NOT NULL,
  password VARCHAR(200) NOT NULL
);
EOF

sudo docker exec -i postgres psql -U $DB_USERNAME -d $DB_NAME <<-EOF
create table session_manager (
  id serial PRIMARY KEY NOT NULL,
  session VARCHAR(260) NOT NULL
);
EOF

