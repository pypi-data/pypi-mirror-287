#!/usr/bin/env python3

"""Module containing the Template class and the command line interface."""
from __future__ import print_function
import argparse
import pandas as pd
import numpy as np
import os
import csv
import shutil, glob
from pathlib import PurePath
from biobb_abaqus.abaqus.common import *
from tqdm import tqdm
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger

class Registration(BiobbObject):

    def __init__(self, fileIn, output_path, properties=None, **kwargs) -> None:

        properties = properties or {}

        # 2.0 Call parent class constructor
        super().__init__(properties)

        # 2.1 Modify to match constructor parameters
        # Input/Output files
        self.io_dict = { 
            'fileIn': {'fileIn': fileIn},
            'output_path': {'output_path': output_path}
        }
        self.files = self.io_dict['fileIn']['fileIn']
        self.properties = properties
        
        #args variables
        #self.fileIn = self.properties.get('fileIn')
        self.morph = self.properties.get('m', 5)
        self.WCEP = self.properties.get('w', 0)
        self.toINP = self.properties.get('i', 4)
        self.interpo = self.properties.get('y', 1)
        self.fusion = self.properties.get('f', 1)
        self.rigid = self.properties.get('r', 1)
        self.surfRegCEP = self.properties.get('c', 1)
        self.checkFElem = self.properties.get('e', 0)
        self.checkHaus = self.properties.get('d', 1)
        self.regCEP = self.properties.get('CEP', 0)
        print(self.properties)
    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`Template <template.template.Template>` object."""

        # 4. Setup Biobb
        if self.check_restart(): return 0
        self.stage_files()       

        self.run()

        return 0

    def run(self):
        pathSources = os.path.join(os.getcwd(), 'sources/')
        pathResults = os.path.join(os.getcwd(), 'results/')
        morph(self.io_dict["fileIn"]["fileIn"], pathSources, pathResults, self.morph, self.WCEP, self.toINP, self.interpo, self.fusion, self.rigid, self.surfRegCEP, self.checkFElem, self.checkHaus, self.regCEP)


def registration(fileIn: str, output_path: str, properties: dict = None, **kwargs) -> int:
    """Create :class:`Template <template.template.Template>` class and
    execute the :meth:`launch() <template.template.Template.launch>` method."""

    # return ParseHippie(properties=properties, **kwargs).launch()
    return Registration(fileIn, output_path, properties, **kwargs).launch()

def main():
    #argument administration
    parser = argparse.ArgumentParser(
        description='program that morphs a source IVD mesh to a target, the patient-specific model')
    parser.add_argument('--fileIn', help='info file that contains information about source and target',
                        type=str, default="./textToBcpd/IVD_L1L2_info_MY0001.txt")
    parser.add_argument(
        '-m', metavar='', help='Non-Rigid registration 1: AF; 2: NP; 3: NoBEP; 4: CEPmorph; 5: All; 0: NONE', type=int, default=5)
    parser.add_argument(
        '-i', metavar='', help='Create the .inp file of 1: AF; 2: NP; 3: NoBEP; 4: All; 0: NONE', type=int, default=4)
    parser.add_argument(
        '-e', metavar='', help='Check failed elements of the resulting .inp file? 1:YES; 2:Iterate value of lambda 0:NO', type=int, default=2)
    parser.add_argument(
        '-r', metavar='', help='Rigid registration at the begining of the process? 1: YES; 0: NO', type=int, default=1)
    parser.add_argument(
        '-w', metavar='', help='Morph with CEP? 1: YES; 0: NO', type=int, default=0)
    parser.add_argument(
        '-y', metavar='', help='Use interpolated files? 1: YES; 0: NO', type=int, default=1)
    parser.add_argument(
        '-f', metavar='', help='Fusion the AF and NP for the final morph? 1: YES; 0: NO', type=int, default=1)
    parser.add_argument(
        '-c', metavar='', help='Morphing the external surfaces of AF and NP (including CEP)? 1: YES; 0: NO', type=int, default=1)
    parser.add_argument(
        '-d', metavar='', help='Check Hausdorff distance between 3D grids (Euclidean distance)? 1: YES; 0: NO', type=int, default=1)
    parser.add_argument(
        '--CEP', metavar='', help='non-rigid registration of the CEP? 1: YES; 0: NO', type=int, default=0)
    parser.add_argument(
        '--output_path', metavar='', help='output path', type=str, default='/results')
    parser.add_argument(
        '--config', metavar='', help='config', type=str, default='workflow.yml')

    args = parser.parse_args()
    args.config = args.config or "{}"

    properties = settings.ConfReader(config=args.config).get_prop_dic()

    # 11. Adapt to match Class constructor (step 2)
    # Specific call of each building block
    registration(fileIn=args.fileIn, output_path=args.output_path, properties=properties)

    # start_registration(device, files)

if __name__ == '__main__':
    main()

# 12. Complete documentation strings
