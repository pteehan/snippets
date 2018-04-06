import argparse
parser = argparse.ArgumentParser(description="pipeline")

parser.add_argument('--n_sample', type=int, default=None)
parser.add_argument('--uuid_source', type=str, default="x")
parser.add_argument('--target', type=str, default="y")
parser.add_argument('--balance', action='store_true', default=False)
args = parser.parse_args()

args.n_sample
args.uuid_source
args.target
args.balance
# etc
