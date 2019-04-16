from default_cell_library import Library
from majority_mapper import *
import sys


def main(argv):
    lib = Library()
    VP = VerilogParser(lib)
    if len(argv) < 2:
        print("Please enter input file")
        return
    file_name = argv[1]
    if not VP.read_file(file_name):
        print("File not found")
        return
    VP.read_file(file_name)
    mod = VP.parse()
    module = majority_mapper(mod, lib)
    module.net_renaming()
    module.instance_renaming()
    if len(argv) == 3:
        out_file = argv[2]
    else:
        out_file = file_name[:-2] + "_majority.v"
    with open(out_file, 'w+') as f:
        f.write(module.to_verilog())

main(sys.argv)