import csv
import json
import logging
import sys

logging.getLogger().setLevel(logging.INFO)
SETTINGS_FILE = "files/settings.json"


class FileController:
    """Class for working with program files"""

    def __init__(self, json_file: str = SETTINGS_FILE) -> None:
        """
        Constructor
        :arg json_file - Path to .json file
        """
        settings = self.__read_settings(json_file)
        self.__hash_path = settings["hash"]
        self.__last_numbers_path = settings["last_numbers"]
        self.__bins_path = settings["bins"]
        self.__card_num_file_path = settings["card_number_file"]
        self.__statistic_file_path = settings["statistic_file"]
        self.__visual_directory = settings["visual_directory"]
        self.__luhn_result = settings["luhn_result"]
        self.__statistics_photo = settings["statistics_photo"]

    @property
    def hash_file_path(self) -> str:
        return self.__hash_path

    @property
    def last_num_file_path(self) -> str:
        return self.__last_numbers_path

    @property
    def card_num_file_path(self) -> str:
        return self.__card_num_file_path

    @property
    def luhn_result(self) -> str:
        return self.__luhn_result

    @property
    def visual_directory(self) -> str:
        return self.__visual_directory

    @property
    def statistics_photo(self) -> str:
        return self.__statistics_photo

    @staticmethod
    def __read_settings(settings_file: str) -> dict:
        """
        Method reads the settings file
        :arg settings_file - name of the settings file
        :return - dictionary of paths to program files
        """
        try:
            with open(settings_file) as json_file:
                settings = json.load(json_file)
            logging.info(
                f"Settings file successfully loaded from {settings_file}")
        except OSError as err:
            logging.warning(
                f"Settings file wasn't loaded from {settings_file}")
            sys.exit(err)
        return settings

    @staticmethod
    def read_text(file_path: str) -> str:
        """
        Method reads the text file
        :arg file_path - path to the file
        :return: text from the file
        """
        try:
            with open(file_path, "r") as text_file:
                text = text_file.read()
            logging.info(
                f"Text was successfully read from the file {file_path}")
        except OSError as err:
            logging.warning(
                f"Text wasn't read from the file {file_path}")
            sys.exit(err)
        return text

    @staticmethod
    def write_text(card_num: str, file_name: str) -> None:
        """
        Method writes the text into the file
        :arg card_num - the number of card
        :arg file_name - path to the file
        """
        try:
            with open(file_name, "w") as text_file:
                text_file.write(card_num)
            logging.info(
                f"Text was successfully written to the file {file_name}")
        except OSError as err:
            logging.warning(
                f"Text wasn't written to the file {file_name}")
            sys.exit(err)

    def read_bins(self) -> list:
        """
        Method reads the file containing bins
        :return - bins
        """
        try:
            bins = tuple(map(int, self.__bins_path))
            logging.info(
                f"List was successfully read from file {self.__bins_path}")
        except OSError as err:
            logging.warning(
                f"List was not read from file {self.__bins_path}")
            sys.exit(err)
        return bins

    def write_statistic(self, cores: int, time: float) -> None:
        """
        Method appends statistic data to the end of the file
        :arg cores - number of cores
        :arg time - time of enumerate
        """
        try:
            with open(self.__statistic_file_path, "a", newline="") as csv_file:
                writer = csv.writer(csv_file, delimiter=" ")
                writer.writerow([cores, time])
            logging.info(
                f"Statistic written to file {self.__statistic_file_path}")
        except OSError as err:
            logging.warning(
                f"Statistics wasn't written to the file {self.__statistic_file_path}")
            sys.exit(err)

    def load_stats(self) -> dict:
        """
        The function loads statistics from txt file
        :return - statistics of enumerate
        """
        statistics = {}
        try:
            with open(self.__statistic_file_path, "r") as text_file:
                lines = text_file.readlines()
        except OSError:
            logging.warning(
                f"Statistics wasn't read from the file {self.__statistic_file_path}")
        for line in lines:
            line = list(map(float, line.split()))
            statistics[line[0]] = line[1]
        logging.info(
            f"Statistics was successfully read from the file {self.__statistic_file_path}")
        return statistics
