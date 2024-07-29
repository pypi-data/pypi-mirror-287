from argparse import ArgumentParser

def main():

  parser = ArgumentParser()
  parser.add_argument('-p', '--num-procs', type=int, default=None)
  parser.add_argument('-s', '--chunk-size', type=int, default=10000)
  parser.add_argument('-v', '--verbose', action='store_true')

  args = parser.parse_args()

  import sys
  from pgn_clis.lib.sans2fens import run_sans2fens
  run_sans2fens(
    sys.stdin, sys.stdout, num_procs=args.num_procs, chunk_size=args.chunk_size,
    verbose=args.verbose
  )