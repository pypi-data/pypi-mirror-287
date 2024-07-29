import argparse
import time

from src.throttle.throttle import Throttle


def main():
    parser = argparse.ArgumentParser(
        description="Throttle: A versatile progress indicator for your Python scripts.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="Example usage:\n"
               "  python cli.py --total 100 --progress 50 --style bar --color green\n"
               "  python cli.py --total 100 --progress 75 --style spinner\n"
               "  python cli.py --total 200 --progress 100 --style dots --fill * --empty -\n"
               "  python cli.py --total 50 --progress 25 --style time_clock"
    )

    parser.add_argument(
        '--total',
        type=int,
        required=True,
        help='The total number of steps or items to process (required).'
    )
    parser.add_argument(
        '--progress',
        type=int,
        required=True,
        help='The current progress (an integer between 0 and total).'
    )
    parser.add_argument(
        '--style',
        type=str,
        choices=['spinner', 'bar', 'dots', 'time_clock'],
        default='bar',
        help='The style of progress indicator (default: bar).'
    )
    parser.add_argument(
        '--color',
        type=str,
        choices=['blue', 'green', 'red'],
        default='blue',
        help='The color of the progress bar (default: blue).'
    )
    parser.add_argument(
        '--fill',
        type=str,
        default='#',
        help='The character used to fill the progress bar (default: #).'
    )
    parser.add_argument(
        '--empty',
        type=str,
        default=' ',
        help='The character used for the empty part of the progress bar (default: space).'
    )
    parser.add_argument(
        '--desc',
        type=str,
        default='Progress',
        help='A short description of the task in progress (default: "Progress").'
    )
    parser.add_argument(
        '--demo',
        action='store_true',
        help='Run a demo showing the progress indicator in action.'
    )

    args = parser.parse_args()

    # Validation
    if args.progress < 0 or args.progress > args.total:
        parser.error("Progress must be an integer between 0 and total.")

    # Create Throttle instance
    loader = Throttle(total=args.total,
                      desc=args.desc,
                      style=args.style,
                      color=args.color,
                      fill_char=args.fill,
                      empty_char=args.empty)
    loader.completed = args.progress

    if args.demo:
        loader.start()
        for i in range(loader.completed, loader.total + 1):
            time.sleep(0.1)  # Simulate a task
            loader.update()
        loader.close()
    else:
        print(loader.render())


if __name__ == "__main__":
    main()
