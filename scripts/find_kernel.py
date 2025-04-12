#!/usr/bin/python3

def find_kernel(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    
    # Шукаємо ARM Image заголовок (0x016f2818)
    print("Шукаємо Linux kernel magic number...")
    for i in range(len(data)-4):
        # ARM Linux magic 0x016f2818
        if data[i:i+4] == b'\x18\x28\x6f\x01':
            print(f"\nЗнайдено заголовок ядра на offset 0x{i:x}")
            # Виводимо метадані ядра
            header = data[i:i+0x40]
            print(f"Заголовок: {header.hex()}")
            size = int.from_bytes(header[4:8], byteorder='little')
            print(f"Розмір ядра: {size} bytes")
            return i, size

    return None, None

offset, size = find_kernel('pluto_txrx.bin')
if offset is not None:
    print(f"\nВитягуємо ядро...")
    with open('pluto_txrx.bin', 'rb') as f:
        f.seek(offset)
        kernel_data = f.read(size)
    with open('kernel.bin', 'wb') as f:
        f.write(kernel_data)
    print(f"Ядро збережено в kernel.bin")
