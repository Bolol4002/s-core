# Vivado Project Creation Script
# Run with: vivado -mode batch -source create_project.tcl

# Create project
create_project -part xc7a35tcpg236-1 -force

# Add source files
add_files [glob ../src/*.sv]

# Add constraints
add_files -fileset constrs_1 [glob ../constraints/*.xdc]

# Set top module
set_property top fpga_top [current_fileset]

# Run synthesis
launch_runs synth_1 -jobs 4
wait_on_run synth_1

# Run implementation
launch_runs impl_1 -to_step write_bitstream
wait_on_run impl_1

# Generate bitstream
open_run impl_1
write_bitstream -force fpga_top.bit

puts "Bitstream generated: fpga_top.bit"
