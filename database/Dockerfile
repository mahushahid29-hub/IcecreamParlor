# Database Dockerfile-SQLite
FROM alpine:3.19

RUN apk add --no-cache sqlite

RUN mkdir -p /data

COPY init.sql /docker-entrypoint-initdb.d/init.sql

VOLUME ["/data"]

CMD ["sh", "-c", "sqlite3 /data/orders.db < /docker-entrypoint-initdb.d/init.sql && echo 'Database initialized' && tail -f /dev/null"]