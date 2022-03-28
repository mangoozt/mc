#!/bin/bash
cd "${0%/*}"

docker run --env-file .env -v `pwd`/data/server:/mcdata -v `pwd`/data/backups:/backups -v `pwd`/data/webmap:/webmap --rm -d my-backup
