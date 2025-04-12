#!/usr/bin/python3

def analyze_fit_sections(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    
    print("Analyzing FIT image sections:")
    
    # Шукаємо рядки, що можуть вказувати на секції ядра
    kernel_markers = [b'kernel', b'linux', b'Image']
    
    for marker in kernel_markers:
        positions = []
        pos = 0
        while True:
            pos = data.find(marker, pos)
            if pos == -1:
                break
            positions.append(pos)
            pos += 1
        
        for pos in positions:
            print(f"\nFound '{marker.decode()}' at offset: 0x{pos:x}")
            # Показуємо 100 байт навколо знахідки
            start = max(0, pos - 50)
            end = min(len(data), pos + 50)
            print(f"Surrounding content: {data[start:end].hex()}")
            
            # Шукаємо розмір секції поблизу
            size_start = data.find(b'\x00\x00\x00', pos)
            if size_start != -1 and size_start < pos + 100:
                size_bytes = data[size_start:size_start+4]
                size = int.from_bytes(size_bytes, byteorder='big')
                print(f"Possible size found at 0x{size_start:x}: {size} bytes")

# Аналізуємо файл
analyze_fit_sections('pluto_txrx.bin')
