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
        self.__hash_file_path = settings["hash_file"]
        self.__last_numbers_file_path = settings["last_numbers_file"]
        self.__bins_file_path = settings["bins_file"]
        self.__card_num_file_path = settings["card_number_file"]
        self.__statistic_file_path = settings["statistic_file"]
        self.__visual_directory = settings["visual_directory"]

    @property
    def hash_file_path(self) -> str:
        return self.__hash_file_path

    @property
    def last_num_file_path(self) -> str:
        return self.__last_numbers_file_path

    @property
    def card_num_file_path(self) -> str:
        return self.__card_num_file_path

    @property
    def visual_directory(self) -> str:
        return self.__visual_directory

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


