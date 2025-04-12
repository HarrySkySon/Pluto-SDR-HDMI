import re

def extract_data_from_section(section_name, content):
    pattern = f'{section_name}.*?data = \\[(.*?)\\];'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        hex_str = match.group(1).replace('\n', '').replace(' ', '')
        return bytes.fromhex(hex_str)
    return None

with open('pluto_txrx.bin', 'rb') as f:
    content = f.read().decode('latin1')

for i, section in enumerate(['fdt@1', 'fdt@2', 'fdt@3']):
    data = extract_data_from_section(section, content)
    if data:
        with open(f'dts/rev{chr(65+i)}/pluto.dtb', 'wb') as f:
            f.write(data)
