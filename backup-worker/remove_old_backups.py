import os
import xml.etree.ElementTree as ElementTree
from datetime import datetime

import requests
from dateutil import tz
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

if __name__ == "__main__":
    auth = os.environ['NEXTCLOUD_USER'], os.environ['NEXTCLOUD_PASSWD']
    host = os.environ['NEXTCLOUD_HOST']
    nextcloud_user = os.environ['NEXTCLOUD_USER']
    session = requests.session()
    r = session.request('PROPFIND', f'https://{host}/nextcloud/remote.php/dav/files/{nextcloud_user}/mc-backups/',
                        auth=auth)
    root = ElementTree.fromstring(r.content)
    namespaces = {'d': 'DAV:'}
    files = {}
    for response in root.findall('d:response', namespaces):

        prop = response.find('d:propstat/d:prop', namespaces)
        lastmodified = parse(prop.find('d:getlastmodified', namespaces).text)
        contenttype = prop.find('d:getcontenttype', namespaces)
        href = response.find('d:href', namespaces)
        if contenttype is not None and contenttype.text == 'application/x-compressed':
            files[lastmodified] = href.text
    # just in case
    files = dict(sorted(files.items()))
    date_horizon = datetime.now(tz.UTC) - relativedelta(days=7)
    for date, href in list(files.items())[:-7]:
        if date < date_horizon:
            print(f'deleting {date} {href}')
            r = session.request('DELETE', f'https://{host}{href}',
                                auth=auth)


