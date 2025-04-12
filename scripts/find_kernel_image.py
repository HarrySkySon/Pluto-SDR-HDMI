#!/usr/bin/python3

def find_kernel_image(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    
    # Пошук ARM Linux Image header (0xea000000)
    header = bytes([0xea, 0x00, 0x00, 0x00])
    
    print("Searching for ARM Linux kernel header...")
    pos = 0
    while True:
        pos = data.find(header, pos)
        if pos == -1:
            break
            
        print(f"\nPotential kernel at offset: 0x{pos:x}")
        # Показати 32 байти навколо знахідки
        start = max(0, pos - 16)
        end = min(len(data), pos + 16)
        print(f"Content: {data[start:end].hex()}")
        
        # Зберегти потенційне ядро
        kernel_data = data[pos:pos + 4328000]
        with open(f'kernel_{pos:x}.bin', 'wb') as out:
            out.write(kernel_data)
        print(f"Saved potential kernel to kernel_{pos:x}.bin")
        
        pos += 4

find_kernel_image('pluto_txrx.bin')
