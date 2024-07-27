import argparse
import os
from src.app.data_generation import DataGeneration


def main():

    parser = argparse.ArgumentParser(description="Data generation CLI")
    subparsers = parser.add_subparsers(dest='command', required=True)

    parser_refine = subparsers.add_parser('run', help='Generate data. I.e. 5 indoor houseplants')
    parser_refine.add_argument('--prompt', type=str, help='Pass what data you would like to be generated.')

    args = parser.parse_args()

    generator = DataGeneration()
    if args.command =='run':
        json_object = generator.generate(args.prompt)
        print(json_object)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()