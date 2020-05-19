from collections import defaultdict
import pandas as pd
import numpy as np


class DataObject():

    def __init__(self, file_path, bead_radius):
        self.file_path = file_path

        self._read_file()
        for k, v in self.meta_data.items():
            setattr(self, k, v)
            
        self.bead_radius = bead_radius
        self.results = dict()

    def _read_file(self):
        with open(self.file_path, "r") as f:
            lines = f.readlines()

        self.meta_data = defaultdict(dict)
        segment = "instrument"
        for line in lines:
            if "#" in line:
                meta_data = line.strip(" #").strip("\n").split(": ")
                if len(meta_data) > 1 and len(meta_data) <= 2:
                    key = meta_data[0]
                    key = ''.join(car for car in key if car.isalnum())
                    try:
                        value = eval(meta_data[1])
                    except:
                        value = meta_data[1]

                    if key == "segment":
                        segment = value
                        self.meta_data[segment][key] = value
                    else:
                        self.meta_data[segment][key] = value

        datasets = [[]]
        for line in lines:
            if line.startswith('#'):
                if datasets[-1] != []:
                    datasets.append([])
            else:
                strip_line = line.strip()
                if strip_line:
                    datasets[-1].append(strip_line.split())

        for segment, dataset in zip(list(self.meta_data.keys())[1:], datasets):
            df = pd.DataFrame(np.array(dataset).astype("float32"), columns=self.meta_data[segment]["columns"].split())
            setattr(self, f"{segment}_data", df)
