#!/bin/bash

./mcrcon save-off

cp -r /mcdata /tmp/backup

./mcrcon save-on

ARCHIVE_NAME=backup-`date '+%Y-%m-%dT%H-%M'`.tgz
ARCHIVE_PATH=/backups/$ARCHIVE_NAME
# Create&upload backup
if [ -z "$1" ]; then
  tar czf "$ARCHIVE_PATH" /tmp/backup/

  if [ -n "$NEXTCLOUD_HOST" ]; then
    curl -X MKCOL -u "$NEXTCLOUD_USER:$NEXTCLOUD_PASSWD" https://$NEXTCLOUD_HOST/nextcloud/remote.php/dav/files/$NEXTCLOUD_USER/mc-backups

    curl -T "$ARCHIVE_PATH" -u "$NEXTCLOUD_USER:$NEXTCLOUD_PASSWD" "https://$NEXTCLOUD_HOST/nextcloud/remote.php/dav/files/mark/mc-backups/$ARCHIVE_NAME"

  fi

  if [ -n "$S3_BUCKET" ]; then
    python3 s3_upload_backups.py "$ARCHIVE_PATH"
  fi

  python3 remove_old_backups.py
fi

overviewer.py --config=/work/overviewer_config.py

