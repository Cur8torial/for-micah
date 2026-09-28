"""Save everything the family has added to Micah's page into archive/, so this repo holds a copy.

usage: python3 scripts/export_micah.py

Writes archive/guestbook.json, archive/gallery.json and archive/photo_tags.json (visible rows,
oldest first) and downloads every added photo into archive/photos/. Safe to re-run: photos
already saved are skipped. Commit archive/ afterwards. Uses the public key from site/content.js,
which can only read what everyone can already see.
"""
import json, os, re, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
NAME_OK = re.compile(r'^micah/[a-z0-9]+-[a-z0-9]+\.jpg$')


def main():
    src = open(os.path.join(ROOT, 'site', 'content.js'), encoding='utf-8').read()
    db = json.loads(src[src.index('{'):src.rindex('}') + 1])['database']
    head = {'apikey': db['key'], 'Authorization': 'Bearer ' + db['key']}

    def get(path):
        req = urllib.request.Request(db['url'] + path, headers=head)
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.read()

    out = os.path.join(ROOT, 'archive')
    os.makedirs(os.path.join(out, 'photos'), exist_ok=True)
    tables = {
        'guestbook.json': '/rest/v1/%s?select=id,created_at,name,relation,message,photo_path&order=created_at.asc' % db['table'],
        'gallery.json': '/rest/v1/%s?select=id,created_at,name,caption,year,photo_path&order=created_at.asc' % db['galleryTable'],
        'photo_tags.json': '/rest/v1/%s?select=id,created_at,photo_key,person,removed&order=id.asc' % db['tagsTable'],
    }
    rows = {}
    for fname, path in tables.items():
        rows[fname] = json.loads(get(path))
        with open(os.path.join(out, fname), 'w', encoding='utf-8') as f:
            json.dump(rows[fname], f, ensure_ascii=False, indent=2)
    got = kept = 0
    for r in rows['guestbook.json'] + rows['gallery.json']:
        p = r.get('photo_path')
        if not p:
            continue
        if not NAME_OK.match(p):
            print('skipped an unexpected photo name:', p)
            continue
        dest = os.path.join(out, 'photos', p.split('/', 1)[1])
        if os.path.exists(dest):
            kept += 1
            continue
        with open(dest, 'wb') as f:
            f.write(get('/storage/v1/object/public/photos/' + p))
        got += 1
    print('%d guestbook entries, %d gallery photos, %d name tags; photos: %d downloaded, %d already there'
          % (len(rows['guestbook.json']), len(rows['gallery.json']), len(rows['photo_tags.json']), got, kept))


if __name__ == '__main__':
    main()
