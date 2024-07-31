# greydata/cli.py

import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Greydata: A command line tool for processing data.'
    )
    
    parser.add_argument(
        '-i', '--input', 
        type=str, 
        required=True, 
        help='Path to the input file.'
    )
    
    parser.add_argument(
        '-o', '--output', 
        type=str, 
        required=True, 
        help='Path to the output file.'
    )
    
    parser.add_argument(
        '-v', '--verbose', 
        action='store_true', 
        help='Increase output verbosity.'
    )
    
    return parser.parse_args()

def main():
    args = parse_arguments()

    if args.verbose:
        print(f"Input file: {args.input}")
        print(f"Output file: {args.output}")
    
    print("Processing data...")

if __name__ == "__main__":
    main()
