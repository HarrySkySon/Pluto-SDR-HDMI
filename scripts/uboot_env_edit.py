#!/usr/bin/python3

def modify_uboot_env(input_file, output_file):
    with open(input_file, 'rb') as f:
        content = f.read()

    # Розширений список замін
    replacements = [
        (b'qspiboot=set stdout nulldev', b'qspiboot=echo "Skip SPI boot"\0\0\0\0\0\0\0\0'),
        (b'qspiboot_verbose=', b'qspiboot_verbose=echo "Skip SPI boot verbose"\0\0'),
        (b'qspiboot_extraenv=', b'qspiboot_extraenv=echo "Skip SPI boot extra"\0\0'),
        (b'preboot=if test $modeboot = sdboot', b'preboot=echo "Force SD boot"\0\0\0\0\0\0\0\0'),
        (b'bootcmd=run $modeboot', b'bootcmd=run sdboot\0\0\0\0\0\0\0\0')
    ]

    modified = content
    for old, new in replacements:
        if old in modified:
            print(f"Replacing: {old}")
            modified = modified.replace(old, new)
        else:
            print(f"Warning: {old} not found")

    with open(output_file, 'wb') as f:
        f.write(modified)

# Використання
input_file = '/media/sf_ZYNQ_SDR_AD9361/Workflow/Files_of_board/pluto_txrx/pluto_txrx_original/uboot-env.bin'
output_file = '/media/sf_ZYNQ_SDR_AD9361/Workflow/Files_of_board/pluto_txrx/uboot-env-mod.bin'
modify_uboot_env(input_file, output_file)
