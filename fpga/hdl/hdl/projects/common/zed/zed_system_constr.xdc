# constraints
# hdmi

set_property -dict {PACKAGE_PIN V5 IOSTANDARD LVCMOS33} [get_ports hdmi_out_clk]
set_property -dict {PACKAGE_PIN V10 IOSTANDARD LVCMOS33 IOB TRUE} [get_ports hdmi_vsync]
set_property -dict {PACKAGE_PIN V6 IOSTANDARD LVCMOS33 IOB TRUE} [get_ports hdmi_hsync]
set_property -dict {PACKAGE_PIN W6 IOSTANDARD LVCMOS33 IOB TRUE} [get_ports hdmi_data_e]
set_property -dict {PACKAGE_PIN U10 IOSTANDARD LVCMOS33 IOB TRUE} [get_ports {hdmi_data[0]}]
set_property -dict {PACKAGE_PIN Y7 IOSTANDARD LVCMOS33 IOB TRUE} [get_ports {hdmi_data[1]}]
set_property -dict {PACKAGE_PIN Y6 IOSTANDARD LVCMOS33 IOB TRUE} [get_ports {hdmi_data[2]}]
set_property -dict {PACKAGE_PIN Y9 IOSTANDARD LVCMOS33 IOB TRUE} [get_ports {hdmi_data[3]}]
set_property -dict {PACKAGE_PIN Y8 IOSTANDARD LVCMOS33 IOB TRUE} [get_ports {hdmi_data[4]}]
set_property -dict {PACKAGE_PIN V8 IOSTANDARD LVCMOS33 IOB TRUE} [get_ports {hdmi_data[5]}]
set_property -dict {PACKAGE_PIN W8 IOSTANDARD LVCMOS33 IOB TRUE} [get_ports {hdmi_data[6]}]
set_property -dict {PACKAGE_PIN W10 IOSTANDARD LVCMOS33 IOB TRUE} [get_ports {hdmi_data[7]}]
set_property -dict {PACKAGE_PIN W9 IOSTANDARD LVCMOS33 IOB TRUE} [get_ports {hdmi_data[8]}]
set_property -dict {PACKAGE_PIN U9 IOSTANDARD LVCMOS33 IOB TRUE} [get_ports {hdmi_data[9]}]
set_property -dict {PACKAGE_PIN U8 IOSTANDARD LVCMOS33 IOB TRUE} [get_ports {hdmi_data[10]}]
set_property -dict {PACKAGE_PIN W11 IOSTANDARD LVCMOS33 IOB TRUE} [get_ports {hdmi_data[11]}]
set_property -dict {PACKAGE_PIN Y11 IOSTANDARD LVCMOS33 IOB TRUE} [get_ports {hdmi_data[12]}]
set_property -dict {PACKAGE_PIN T5 IOSTANDARD LVCMOS33 IOB TRUE} [get_ports {hdmi_data[13]}]
set_property -dict {PACKAGE_PIN U5 IOSTANDARD LVCMOS33 IOB TRUE} [get_ports {hdmi_data[14]}]
set_property -dict {PACKAGE_PIN Y12 IOSTANDARD LVCMOS33 IOB TRUE} [get_ports {hdmi_data[15]}]

# spdif

set_property -dict {PACKAGE_PIN Y13 IOSTANDARD LVCMOS33} [get_ports spdif]

# i2s

#set_property  -dict {PACKAGE_PIN  L15   IOSTANDARD LVCMOS25} [get_ports i2s_mclk]
#set_property  -dict {PACKAGE_PIN  K16   IOSTANDARD LVCMOS25} [get_ports i2s_bclk]
#set_property  -dict {PACKAGE_PIN  J16   IOSTANDARD LVCMOS25} [get_ports i2s_lrclk]
#set_property  -dict {PACKAGE_PIN  J15    IOSTANDARD LVCMOS25} [get_ports i2s_sdata_out]
#set_property  -dict {PACKAGE_PIN  R19   IOSTANDARD LVCMOS25} [get_ports i2s_sdata_in]


