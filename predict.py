import argparse
import os
import sys

def parse_args(args):
    parser = argparse.ArgumentParser(description='Predictor for UAQ Thesis')
    parser.add_argument('--input', '-i', required=True, help='Input mr file path')
    parser.add_argument('--output', '-o', help='Output segmentations file path')
    parser.add_argument('--device', '-d')
    return parser.parse_args(args)

def main(args):
    opts = parse_args(args)
    print("Input:", opts.input)
    print("Output:", opts.output)

    os.environ['nnUNet_raw'] = "nnUNet_raw"
    os.environ['nnUNet_preprocessed'] = "nnUNet_preprocessed"
    os.environ['nnUNet_results'] = "nnUNet_results"
    cmd_str = f"nnUNetv2_predict -i {opts.input} -o {opts.output} -d 001 -c 3d_fullres -f all -device {opts.device}"
    
    print("Executing command:", cmd_str)
    exit_code = os.system(cmd_str)
    if exit_code != 0:
        print("Error: Command execution failed with exit code", exit_code)

if __name__ == "__main__":
    main(sys.argv[1:])