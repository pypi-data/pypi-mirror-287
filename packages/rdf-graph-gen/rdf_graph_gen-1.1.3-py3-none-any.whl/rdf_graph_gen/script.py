import argparse
from rdf_graph_gen.rdf_graph_generator import *


def main():
    parser = argparse.ArgumentParser(description="CLI for processing two files.")
    parser.add_argument("file1", help="Path to the input file")
    parser.add_argument("file2", help="Path to the output file")
    parser.add_argument("instance_no", help="Number of instances that should be generated")

    args = parser.parse_args()
    generate_rdf(args.file1, args.file2, int(args.instance_no))


if __name__ == "__main__":
    main()
