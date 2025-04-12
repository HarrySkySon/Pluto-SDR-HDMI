#!/usr/bin/python3

def extract_kernel(filename, offset=0x22d92f0, size=4328000):
    print(f"Extracting kernel from offset 0x{offset:x}, size: {size} bytes")
    try:
        with open(filename, 'rb') as f:
            # Переходимо до позиції ядра
            f.seek(offset)
            # Читаємо дані ядра
            kernel_data = f.read(size)
            
            if len(kernel_data) != size:
                print(f"Warning: Read only {len(kernel_data)} bytes instead of {size}")
            
            # Зберігаємо перші 16 байт для перевірки
            print(f"First 16 bytes: {kernel_data[:16].hex()}")
            
            # Записуємо ядро
            with open('kernel.bin', 'wb') as out:
                out.write(kernel_data)
            
            print(f"Kernel saved to kernel.bin")
    except Exception as e:
        print(f"Error: {e}")

# Витягуємо ядро
extract_kernel('pluto_txrx.bin')
