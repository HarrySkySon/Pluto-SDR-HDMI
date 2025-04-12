import re
import os

with open('pluto_txrx.bin', 'rb') as f:
    content = f.read()

dtb_starts = [m.start() for m in re.finditer(b'\xd0\x0d\xfe\xed', content)][:3]  # Беремо тільки перші 3

for i, start in enumerate(dtb_starts):
    with open(f'dts/rev{chr(65+i)}/pluto.dtb', 'wb') as f:
        f.write(content[start:start+24576])
