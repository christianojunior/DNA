import sys, lib.dna_lib

if len(sys.argv) > 1:
    dev_id = lib.dna_lib.ip_to_id(sys.argv[1])
    modules = lib.dna_lib.get_modules(dev_id)
    lib.dna_lib.print_info(modules)

else:
    print("Usage: %s device_ip" % sys.argv[0])