# iic

#set_property  -dict {PACKAGE_PIN  T11    IOSTANDARD LVCMOS25} [get_ports iic_scl]
#set_property  -dict {PACKAGE_PIN  T10    IOSTANDARD LVCMOS25} [get_ports iic_sda]
#set_property  -dict {PACKAGE_PIN  T12  IOSTANDARD LVCMOS25 PULLTYPE PULLUP} [get_ports iic_mux_scl[1]]
#set_property  -dict {PACKAGE_PIN  U12   IOSTANDARD LVCMOS25 PULLTYPE PULLUP} [get_ports iic_mux_sda[1]]
#set_property  -dict {PACKAGE_PIN  U13   IOSTANDARD LVCMOS25 PULLTYPE PULLUP} [get_ports iic_mux_scl[0]]
#set_property  -dict {PACKAGE_PIN  V12   IOSTANDARD LVCMOS25 PULLTYPE PULLUP} [get_ports iic_mux_sda[0]]

# otg

set_property -dict {PACKAGE_PIN K16 IOSTANDARD LVCMOS25} [get_ports otg_vbusoc]

# gpio (switches, leds and such)

set_property -dict {PACKAGE_PIN M14 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[0]}]
set_property -dict {PACKAGE_PIN L15 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[1]}]
set_property -dict {PACKAGE_PIN L14 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[2]}]
set_property -dict {PACKAGE_PIN N16 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[3]}]
set_property -dict {PACKAGE_PIN N15 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[4]}]
set_property -dict {PACKAGE_PIN J14 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[5]}]
set_property -dict {PACKAGE_PIN K14 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[6]}]
set_property -dict {PACKAGE_PIN G15 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[7]}]
set_property -dict {PACKAGE_PIN H15 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[8]}]
set_property -dict {PACKAGE_PIN H20 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[9]}]
set_property -dict {PACKAGE_PIN J20 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[10]}]

set_property -dict {PACKAGE_PIN G18 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[11]}]
set_property -dict {PACKAGE_PIN G17 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[12]}]
set_property -dict {PACKAGE_PIN F20 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[13]}]
set_property -dict {PACKAGE_PIN F19 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[14]}]
set_property -dict {PACKAGE_PIN H18 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[15]}]
set_property -dict {PACKAGE_PIN J18 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[16]}]
set_property -dict {PACKAGE_PIN H16 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[17]}]
set_property -dict {PACKAGE_PIN K18 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[18]}]

set_property -dict {PACKAGE_PIN K17 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[19]}]
set_property -dict {PACKAGE_PIN L17 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[20]}]
set_property -dict {PACKAGE_PIN L16 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[21]}]
set_property -dict {PACKAGE_PIN J19 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[22]}]
set_property -dict {PACKAGE_PIN K19 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[23]}]
set_property -dict {PACKAGE_PIN L19 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[24]}]
set_property -dict {PACKAGE_PIN M18 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[25]}]
set_property -dict {PACKAGE_PIN M17 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[26]}]

set_property -dict {PACKAGE_PIN F17 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[27]}]
set_property -dict {PACKAGE_PIN F16 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[28]}]
set_property -dict {PACKAGE_PIN E19 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[29]}]
set_property -dict {PACKAGE_PIN E18 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[30]}]

set_property -dict {PACKAGE_PIN D20 IOSTANDARD LVCMOS25} [get_ports {gpio_bd[31]}]

# Define SPI clock
create_clock -period 40.000 -name spi0_clk [get_pins -hier */EMIOSPI0SCLKO]
create_clock -period 40.000 -name spi1_clk [get_pins -hier */EMIOSPI1SCLKO]

set_property PACKAGE_PIN N20 [get_ports {rx_data_in_p[0]}]

set_property BITSTREAM.GENERAL.COMPRESS TRUE [current_design]
