import os
import sys
import pandas as pd
import scipy.optimize as so
import matplotlib.pyplot as plt
from collections import defaultdict
import scipy.ndimage as gauss_filter

from nanodemo.functions import *
from nanodemo.dataobject import DataObject
from nanodemo.models import hertz_model, hertz_model2, line


class ProcessingObject():

    def __init__(self, path_to_file_or_list_of_files, bead_radius, opt_kwargs={}):
        
        if isinstance(path_to_file_or_list_of_files, str):
            self.dataobjs = [DataObject(path_to_file_or_list_of_files, bead_radius)]
        if isinstance(path_to_file_or_list_of_files, list):
            self.dataobjs = [DataObject(x, bead_radius) for x in path_to_file_or_list_of_files]

        self.opt_kwargs = opt_kwargs
        
        self.models = {
            'hertz_model':hertz_model,
            'hertz_model2':hertz_model2,
            'line':line,
            }

    def _preprocessing(self):
        for idx_data, dataobj in enumerate(self.dataobjs):
            d, f, t = dataobj.extend_data[['smoothedMeasuredHeight', 'vDeflection', 'time']].T.values
            

            baseline_perc = self.opt_kwargs.get("baseline_perc", 0.1)
            baseline_index = int(len(d) * baseline_perc)
            params, _ = so.curve_fit(linear, d[:baseline_index], f[:baseline_index])
            f = f - linear(d, *params)
            d = d.max() - d
    
    
            f = gauss_filter.gaussian_filter1d(f, 3)
    
            dataobj.dft = (d,f,t)
            sys.stdout.write(f"\r\t Preprocessed {dataobj.file_path} ({idx_data + 1} of out {len(self.dataobjs)})")
            sys.stdout.flush()

    def fit_models(self, *models, save_plot=False):
        self._preprocessing()
        sys.stdout.write("\n")
        sys.stdout.flush()
        for i_mod, model in enumerate(models):
            for i_dobj, dataobj in enumerate(self.dataobjs):
                model_results, func_vals = self.models[model](dataobj, self.opt_kwargs)
                dataobj.results[model] = model_results.best_values
                if save_plot:
                    plt.plot(func_vals[0], func_vals[1], label=f"{model} raw")
                    plt.plot(func_vals[0], func_vals[2], label=f"{model} fitted")
                    plt.legend()
                    plt.savefig(f"{dataobj.file_path.replace('.txt', f'_{model}.png')}")
                    plt.close()
                    
                sys.stdout.write(f"\r\tFitting {model} ({i_mod+1} out of {len(models)} models) for {dataobj.file_path} ({i_dobj+1} out of {len(self.dataobjs)} files)")
                sys.stdout.flush()

        

    def to_csv(self, file_path, **kwargs):
        results = defaultdict(list)
        sys.stdout.write("\n")
        sys.stdout.flush()
        for dataobj in self.dataobjs:
            results["Name"].append(dataobj.file_path)
            results["Fits"].append(dataobj.results)
        df =pd.DataFrame.from_dict(results).to_csv(file_path, **kwargs)
        abspath = os.path.abspath(file_path)
        sys.stdout.write(f"\r\t Results saved to {abspath})")
        sys.stdout.flush()
        
if __name__ == "__main__":
    pass
