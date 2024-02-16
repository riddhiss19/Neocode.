import json
import os
from collections import defaultdict
from typing import List, Dict


class DataManager:
    def __init__(self, data_dir: str) -> None:
        self.data_dir = data_dir
        self.cache = {}

    def get_data(self, key: str) -> List[Dict]:
        if key in self.cache:
            return self.cache[key]

        file_path = os.path.join(self.data_dir, f"{key}.json")
        if not os.path.exists(file_path):
            raise ValueError(f"No data file found for {key}")

        with open(file_path) as f:
            data = json.load(f)

        self.cache[key] = data
        return data


dm = DataManager("./data")
user_data = dm.get_data("users")
