#!/usr/bin/env python3

# Index database for MFEprimer-2.0
# Wubin Qu <quwubin@gmail.com>.

# python version written by Ulises Rosas <ulisesfrosasp@gmail.com>

import subprocess
import platform
import argparse
import re

def getOpts():
    parser = argparse.ArgumentParser(description="",usage= "IndexDb.py Fasta_file K_value")
    parser.add_argument('fasta_file', help="fasta file", type = str)
    parser.add_argument('-k',  metavar = "", default = 9, type = int, help = 'k value')
    args = parser.parse_args()
    return args

def runShell(args):
    p = subprocess.Popen(args)
    p.communicate()

def main():
    opts = getOpts()
    # print(opts)
    pltsys = platform.system()
    if not re.findall("(Darwin|Linux)", pltsys):
        print("\nNot recognizable Operative System\n")
        exit()

    bitarch = platform.architecture()[0].replace("bit", "")

    print("Begin indexing ...\n")

    runShell(
        "UniFastaFormat.py -i {0}"
            .format(opts.fasta_file)
            .split()
    )
    print("Step 1/3: UniFasta done.\n")

    runShell(
        "MFEprimer_{0}_{1}_faToTwoBit {2}.unifasta {2}.2bit"
            .format(pltsys, bitarch, opts.fasta_file)
            .split()
    )
    print("Step 2/3: faToTwoBit done.\n")

    print("Step 3/3: Index begin ...\n")
    runShell(
        "mfe_index_db.py -f {0}.unifasta -k {1}"
            .format(opts.fasta_file, opts.k)
            .split()
    )
    print("Step 3/3: Index done\n")

    runShell(
        "rm {0}.unifasta"
            .format(opts.fasta_file)
            .split()
    )

if __name__ == '__main__':
    main()
