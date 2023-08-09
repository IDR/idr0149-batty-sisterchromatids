import pandas
import re

experiment = "F"
anno_file = f"../experiment{experiment}/idr0149-experiment{experiment}-annotation.csv"
files_file = f"../experiment{experiment}/{experiment}.txt"
out_file = f"../experiment{experiment}/idr0149-experiment{experiment}-filePaths.tsv"
experiment_no = "ABCDEF".index(experiment)+1
base_dir = f"/uod/idr/filesets/idr0149-batty-sisterchromatids/20230605-ftp/experiment{experiment_no}"

def read_anno(file):
    images = {}
    df = pandas.read_csv(file, dtype=str)
    for _, row in df.iterrows():
        images[row["Image File"]] = row["Dataset Name"]
    return images

images = read_anno(anno_file)

with open(files_file) as f:
    with open(out_file, "w") as out:
        line = f.readline()
        while line:
            filename = re.sub("\n", "", line)
            filename = re.sub(".+/", "", filename)
            if filename in images:
                out.write(f"Dataset:name:{images[filename]}\t{base_dir}/{line}")
            else:
                print(f"ERR: {filename} not found!")
            line = f.readline()
