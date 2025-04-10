# Custom Linux Image for Enhanced PlutoSDR Board

## Overview

This repository contains a complete solution for a modified PlutoSDR board with enhanced hardware capabilities, including both the FPGA design and custom Linux image. The project provides full support for additional hardware features while maintaining original SDR functionality.

## Hardware Modifications

The enhanced PlutoSDR board includes:

- HDMI output port connected to Bank 35 of the FPGA
- Expanded RAM (2 × MT41J64M16JT-187E, total 1GB DDR3)
- Ethernet port
- NAND flash memory
- Additional GPIO functionality

## FPGA Design

### Block Design Features

The custom Vivado block design combines SDR functionality with HDMI output:

- **Radio Module**: Full integration of the AD9361 transceiver supporting the 70 MHz to 6 GHz frequency range
- **Dual-channel Configuration**: 2 RX channels (I and Q) and 2 TX channels (I and Q)
- **HDMI Subsystem**: Native HDMI output at 720p resolution through Bank 35
- **Clock Management**: Dynamic clock generation for HDMI timing
- **FPGA Resources Optimization**: Efficient resource utilization for both radio and display functionality

### FPGA Design Structure

The block design includes:

1. **Processing System**: Zynq-7020 PS configuration with DDR3 memory controller
2. **Radio Interface**: AD9361 interface with AXI Stream DMA controllers
3. **HDMI Components**:
   - Video Timing Controller (VTC)
   - AXI Video DMA (VDMA)
   - Dynamic Clock Generator
   - RGB to DVI Encoder
   - Supporting components (clock wizards, reset controllers)

### Design Considerations

- **Memory Mapping**: Careful allocation of memory spaces to avoid conflicts
- **Clock Domains**: Separate clock domains for radio and video subsystems
- **IO Standards**: LVCMOS25/TMDS_33 for HDMI signals, compatible with the radio interface requirements
- **Interrupts**: Proper interrupt assignment to avoid conflicts

## Repository Structure

```
├── fpga/
│   ├── hdl/                         # HDL source files
│   ├── constraints/                 # XDC constraint files
│   ├── ip/                          # Custom and third-party IP cores
│   ├── block_design/                # Block design TCL files
│   └── bitstream/                   # Generated bitstream files
├── linux/                           # Linux kernel source
├── scripts/
│   ├── analyze_config.sh            # Kernel config analysis
│   ├── analyze_fit_structure.py     # FIT image structure analysis
│   ├── extract_fpga_final.py        # FPGA bitstream extraction
│   ├── extract_ramdisk.py           # Ramdisk extraction
│   └── analyze_pluto_dts.py         # Device Tree analysis
├── config/
│   ├── pluto_custom.its             # FIT image description
│   └── kernel.config                # Kernel configuration
├── dts/
│   └── pluto.dts                    # Custom Device Tree
├── original/                        # Original manufacturer files
│   ├── boot.bin
│   ├── fsbl.elf
│   ├── pluto_txrx.bin
│   └── uboot-env.bin
├── gcc-arm-8.2-2018.08-x86_64-arm-linux-gnueabihf.tar.xz  # Cross-compiler
└── README.md
```

## Why This Project?

The original PlutoSDR firmware doesn't support the additional hardware features. This custom image enables:

1. Standalone operation with HDMI display
2. Full utilization of 1GB RAM
3. Network connectivity via Ethernet
4. Additional storage with NAND
5. Enhanced GPIO capabilities

## Features

- Custom FPGA design with integrated HDMI and radio functionality
- Modified Linux kernel based on Analog Devices repository with added drivers
- Device Tree supporting all hardware components
- HDMI output support at 720p resolution
- Full 1GB RAM support
- Ethernet connectivity
- NAND storage support

## Building

### Prerequisites:

- Vivado 2019.1 or later (for FPGA design)
- ARM cross-compiler (included in the repository)
- Device Tree Compiler
- U-Boot tools
- Python 3.x

### Building the FPGA Design:

```bash
# Build the FPGA bitstream
cd fpga
vivado -mode batch -source build_bitstream.tcl
```

### Building the Linux Kernel:

```bash
# Extract the cross-compiler
tar -xf gcc-arm-8.2-2018.08-x86_64-arm-linux-gnueabihf.tar.xz
export PATH=$PATH:$(pwd)/gcc-arm-8.2-2018.08-x86_64-arm-linux-gnueabihf/bin

# Configure and build kernel
cd linux
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- pluto_defconfig
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- -j$(nproc)

# Build Device Tree
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- dtbs

# Create FIT image
mkimage -f ../config/pluto_custom.its ../pluto_txrx.bin
```

**Note**: This project specifically uses the gcc-arm-8.2-2018.08 cross-compiler to avoid compilation errors and ensure proper kernel operation. Other compiler versions may result in unstable or non-functional images. The required compiler is included in this repository.

## Installation

1. Format SD card (FAT32)
2. Copy pluto_txrx.bin and uEnv.txt to SD card
3. Insert SD card into PlutoSDR
4. Power on device

## FPGA Design Details

### Radio Configuration

The radio subsystem is configured to support the full capabilities of the AD9361 transceiver:

- Frequency range: 70 MHz - 6 GHz
- Bandwidth support: up to 56 MHz
- ADC/DAC resolution: 12-bit
- Sample rate: up to 61.44 MSPS

### HDMI Output

The HDMI subsystem supports standard display formats:

- Resolution: 1280x720 (720p)
- Refresh rate: 60Hz
- Color depth: 24-bit (RGB888)
- HDMI 1.4 compliant

### Integration Challenges

Several challenges were addressed in this design:

1. **IO Bank Constraints**: Both HDMI and radio use dedicated banks with specific IO standards
2. **Memory Bandwidth**: Allocation of AXI bandwidth for both video and radio data
3. **Clock Domain Crossing**: Proper synchronization between different clock domains
4. **Driver Compatibility**: Ensuring Linux drivers work with custom hardware

## Current Status

Working:
- System boot with custom FPGA bitstream
- 1GB RAM recognition
- Basic system functionality
- USB interface
- HDMI output
- Radio functionality

## Contributing

Contributions are welcome! Please read our contributing guidelines and submit pull requests.

## License

GNU General Public License v3.0

## Acknowledgments

- Analog Devices for the original PlutoSDR
- Linux kernel community
- Xilinx for Zynq support
- Digilent for HDMI IP cores

**Note: This project is not affiliated with Analog Devices or the original PlutoSDR manufacturers.**
