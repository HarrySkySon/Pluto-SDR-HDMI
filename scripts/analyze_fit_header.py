#!/usr/bin/python3

def analyze_fit_header(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        
    # Шукаємо FIT magic number та секції
    print("Analyzing FIT image structure:")
    # FIT magic: 0xd00dfeed
    for i in range(len(data)-4):
        if data[i:i+4] == b'\xd0\x0d\xfe\xed':
            print(f"\nFound FIT header at offset: 0x{i:x}")
            # Показуємо 64 байти після заголовка
            print(f"Header content: {data[i:i+64].hex()}")

# Аналізуємо файл
analyze_fit_header('pluto_txrx.bin')
