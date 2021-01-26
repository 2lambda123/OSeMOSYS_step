# main script to run the step function of OSeMOSYS
#%% Importe required packages
import os
import subprocess as sp
from otoole import ReadDatapackage
from otoole import WriteDatafile
from otoole import Context
import data_split
#%% Input
path_data = '../data/utopia.txt'
step_length = 5
#%% Convert datapackage to datafile
def dp_to_df(dp_path,step):
    # otoole datapackage to datafile
    reader = ReadDatapackage()
    writer = WriteDatafile()
    converter = Context(read_strategy=reader, write_strategy=writer)
    df_path = '../data/step%s.txt' % str(step)
    converter.convert(dp_path,df_path)
    return df_path
#%% Run model
def run_df():
    return results_path
#%% If run as script
if __name__ == '__main__':
    data_split.split_dp(path_data,step_length)
    df_step0 = dp_to_df('../data/datapackage0',0)
    # Run step 0
    sp.run(['glpsol -m ../model/osemosys.txt -d ../data/step0.txt'],shell=True)
# %%