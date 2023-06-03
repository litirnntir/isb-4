import argparse
import logging
import time

from enumeration import enumerate_card_num
from file_manager import FileController
from luhn import luhn_algorithm
from graph import visualize_statistics

logging.getLogger().setLevel(logging.INFO)


def main():
    """
    A function that can iterate over the card number
    by its hash, check the correctness of the card
    number and visualize the file with the
    enumeration statistics
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-set",
        "--settings",
        type=str,
        help="Using your own settings file"
    )
    parser.add_argument(
        "-sts",
        "--statistics",
        action="store_true",
        help="Saves statistics to a file"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-enu",
        "--enumeration",
        type=int,
        help="Entering the number of processes for"
             "selecting the card number by its hash"
    )
    group.add_argument(
        "-luh",
        "--luhn",
        action="store_true",
        help="Checking the correctness of"
             "the received card number"
    )
    group.add_argument(
        "-vis",
        "--visualization",
        action="store_true",
        help="Visualizes data from a"
             "file with statistics"
    )
    args = parser.parse_args()
    files = FileController(args.settings) if args.settings else FileController()
    if args.enumeration:
        hash_file = files.read_text(files.hash_file_path)
        last_num = files.read_text(files.last_num_file_path)
        bins = files.read_bins()
        start = time.perf_counter()
        card_num = enumerate_card_num(hash_file, last_num, bins, args.enumeration)
        finish = time.perf_counter()
        if card_num:
            logging.info(
                f"The card number matches the given hash was found")
            files.write_text(card_num, files.card_num_file_path)
            files.write_statistic(args.enumeration, finish - start)
        else:
            logging.info("The card number wasn't found")
    elif args.luhn:
        card_number = files.read_text(files.card_num_file_path)
        if luhn_algorithm(card_number):
            logging.info("The card number is correct")
        else:
            logging.info("The card number isn't correct")
    elif args.visualization:
        stats = files.load_stats()
        visualize_statistics(stats, files.visual_directory)


if __name__ == "__main__":
    main()
