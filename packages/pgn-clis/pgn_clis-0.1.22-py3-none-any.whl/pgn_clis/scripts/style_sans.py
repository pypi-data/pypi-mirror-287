from argparse import ArgumentParser

def main():

  parser = ArgumentParser()
  parser.add_argument('-p', '--num-procs', type=int, default=None)
  parser.add_argument('-s', '--chunk-size', type=int, default=10000)
  parser.add_argument('-v', '--verbose', action='store_true')
  group = parser.add_mutually_exclusive_group()
  group.add_argument('-a', '--all', action='store_true', help='Use all languages (instead of english only)')
  group.add_argument('-l', '--languages', nargs='+', default=['EN'], help='Specify languages to use')
  group.add_argument('-n', '--num-langs', type=int, help='Number of languages to used (sliced from their predefined order)')

  args = parser.parse_args()

  import sys
  from pgn_clis.lib.style_sans import run_style_sans
  from chess_notation import LANGUAGES

  if args.all:
    languages = LANGUAGES
  else:
    if (bad_langs := set(args.languages) - set(LANGUAGES)):
      print(f'[ERROR] Received invalid languages: {list(bad_langs)}', file=sys.stderr)
      print(f'Accepted languages: {LANGUAGES}', file=sys.stderr)
      sys.exit(1)
    languages = args.languages
  
  run_style_sans(
    sys.stdin, sys.stdout, num_procs=args.num_procs, chunk_size=args.chunk_size,
    logstream=sys.stderr if args.verbose else None, languages=languages
  )