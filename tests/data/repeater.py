import sys
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='repeater')

    parser.add_argument(
        '-n',
        action='store',
        type=int,
        help='set N iteration'
    )

    parser.add_argument(
        '-i',
        action='store_true',
        default=False,
        help='set iteration interactively'
    )

    args = parser.parse_args()

    def iterate(start, end):
        for i in range(start, end):
            sys.stdout.write(str(i) + '\n')

        sys.stdout.flush()

    if args.i:
        while True:
            try:
                iteration = sys.stdin.readline().replace('\n', '')

                if iteration == 'exit':
                    sys.exit(2)

                iteration = int(iteration)

                if iteration <= 0:
                    raise ValueError
            except ValueError:
                sys.stderr.write('error\n')
                sys.stderr.flush()
                continue
            else:
                iterate(0, iteration)
    elif args.n:
        if args.n <= 0:
            sys.stderr.write('argument -n is lesser than 0.\n')
            sys.stderr.flush()

            sys.exit(1)

        iterate(0, args.n)
    else:
        sys.exit(1)

    sys.exit(0)
