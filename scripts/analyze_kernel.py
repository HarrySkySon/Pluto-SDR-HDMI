#!/usr/bin/python3

def analyze_kernel(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        
    print(f"File size: {len(data)} bytes")
    print("\nFirst 64 bytes:")
    print(data[:64].hex())
    
    # Шукаємо рядки Linux
    pos = data.find(b'Linux version')
    if pos != -1:
        print("\nFound Linux version string at offset:", hex(pos))
        print(data[pos:pos+100])

# Аналізуємо найбільш вірогідний файл
analyze_kernel('kernel_25981f.bin')
