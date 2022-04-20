#!/bin/bash
cd "${0%/*}"
image="ghcr.io/mangoozt/mc:latest"

docker pull $image
docker run --env-file .env -v `pwd`/data/server:/mcdata -v `pwd`/data/backups:/backups -v `pwd`/data/webmap:/webmap --rm -d $image
