"""
===========
Design file
===========
Information of experimental designs
"""

import os.path as op
import pandas as pd
import numpy as np


utils_dir = op.join(op.dirname(__file__))

def get_designs():
    design_file = op.join(utils_dir, 'ASTexEEG_Exp01_stimuli.csv')
    return pd.read_csv(design_file)


n_exemplars = 15

conditions = (
    'original/big/animate', 'original/big/inanimate',
    'original/small/animate', 'original/small/inanimate'
)


# make a dictionary of trigger/id mapping or condition/id mapping
def get_event_id(map_type='condition'):

    designs = get_designs()
    stimuli_ids = designs['trigger']
    # check the number of stimuli
    assert(n_exemplars * len(conditions) == len(stimuli_ids))

    if map_type == 'trigger':
        stimuli_names = list(map(lambda x: f'Stimulus/S{x:3d}', stimuli_ids))

    elif map_type == 'condition':
        stimuli_conditions = designs['condition']
        stimuli_names = list(map(lambda x,y: f'{x}/object{y:03d}', stimuli_conditions, stimuli_ids))
        # check the conditions of stimuli
        assert(set(stimuli_conditions) == set(conditions))

    event_id = dict(zip(stimuli_names, stimuli_ids))
    return event_id


# ######################################################################### #

def make_blocks(base, n, reps=1):
    blocks = np.tile(np.repeat(np.repeat(base, n, 1), n, 0), (reps, reps))
    np.fill_diagonal(blocks, 0)
    return blocks


stim_type_blocks = dict(
    big=make_blocks(np.fliplr(np.eye(2, k=1)), 2*n_exemplars, 2),
    small=make_blocks(np.flipud(np.eye(2, k=1)), 2*n_exemplars, 2),
    animate=make_blocks(np.fliplr(np.eye(2, k=1)), n_exemplars, 4),
    inanimate=make_blocks(np.flipud(np.eye(2, k=1)), n_exemplars, 4),
    original=make_blocks(np.fliplr(np.eye(2, k=1)), 4*n_exemplars, 1),
    texform=make_blocks(np.flipud(np.eye(2, k=1)), 4*n_exemplars, 1),
)

category_blocks = dict(
    animacy=dict(
        between=make_blocks(np.fliplr(np.eye(2)), n_exemplars, 4),
        within=make_blocks(np.eye(2), n_exemplars, 4)
    ),
    size=dict(
        between=make_blocks(np.fliplr(np.eye(2)), 2*n_exemplars, 2),
        within=make_blocks(np.eye(2), 2*n_exemplars, 2)
    )
)


def get_between_within_index(stim_type, category):

    stim_types = stim_type.split(' ')
    stim_blocks = stim_type_blocks[stim_types[0]]

    if len(stim_types) == 2:
        stim_blocks = stim_blocks * stim_type_blocks[stim_types[1]]

    between_blocks = category_blocks[category]['between'] * stim_blocks
    within_blocks = category_blocks[category]['within'] * stim_blocks

    return between_blocks, within_blocks
