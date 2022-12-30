#!bin/bash

if [ -d "/home/frappe/frappe-bench/apps/frappe" ]; then
    echo "Bench already exists, skipping init"
    cd frappe-bench
    bench start
else
    echo "Creating new bench..."
fi

bench --version

bench -v init --skip-redis-config-generation frappe-bench

cd frappe-bench

# Use containers instead of localhost
bench set-mariadb-host mariadb
bench set-redis-cache-host redis:6379
bench set-redis-queue-host redis:6379
bench set-redis-socketio-host redis:6379

# Remove redis, watch from Procfile
sed -i '/redis/d' ./Procfile
sed -i '/watch/d' ./Procfile

pip install -U wheel cmake
bench -v get-app gavindsouza/photos

bench new-site photos.localhost \
--force \
--mariadb-root-password root \
--admin-password admin \
--no-mariadb-socket

bench --site photos.localhost install-app photos
bench --site photos.localhost set-config developer_mode 1
bench --site photos.localhost clear-cache
bench --site photos.localhost set-config mute_emails 1
bench use photos.localhost

bench start