import sys
import os
sys.path.insert(0, os.path.dirname(os.getcwd()))

# add the demo package to the path

import nanodemo as nd
import glob
from argparse_prompt import PromptParser


def add_arguments(parser):
    parser.add_argument("--path", type=str, help="Enter path to folder as 'folder' or txt file as 'file_name.txt'")
    parser.add_argument("--bead_radius", type=float, help="Enter bead radius in m i.e. 18.5e-6")
    parser.add_argument("--models", type=str, help="Enter models you want to fit the data to i.e. 'hertz_model, hertz_model2'")
    parser.add_argument("--save_plot", default=True, help="Set 'True' to save plot from fit otherwise set 'False'")


def main():
    parser = PromptParser()
    add_arguments(parser)
    args = parser.parse_args()
    
    PATH = "data" # OR IT TAKES A .TXT FILE
    BEAD_RADIUS = 18.5e-6
    MODELS = "hertz_model, line"
    SAVE = False
    
    
    if ".txt" in args.path:
        files = args.path
    else:
        files = glob.glob(f"{args.path}/*.txt")
    
    obj = nd.ProcessingObject(files, args.bead_radius)
    
    models = [x.strip() for x in args.models.split(",")]
    
    obj.fit_models(*models, save_plot=args.save_plot)
    
    obj.to_csv("results_demo2.csv", index=None)


if __name__ == "__main__":
    main()
    
