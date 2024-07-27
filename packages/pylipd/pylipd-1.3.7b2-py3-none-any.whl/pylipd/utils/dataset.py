#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 17:56:50 2023

@author: deborahkhider

Makes it easy to import some specific lpd files for testing and documentation purpose
"""

from pathlib import Path
import glob
from pylipd.lipd import LiPD

DATA_DIR = Path(__file__).parents[1].joinpath("data").resolve()
FOLDER_DIR = DATA_DIR.joinpath('Pages2k/')
#print(DATA_DIR)

def available_dataset_names():
    '''Helper function to easily see what datasets are available to load

    Returns
    -------
    names : list
        List of datasets available via the `load_dataset` method. 

    '''
    path_name = str(DATA_DIR)+'/*.lpd'
    files_unique = glob.glob(path_name)
    
    dir_name = str(FOLDER_DIR)+'/*.lpd'
    files_dir = (glob.glob(dir_name))
    
    files = files_unique + files_dir
    
    names = []
    for item in files:
        names.append(item.split('/')[-1].rsplit('.', 1)[0])
    
    return names


def load_datasets(names):
    
    if type(names) is not list:
        names = [names]
    
    path_name = str(DATA_DIR)+'/*.lpd'
    files_unique = glob.glob(path_name)
    dir_name = str(FOLDER_DIR)+'/*.lpd'
    files_dir = (glob.glob(dir_name)) 
    
    files = files_unique + files_dir
    
    full_paths = []
    for name in names:
       try:
           full_paths.append(list(filter(lambda a: name in a,files))[0])
       except:
           pass
    
    L = LiPD()
    print(full_paths)
    L.load(full_paths)
   
    return L

def load_dir(name = 'Pages2k'):
    
    if name!= 'Pages2k':
        raise ValueError("Option for folder is 'Pages2k")
    
    L = LiPD()
    L.load_from_dir(str(FOLDER_DIR))
    
    return L
