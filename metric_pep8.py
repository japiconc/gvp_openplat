"""
Script to check PEP8 complience for OpenPlatform - Enablers
"""
#!/usr/bin/python

import sys


STR_CHECKING = "checking "
STR_DIRECTORY = "directory "
EXCLUDED = [
    "D:\\WS_OpenPlat\\gvp-openplat\\src\\gvp_openplat\\grant_manager\\sync_services\\gal_connector\\schemas.py",
    "D:\\WS_OpenPlat\\gvp-openplat\\src\\gvp_openplat\\grant_manager\\sync_services\\gal_connector\\validators.py",
    "D:\\WS_OpenPlat\\gvp-openplat\\src\\gvp_openplat\\message_manager\\server\\schemas.py",
    "D:\\WS_OpenPlat\\gvp-openplat\\src\\gvp_openplat\\task_manager\\api\\schemas.py",
    "D:\\WS_OpenPlat\\gvp-openplat\\src\\gvp_openplat\\utils\\adm_client",
    "D:\\WS_OpenPlat\\gvp-openplat\\src\\gvp_openplat\\utils\\rmg_client",
    "D:\\WS_OpenPlat\\gvp-openplat\\src\\gvp_openplat\\utils\\ims_dim_client",
    "D:\\WS_OpenPlat\\gvp-openplat\\src\\gvp_openplat\\utils\\ims_topology_client",
    "D:\\WS_OpenPlat\\gvp-openplat\\src\\gvp_openplat\\utils\\mib_api_client\\opus_client",
]


def check_excluded(filename):
    for name in EXCLUDED:
        if name in filename:
            return True
    return False

def print_report(text, list_files):
    print("---------------------")
    print(" {} FILES ({})".format(text, len(list_files)))
    print("---------------------")

    count = 1
    for filename in list_files:
        print("{} - {}".format(count, filename))
        count += 1

    print("")


if len(sys.argv) <= 1:
    sys.exit(-1)

FILENAME = str(sys.argv[1])

with open(FILENAME) as fhandler:
    all_lines = fhandler.readlines()

error_files = []
ok_files=[]
excluded_files=[]

in_error = False
current_file = None

for line in all_lines:
    line = line.rstrip('\n')

    if not line.startswith(STR_CHECKING) and not line.startswith(STR_DIRECTORY):
        in_error = True
    else:
        if in_error and current_file:
            if check_excluded(current_file):
                excluded_files.append(current_file)
            else:
                error_files.append(current_file)
        elif current_file is not None:
            ok_files.append(current_file)

        if line.startswith(STR_CHECKING):
            current_file = line[len(STR_CHECKING):]
        else:
            current_file = None

        in_error = False

if in_error and current_file:
    error_files.append(current_file)
elif current_file is not None:
    ok_files.append(current_file)

print_report("OK", ok_files)
print_report("EXCLUDED", excluded_files)
print_report("ERROR", error_files)

pass
