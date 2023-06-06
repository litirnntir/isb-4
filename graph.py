import os
import logging
import matplotlib.pyplot as plt
import sys

logging.getLogger().setLevel(logging.INFO)


def visualize_statistics(statistics: dict, visual_directory: str, statistic_photo_directory: str) -> None:
    """
    The function visualize statistics and save the result to some directory
    :arg statistics - statistics for visualization
    :arg statistic_photo_directory - graph name
    :arg visual_directory - path to directory
    """
    plt.ylabel("Work time, s")
    plt.xlabel("Processes")
    plt.title("Enumeration statistics")
    pools, work_times = statistics.keys(), statistics.values()
    plt.bar(pools, work_times, color="purple", width=0.7)
    try:
        plt.savefig(os.path.join(visual_directory, statistic_photo_directory))
    except OSError as err:
        logging.warning(
            f"Bar chart wasn't saved to the directory {visual_directory}")
        sys.exit(err)
    logging.info(
        f"Bar chart was successfully saved to the directory {visual_directory}")
