
# PlanAhead Launch Script for Pre-Synthesis Floorplanning, created by Project Navigator

create_project -name LCD -dir "C:/Users/Aleksandar/Desktop/Arhitekture2/LCD/planAhead_run_1" -part xc3s500efg320-4
set_param project.pinAheadLayout yes
set srcset [get_property srcset [current_run -impl]]
set_property target_constrs_file "lcdtest.ucf" [current_fileset -constrset]
set hdlfile [add_files [list {lcdtest.vhd}]]
set_property file_type VHDL $hdlfile
set_property library work $hdlfile
set_property top lcdtest $srcset
add_files [list {lcdtest.ucf}] -fileset [get_property constrset [current_run]]
open_rtl_design -part xc3s500efg320-4
