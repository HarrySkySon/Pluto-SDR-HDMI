#!/usr/bin/python3
import os

def debug_file_content(filename):
    print(f"\nDebug info for {filename}:")
    file_size = os.path.getsize(filename)
    print(f"File size: {file_size} bytes")
    
    if file_size > 0:
        with open(filename, 'rb') as f:
            # Читаємо перші 100 байт для аналізу
            data = f.read(100)
            print(f"First 100 bytes: {data.hex()}")

def extract_kernel(input_file, offset=0x22d92f0, size=4328000):
    print(f"Attempting to extract kernel:")
    print(f"Input file: {input_file}")
    print(f"Offset: 0x{offset:x} ({offset})")
    print(f"Size: {size} bytes")
    
    try:
        # Перевіряємо вхідний файл
        input_size = os.path.getsize(input_file)
        print(f"\nInput file size: {input_size} bytes")
        
        if offset >= input_size:
            print(f"Error: Offset (0x{offset:x}) is beyond file size!")
            return
        
        with open(input_file, 'rb') as f:
            # Переходимо до позиції ядра
            f.seek(offset)
            print(f"Seeked to position: 0x{offset:x}")
            
            # Читаємо заголовок
            header = f.read(16)
            print(f"Header bytes: {header.hex()}")
            
            # Повертаємось на початок ядра
            f.seek(offset)
            
            # Читаємо все ядро
            kernel_data = f.read(size)
            actual_read = len(kernel_data)
            print(f"\nActually read: {actual_read} bytes")
            
            if actual_read != size:
                print(f"Warning: Expected to read {size} bytes, but got {actual_read}")
            
            if actual_read > 0:
                with open('kernel.bin', 'wb') as out:
                    out.write(kernel_data)
                print("\nKernel saved to kernel.bin")
                debug_file_content('kernel.bin')
            else:
                print("Error: No data read!")
                
    except Exception as e:
        print(f"Error: {str(e)}")

# Витягуємо ядро
extract_kernel('pluto_txrx.bin')
