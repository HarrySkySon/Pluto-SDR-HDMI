#!/usr/bin/env python3
import hashlib
import os

def extract_ramdisk(file_path, output_path):
    try:
        # Перевіряємо доступ до вхідного файлу
        if not os.path.exists(file_path):
            print(f"Error: Input file {file_path} not found!")
            return False
            
        print(f"Input file size: {os.path.getsize(file_path)} bytes")
        
        # Відомі параметри
        ramdisk_offset = 0x679de0
        data_size = 16995570  # розмір з dumpimage -l
        expected_md5 = "df5f0b842ce8a5cfaa680ddb4939641c"  # з dumpimage -l
        
        print("\nStarting extraction process...")
        with open(file_path, 'rb') as f:
            # Перевіряємо розмір файлу
            f.seek(0, 2)
            file_size = f.tell()
            print(f"Total file size: {file_size} bytes")
            
            if ramdisk_offset + data_size > file_size:
                print("Error: Calculated data range exceeds file size!")
                return False
            
            # Читаємо дані
            print(f"Seeking to offset 0x{ramdisk_offset:x}")
            f.seek(ramdisk_offset)
            ramdisk_data = f.read(data_size)
            print(f"Read {len(ramdisk_data)} bytes")
            
            # Перевіряємо MD5
            calculated_md5 = hashlib.md5(ramdisk_data).hexdigest()
            
            print(f"\nData extraction details:")
            print(f"Offset: 0x{ramdisk_offset:x}")
            print(f"Data size: {data_size} bytes")
            print(f"Calculated MD5: {calculated_md5}")
            print(f"Expected MD5: {expected_md5}")
            
            if calculated_md5 == expected_md5:
                print("\nMD5 match! Extracting ramdisk...")
                try:
                    with open(output_path, 'wb') as out:
                        out.write(ramdisk_data)
                    print(f"Successfully wrote {len(ramdisk_data)} bytes to {output_path}")
                    return True
                except Exception as e:
                    print(f"Error writing output file: {e}")
                    return False
            
            print("\nMD5 mismatch! Trying to find correct offset...")
            search_range = 512
            for offset in range(ramdisk_offset - search_range, ramdisk_offset + search_range, 4):
                print(f"Trying offset 0x{offset:x}", end='\r')
                f.seek(offset)
                test_data = f.read(data_size)
                test_md5 = hashlib.md5(test_data).hexdigest()
                
                if test_md5 == expected_md5:
                    print(f"\nFound correct offset at 0x{offset:x}")
                    try:
                        with open(output_path, 'wb') as out:
                            out.write(test_data)
                        print(f"Successfully wrote {len(test_data)} bytes to {output_path}")
                        return True
                    except Exception as e:
                        print(f"Error writing output file: {e}")
                        return False
            
            print("\nCould not find correct data!")
            return False
            
    except Exception as e:
        print(f"Error during extraction: {e}")
        return False

if __name__ == "__main__":
    input_file = "pluto_txrx.bin"
    output_file = "ramdisk.img.gz"  # .gz розширення тому що ramdisk стиснутий
    print(f"Starting ramdisk extraction from {input_file}")
    if extract_ramdisk(input_file, output_file):
        print(f"Ramdisk successfully extracted to {output_file}")
    else:
        print("Failed to extract ramdisk")
