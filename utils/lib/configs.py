"""
===========
Config file
===========
Configuration parameters for the study.
"""

import os
import os.path as op

# ---------------------------------------------------------- #
# set paths
if 'USER' in os.environ:
    user = os.environ['USER']
elif 'USERNAME' in os.environ:
    user = os.environ['USERNAME']

if user == 'Ruosi':
    study_path = '/Users/Ruosi/Dropbox/Research-ASTexEEG/EXPERIMENTS/Exp01'
    N_JOBS = 8
elif user == 'janini':
    study_path = '/Users/janini/Dropbox (KonkLab)/Research-ASTexEEG/EXPERIMENTS/Exp01'
    N_JOBS = 6
elif user == 'R':
    study_path = 'C:/Users/R/Dropbox/Research-ASTexEEG/EXPERIMENTS/Exp01'
    N_JOBS = 3

raw_dir = op.join(study_path, 'raw', 'EEG')           # raw Brainvision files
eeg_dir = op.join(study_path, 'eeg')                  # mne format .fif files
eeglab_dir = op.join(study_path, 'eeglab')            # eeglab preprocessed files
data_dir = op.join(study_path, 'analysis', 'data')    # .mat files
plots_dir = op.join(study_path, 'analysis', 'plots')  # plot files

bads_dir = op.join(study_path, 'scripts', 'preprocessing', 'bads')       # bach epochs and channels
lib_dir = op.join(study_path, 'scripts', 'preprocessing', 'library')     # library

if not op.isdir(eeg_dir):
    os.mkdir(eeg_dir)

if not op.isdir(data_dir):
    os.mkdir(data_dir)

if not op.isdir(plots_dir):
    os.mkdir(plots_dir)

# ---------------------------------------------------------- #
# subject names

subject_ids = (
    'ASTexEEG_Exp01Sub01', 'ASTexEEG_Exp01Sub02',
    'ASTexEEG_Exp01Sub03', 'ASTexEEG_Exp01Sub04',
    'ASTexEEG_Exp01Sub05', 'ASTexEEG_Exp01Sub06',
    'ASTexEEG_Exp01Sub07',
)

pilot_subject_ids = (
    'ASTexEEG_Pilot04Sub01',
    'ASTexEEG_Pilot04Sub02'
)

# ---------------------------------------------------------- #
# preprocessing information

tmin, tmax = -.1, .9              # epoch
n_epochs = 2880                   # number of epochs
eog = {'HEOG', 'FP1', 'FP2'}      # EOG channels
decim = 1                         # rate to downsample the data

RANDOM_STATE = 314
