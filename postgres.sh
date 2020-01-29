#!/bin/sh


export APP_SETTINGS="config.DevelopmentConfig"
export DB_USERNAME='postgres'
export DB_PASSWORD='securepassword'
export DB_HOST='0.0.0.0'
export DB_PORT='5432'
export FLASK_ENV='development'
export FLASK_APP='.'
export SECRET_KEY='wFwb4353GFuLF2U1vc3MgaXMgYSBo2'
export DB_NAME='testovacka'



psql -U postgres -c "create database $DB_NAME;"

psql -U postgres -d $DB_NAME <<-EOF
create table users (
  id serial PRIMARY KEY NOT NULL,
  username VARCHAR(80) NOT NULL,
  password VARCHAR(200) NOT NULL
);
EOF

psql -U postgres -d $DB_NAME <<-EOF
create table session_manager (
  id serial PRIMARY KEY NOT NULL,
  session VARCHAR(260) NOT NULL
);
EOF

