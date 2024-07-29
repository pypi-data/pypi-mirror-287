import csv
import os

from typing import List, Dict, Optional, Tuple

from scipy.spatial import KDTree


class Geo2Zip:
    def __init__(self, path: Optional[str] = None):
        """
        Initializes the Geo2Zip object and builds the KDTree from CSV files in the provided path.

        :param path: Path to the CSV file or directory containing CSV files with geo-coordinates and zip codes.
        """
        if path is None:
            path = os.path.join(os.path.dirname(__file__), 'data')

        if os.path.isdir(path):
            self.data = self._read_csv_files(path)
        elif os.path.isfile(path):
            self.data = self._read_csv(path)
        else:
            raise ValueError(f"The provided path '{path}' is neither a directory nor a file.")

        self.tree, self.geoids, self.countries = self._build_kdtree(self.data)

    def _read_csv_files(self, directory_path: str) -> List[Dict[str, str]]:
        """
        Reads all CSV files in the given directory and returns a list of dictionaries representing the rows.

        :param directory_path: Path to the directory containing CSV files.
        :return: List of dictionaries with CSV data.
        """
        all_data = []
        for filename in os.listdir(directory_path):
            if filename.endswith('.csv'):
                file_path = os.path.join(directory_path, filename)
                all_data.extend(self._read_csv(file_path))
        return all_data

    def _read_csv(self, file_path: str) -> List[Dict[str, str]]:
        """
        Reads a single CSV file and returns a list of dictionaries representing the rows.

        :param file_path: Path to the CSV file.
        :return: List of dictionaries with CSV data.
        """
        try:
            with open(file_path, mode='r', newline='') as csvfile:
                sample = csvfile.read(1024)
                csvfile.seek(0)
                dialect = csv.Sniffer().sniff(sample)
                reader = csv.DictReader(csvfile, dialect=dialect)
                return [row for row in reader]
        except FileNotFoundError:
            raise FileNotFoundError(f"CSV file not found at path: {file_path}")
        except csv.Error as e:
            raise Exception(f"Error detecting CSV dialect: {e}")
        except Exception as e:
            raise Exception(f"Error reading CSV file: {e}")

    def _build_kdtree(self, data: List[Dict[str, str]]) -> Tuple[KDTree, List[str], List[str]]:
        """
        Builds a KDTree from the provided data.

        :param data: List of dictionaries containing geo-coordinates, zip codes, and country names.
        :return: A tuple containing the KDTree, a list of Zip/Postal codes, and a list of countries
        """
        coordinates, geoids, countries = [], [], []

        for row in data:
            try:
                lat = float(row['LAT'])
                lon = float(row['LONG'])
                coordinates.append((lat, lon))
                geoids.append(row['GEOID'])
                countries.append(row['COUNTRY'])
            except ValueError:
                # Skip rows with invalid coordinates
                continue

        tree = KDTree(coordinates)
        return tree, geoids, countries

    def find_closest_zip(self, lat: float, lon: float) -> Tuple[str, str]:
        """
        Finds the closest zip code and country name for the given latitude and longitude using the KDTree.

        :param lat: Latitude of the query point.
        :param lon: Longitude of the query point.
        :return: A tuple containing the Zip/Postal code and the country name of the closest point.
        """
        distance, index = self.tree.query((lat, lon))
        return self.geoids[index], self.countries[index]

