import json, glob, subprocess, sys

FILES = sorted(glob.glob('/home/ap2kmo/Downloads/wer/all_sites/owais-portfolio/src/data/links/*.json'))

items = []
seen = set()
for f in FILES:
    name = f.split('/')[-1].replace('.json', '')
    for it in json.load(open(f)):
        key = (name, it['url'])
        items.append((name, it))
        seen.add(it['url'])

urls = [it['url'] for _, it in items]
with open('/tmp/opencode/links/urls.txt', 'w') as fh:
    fh.write('\n'.join(urls) + '\n')

print(f'{len(urls)} urls to check ({len(set(urls))} unique)')

UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'
cmd = (
    f"cat /tmp/opencode/links/urls.txt | xargs -P 24 -I{{}} "
    f"sh -c 'c=$(curl -k -s -o /dev/null -A \"{UA}\" --connect-timeout 8 -m 25 -L -w \"%{{http_code}}\" \"{{}}\" 2>/dev/null || echo 000); echo -e \"$c\\t{{}}\"'"
)
out = subprocess.run(cmd, shell=True, capture_output=True, text=True, executable='/bin/bash').stdout

ok, dead, warn = [], [], []
for line in out.splitlines():
    if not line.strip():
        continue
    code, url = line.split('\t', 1)
    code = code.strip()
    if code == '000':
        dead.append((code, url))
    elif code.startswith(('4', '5')) and code not in ('429', '403', '444', '450', '503', '451'):
        dead.append((code, url))
    else:
        ok.append((code, url))

print(f'OK/redirect: {len(ok)}  DEAD/bad-status: {len(dead)}')

with open('/tmp/opencode/links/dead.txt', 'w') as fh:
    for code, url in sorted(dead):
        fh.write(f'{code}\t{url}\n')

print('--- dead / questionable ---')
for code, url in sorted(dead):
    print(f'{code}  {url}')