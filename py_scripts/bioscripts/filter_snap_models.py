#!/usr/bin/python3

def filter_snap_models(models_in_path, snap_validate_path, models_out_path):
    with open(models_in_path, "r") as models_in_file, open(snap_validate_path,"r") as snap_validate_file, open(models_out_path,"w") as models_out_file:
        models_ok = []
        for line in snap_validate_file:
            line_split = line.rstrip().split(" ")
            if len(line_split) == 3 and line_split[-1] == "OK":
                model = line_split[1]
                models_ok.append(model)
        for line in models_in_file:
            if line[0] == ">" :
                models_out_file.write(line)
            else:
                model_name = line.rstrip().split(" ")[-1]
                if model_name in models_ok:
                    models_out_file.write(line)

    return 0

models_in_path = "/Users/annanenarokova/work/hypsa_local/jana_m/genome.ann"
snap_validate_path = "/Users/annanenarokova/work/hypsa_local/jana_m/snap_validate_output.txt"
models_out_path = "/Users/annanenarokova/work/hypsa_local/jana_m/genome_models_ok_new.ann"

filter_snap_models(models_in_path, snap_validate_path, models_out_path)