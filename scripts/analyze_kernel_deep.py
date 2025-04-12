#!/usr/bin/python3

def analyze_kernel(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        
    print(f"File size: {len(data)} bytes")
    
    # Аналіз заголовка
    print("\nAnalyzing ARM header:")
    for i in range(0, 64, 4):
        word = int.from_bytes(data[i:i+4], byteorder='little')
        print(f"0x{i:04x}: 0x{word:08x}")
    
    # Пошук відомих рядків
    markers = [b'Linux version', b'ARM', b'Kernel', b'Booting']
    for marker in markers:
        positions = []
        pos = 0
        while True:
            pos = data.find(marker, pos)
            if pos == -1:
                break
            positions.append(pos)
            print(f"\nFound '{marker.decode()}' at offset 0x{pos:x}:")
            print(data[pos:pos+100])
            pos += 1

# Аналізуємо файл
analyze_kernel('kernel_25981f.bin')
