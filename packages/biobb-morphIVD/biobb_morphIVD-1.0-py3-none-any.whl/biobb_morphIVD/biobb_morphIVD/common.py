#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
 ___  ___  ________     ___    ___ ___  ___  ________     ___    ___ ___    ___  _______  ________
|\  \|\  \|\   __  \   |\  \  /  /|\  \|\  \|\   __  \   |\  \  /  /|\  \  /  /|/  ___  \|\_____  \
\ \  \\\  \ \  \|\  \  \ \  \/  / | \  \\\  \ \  \|\  \  \ \  \/  / | \  \/  / /__/|_/  /\|____|\ /_
 \ \   __  \ \   __  \  \ \    / / \ \   __  \ \   __  \  \ \    / / \ \    / /|__|//  / /     \|\  \
  \ \  \ \  \ \  \ \  \  /     \/   \ \  \ \  \ \  \ \  \  /     \/   /     \/     /  /_/__   __\_\  \
   \ \__\ \__\ \__\ \__\/  /\   \    \ \__\ \__\ \__\ \__\/  /\   \  /  /\   \    |\________\|\_______\
    \|__|\|__|\|__|\|__/__/ /\ __\    \|__|\|__|\|__|\|__/__/ /\ __\/__/ /\ __\    \|_______|\|_______|
                       |__|/ \|__|                       |__|/ \|__||__|/ \|__|


"""

#***************************************************************
#******    Functions used in the main program morph.py    ******
#******    auth: Estefano Muñoz-Moya                      ******
#******    webPage: https://estefano23.github.io/         ******
#******    github: estefano23                             ******
#******    email: estefano.munoz.moya@gmail.com           ******
#***************************************************************


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# introduction
# ------------

#libraries
from __future__ import print_function
import os
import csv
import subprocess
import numpy as np
import math
from statistics import *
###
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------


def morph(fileIn, pathSources, pathResults, morph, WCEP, toINP, interpo, fusion, rigid, surfRegCEP, checkFElem, checkHaus, regCEP):
    # define file name, path, disc, and patient id
    pathFile = os.path.dirname(fileIn)  # file directory
    baseName = os.path.basename(fileIn)  # file basename
    baseNameWE = os.path.splitext(baseName)[0]  # file basename with extention

    # disc information
    numberIVD = baseName.split('_')[1]  # disc numer
    patient = baseName.split('_')[3].split('.')[0]  # patient id

    # container folder
    # source folder: template mesh point cloud
    pathTemplate = pathSources + 'template'
    pathNodes = pathTemplate + "/" + "nodes"
    pathTarget = 'textToBcpd'  # target folder: patient-specific point cloud
    pathOutToInp = "toInp"  # temp folder: temporal files to create input files
    # .inp folder: folder that contains the .inp final files
    pathInp = pathResults + 'inputs'
    # .inp parts folder: folder that contains AF and NP .inp files
    pathParts = pathInp + "/parts"
    # .inp complete folder: folder that contains the complete patient-specific .inp models
    pathCompleted = pathInp + "/complete"

    # to print in terminal
    # program presentation with argparse selection

    print("")
    print("")
    print("                              Morphing for IVD")
    print("                              ----------------")
    print("")
    print("Reading the file: " + fileIn)
    print("Disc: " + numberIVD)
    print("Patient: " + patient)
    if interpo == 0:
        print("Interpolated values?: NO")
    elif interpo == 1:
        print("Interpolated values?: YES")
    if rigid == 0:
        print("Rigid registration?: NO")
    elif rigid == 1:
        print("Rigid registration?: YES")
    if fusion == 0:
        print("Fusion the morphed AF and NP?: NO")
    elif fusion == 1:
        print("Fusion the morphed AF and NP?: YES")
    if WCEP == 0:
        print("Morph with CEP?: NO")
    elif WCEP == 1:
        print("Morph with CEP?: YES")
    if surfRegCEP == 1:
        print("Morphing the external surfaces of AF and NP (including CEP)?: YES")
    elif surfRegCEP == 0:
        print("Morphing the external surfaces of AF and NP (including CEP)?: NO")
    if checkFElem == 1:
        print("Check failed elements of the resulting .inp file?: YES")
    elif checkFElem == 0:
        print("Check failed elements of the resulting .inp file?: NO")
    if regCEP == 1:
        print("non-rigid registration of the CEP?: YES")
    elif regCEP == 0:
        print("non-rigid registration of the CEP?: NO")
    print(" ")

    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # necessary files

    # point cloud file with the nodes in the external surface of AF and NP
    fileTargetAF = "IVD_" + numberIVD + "_nodesOnSurface_AF_" + patient + ".txt"
    fileTargetNP = "IVD_" + numberIVD + "_nodesOnSurface_NP_" + patient + ".txt"
    if regCEP == 1:
        fileTargetCEPupper = "IVD_" + numberIVD + \
            "_nodesOnSurface_CEPupper_" + patient + ".txt"
        fileTargetCEPlower = "IVD_" + numberIVD + \
            "_nodesOnSurface_CEPlower_" + patient + ".txt"

        fileTargetCEPupper_up = "IVD_" + numberIVD + \
            "_nodesOnSurface_CEPupper_up_" + patient + ".txt"
        fileTargetCEPupper_down = "IVD_" + numberIVD + \
            "_nodesOnSurface_CEPupper_down_" + patient + ".txt"

        fileTargetCEPlower_up = "IVD_" + numberIVD + \
            "_nodesOnSurface_CEPlower_up_" + patient + ".txt"
        fileTargetCEPlower_down = "IVD_" + numberIVD + \
            "_nodesOnSurface_CEPlower_down_" + patient + ".txt"

    # rigid registration (if -r is selected)
    # file with AF and NP in one file
    fileToRigid = "IVD_" + numberIVD + "_nodesOnSurface_toRigid_" + patient + ".txt"
    # files with AF and NP after rigid registration
    fileTemplateAFRigid = "template_AFRigid_" + numberIVD + "_" + patient + ".txt"
    fileTemplateNPRigid = "template_NPRigid_" + numberIVD + "_" + patient + ".txt"
    if regCEP == 1:
        fileTemplateCEPupperRigid = "template_CEPupperRigid_" + \
            numberIVD + "_" + patient + ".txt"
        fileTemplateCEPupperUpRigid = "template_CEPupperUpRigid_" + \
            numberIVD + "_" + patient + ".txt"
        fileTemplateCEPupperDownRigid = "template_CEPupperDownRigid_" + \
            numberIVD + "_" + patient + ".txt"

        fileTemplateCEPlowerRigid = "template_CEPlowerRigid_" + \
            numberIVD + "_" + patient + ".txt"
        fileTemplateCEPlowerUpRigid = "template_CEPlowerUpRigid_" + \
            numberIVD + "_" + patient + ".txt"
        fileTemplateCEPlowerDownRigid = "template_CEPlowerDownRigid_" + \
            numberIVD + "_" + patient + ".txt"

    # non-rigid registration
    # point cloud file with the nodes of the complete mesh after the non-rigid (morphed) registration of AF and NP
    outPutFileMorphedAF = 'Morphed_AF_' + numberIVD + '_' + patient + '.inp'
    outPutFileMorphedNP = 'Morphed_NP_' + numberIVD + '_' + patient + '.inp'
    outPutFileMorphedIVD = 'Morphed_IVD_' + numberIVD + '_' + patient + '.inp'
    # output file that contains the number of failed elements and the lambda value
    outPutFileFailedElem = 'Morphed_IVD_' + numberIVD + '_' + patient + '_FE.csv'
    # output file that contains the euclidean distance of the morphed file
    outPutFileEuclidean = 'Morphed_IVD_' + numberIVD + '_' + patient + '_EU.csv'
    ### exception: if the rigid registration (-r) option is selected, a new temporal file is created
    outPutFileMorphedRigid = 'MorphedRigid_' + numberIVD + '_' + patient + '_'
    # output temporal files of AF, NP, and the entire disc after the non-rigid registration
    outPutFileNodesOnSurfaceAFwoNodesCEP = 'nodesOnSurfaceAFwoNodesCEP_' + \
        numberIVD + '_' + patient + '_'
    outPutFileNodesOnSurfaceNPwoNodesCEP = 'nodesOnSurfaceNPwoNodesCEP_' + \
        numberIVD + '_' + patient + '_'
    outPutFileNodesOnSurfaceAFwNodesCEP = 'nodesOnSurfaceAFwNodesCEP_' + \
        numberIVD + '_' + patient + '_'
    outPutFileNodesOnSurfaceNPwNodesCEP = 'nodesOnSurfaceNPwNodesCEP_' + \
        numberIVD + '_' + patient + '_'
    outPutFileNodesOnSurfaceCEPupper = 'nodesOnSurfaceCEPupper_' + \
        numberIVD + '_' + patient + '_'
    outPutFileNodesOnSurfaceCEPupperUp = 'nodesOnSurfaceCEPupper_up_' + \
        numberIVD + '_' + patient + '_'
    outPutFileNodesOnSurfaceCEPupperDown = 'nodesOnSurfaceCEPupper_down_' + \
        numberIVD + '_' + patient + '_'
    outPutFileNodesOnSurfaceCEPlower = 'nodesOnSurfaceCEPlower_' + \
        numberIVD + '_' + patient + '_'
    outPutFileNodesOnSurfaceCEPlowerUp = 'nodesOnSurfaceCEPlower_up_' + \
        numberIVD + '_' + patient + '_'
    outPutFileNodesOnSurfaceCEPlowerDown = 'nodesOnSurfaceCEPlower_down_' + \
        numberIVD + '_' + patient + '_'

    # output temporal files of AF, NP, and the entire disc after the non-rigid registration
    outPutFileAF = 'AF_' + numberIVD + '_' + patient + '_'
    outPutFileNP = 'NP_' + numberIVD + '_' + patient + '_'
    outPutFileMorphed = 'Morphed_' + numberIVD + '_' + patient + '_'
    # file name of the temporal merged file of the morphed AF and NP
    fileMorphed = "mergedMorphed_IVD_" + numberIVD + "_" + patient + ".txt"
    # file name of the temporal nodesOnSurface file of the morphed AF and NP
    fileNodesOnSurfaceAF = "nodesOnSurface_AF_" + numberIVD + "_" + patient + ".txt"
    fileNodesOnSurfaceNP = "nodesOnSurface_NP_" + numberIVD + "_" + patient + ".txt"
    fileNodesOnSurfaceMorphed = "nodesOnSurface_Morphed_" + \
        numberIVD + "_" + patient + ".txt"

    # template .txt (coordinates) and .inp (ABAQUS) files of AF and NP to put the new nodes coordinates
    ### exception: if the CEP (-w) option is selected, the "with CEP" (WCEP) templated is used
    if WCEP == 1:
        fileTemplateAF = "template_AF_WCEP.txt"
        templateInpAF = "template_AF_WCEP.inp"
        fileTemplateNP = "template_NP_WCEP.txt"
        templateInpNP = "template_NP_WCEP.inp"
    if (WCEP == 0 or surfRegCEP == 1):
        fileTemplateAF = "template_AF.txt"
        templateInpAF = "template_AF.inp"
        fileTemplateNP = "template_NP.txt"
        templateInpNP = "template_NP.inp"
        
    if regCEP == 1:
        # template .txt (coordinates) and .inp (ABAQUS) files of CEP to put the new nodes coordinates
        fileTemplateCEPupper = "template_CEPupper.txt"
        templateInpCEPupper = "template_CEPupper.inp"
        fileTemplateCEPupper_up = "template_CEPupper_up.txt"
        fileTemplateCEPupper_down = "template_CEPupper_down.txt"

        fileTemplateCEPlower = "template_CEPlower.txt"
        templateInpCEPlower = "template_CEPlower.inp"
        fileTemplateCEPlower_up = "template_CEPlower_up.txt"
        fileTemplateCEPlower_down = "template_CEPlower_down.txt"

    # template .txt (coordinates with no index number) and .inp (ABAQUS) files of the entire disc to put the new nodes coordinates
    fileTemplateNoBEP = "L4-L5_noBEP_noIndex.txt"
    templateInpMorphed = "template_L4-L5_noBEP.inp"
    pathInpTemplateAF = "./" + pathTemplate + "/" + templateInpAF
    pathInpTemplateNP = "./" + pathTemplate + "/" + templateInpNP
    pathInpTemplateMorphed = "./" + pathTemplate + "/" + templateInpMorphed

    ###exception: if interpolated registration is selected (-y), the ..._y.interpolated.txt is used
    if interpo == 0:
        outPutFileNodesOnSurfaceAFwoNodesCEPE = outPutFileNodesOnSurfaceAFwoNodesCEP + "y.txt"
        outPutFileNodesOnSurfaceNPwoNodesCEPE = outPutFileNodesOnSurfaceNPwoNodesCEP + "y.txt"
        outPutFileNodesOnSurfaceAFwNodesCEPE = outPutFileNodesOnSurfaceAFwNodesCEP + "y.txt"
        outPutFileNodesOnSurfaceNPwNodesCEPE = outPutFileNodesOnSurfaceNPwNodesCEP + "y.txt"
        outPutFileMorphedRigidE = outPutFileMorphedRigid + "y.txt"
        outPutFileAFE = outPutFileAF + "y.txt"
        outPutFileNPE = outPutFileNP + "y.txt"
        outPutFileMorphedE = outPutFileMorphed + "y.txt"
        outPutFileNodesOnSurfaceCEPupperE = outPutFileNodesOnSurfaceCEPupper + "y.txt"
        outPutFileNodesOnSurfaceCEPupperUpE = outPutFileNodesOnSurfaceCEPupperUp + "y.txt"
        outPutFileNodesOnSurfaceCEPupperDownE = outPutFileNodesOnSurfaceCEPupperDown + "y.txt"
        outPutFileNodesOnSurfaceCEPlowerE = outPutFileNodesOnSurfaceCEPlower + "y.txt"
        outPutFileNodesOnSurfaceCEPlowerUPE = outPutFileNodesOnSurfaceCEPlowerUp + "y.txt"
        outPutFileNodesOnSurfaceCEPlowerDownE = outPutFileNodesOnSurfaceCEPlowerDown + "y.txt"
    elif interpo == 1:
        outPutFileNodesOnSurfaceAFwoNodesCEPE = outPutFileNodesOnSurfaceAFwoNodesCEP + \
            "y.interpolated.txt"
        outPutFileNodesOnSurfaceNPwoNodesCEPE = outPutFileNodesOnSurfaceNPwoNodesCEP + \
            "y.interpolated.txt"
        outPutFileNodesOnSurfaceAFwNodesCEPE = outPutFileNodesOnSurfaceAFwNodesCEP + \
            "y.interpolated.txt"
        outPutFileNodesOnSurfaceNPwNodesCEPE = outPutFileNodesOnSurfaceNPwNodesCEP + \
            "y.interpolated.txt"
        outPutFileMorphedRigidE = outPutFileMorphedRigid + "y.interpolated.txt"
        outPutFileAFE = outPutFileAF + "y.interpolated.txt"
        outPutFileNPE = outPutFileNP + "y.interpolated.txt"
        outPutFileMorphedE = outPutFileMorphed + "y.interpolated.txt"
        outPutFileNodesOnSurfaceCEPupperE = outPutFileNodesOnSurfaceCEPupper + "y.interpolated.txt"
        outPutFileNodesOnSurfaceCEPupperUpE = outPutFileNodesOnSurfaceCEPupperUp + \
            "y.interpolated.txt"
        outPutFileNodesOnSurfaceCEPupperDownE = outPutFileNodesOnSurfaceCEPupperDown + \
            "y.interpolated.txt"
        outPutFileNodesOnSurfaceCEPlowerE = outPutFileNodesOnSurfaceCEPlower + "y.interpolated.txt"
        outPutFileNodesOnSurfaceCEPlowerUpE = outPutFileNodesOnSurfaceCEPlowerUp + \
            "y.interpolated.txt"
        outPutFileNodesOnSurfaceCEPlowerDownE = outPutFileNodesOnSurfaceCEPlowerDown + \
            "y.interpolated.txt"

    # list of information about the node coordinates
    # dictionary | total nodes and coordiantes of the source: template mesh
    nodeTotTemplate = dict()
    nodeNoBEPTemplate = list()  # list | total nodes of the source: template disc mesh

    # complete template: reading all nodes without coordinates
    with open(pathTemplate + '/L4-L5_noBEP.txt', 'r') as a:
        reader_a = csv.reader(a)
        for row in reader_a:
            nodeNoBEPTemplate.append(int(row[0]))

    # reading the nodes (without coordinates) of AF, TZ, and NP
    # list | total nodes of the AF source: template AF mesh
    nodesTemplateNumberAF = list()
    # list | total nodes of the NP source: template NP mesh
    nodesTemplateNumberNP = list()
    # list | total nodes of the TZ source: template TZ mesh
    nodeTransitionTemplate = list()

    # with CEP
    nodesAFwCEP = list()
    nodesNPwCEP = list()
    nodesOnSurfaceAFwCEP = list()
    nodesOnSurfaceNPwCEP = list()
    nodesOnSurfaceTZwCEP = list()

    with open(pathNodes + "/" + "nodesAFwCEP.txt", 'r') as f:
        for row in f:
            nodesAFwCEP.append(int(row))
    with open(pathNodes + "/" + "nodesNPwCEP.txt", 'r') as f:
        for row in f:
            nodesNPwCEP.append(int(row))
    with open(pathNodes + "/" + "nodesOnSurfaceAFwCEP.txt", 'r') as f:
        for row in f:
            nodesOnSurfaceAFwCEP.append(int(row))
    with open(pathNodes + "/" + "nodesOnSurfaceNPwCEP.txt", 'r') as f:
        for row in f:
            nodesOnSurfaceNPwCEP.append(int(row))
    with open(pathNodes + "/" + "nodesOnSurfaceTZwCEP.txt", 'r') as f:
        for row in f:
            nodesOnSurfaceTZwCEP.append(int(row))


    # without CEP
    nodesAFwoCEP = list()
    nodesNPwoCEP = list()
    nodesOnSurfaceAFwoCEP = list()
    nodesOnSurfaceNPwoCEP = list()
    nodesOnSurfaceTZwoCEP = list()

    with open(pathNodes + "/" + "nodesAFwoCEP.txt", 'r') as f:
        for row in f:
            nodesAFwoCEP.append(int(row))
    with open(pathNodes + "/" + "nodesNPwoCEP.txt", 'r') as f:
        for row in f:
            nodesNPwoCEP.append(int(row))
    with open(pathNodes + "/" + "nodesOnSurfaceAFwoCEP.txt", 'r') as f:
        for row in f:
            nodesOnSurfaceAFwoCEP.append(int(row))
    with open(pathNodes + "/" + "nodesOnSurfaceNPwoCEP.txt", 'r') as f:
        for row in f:
            nodesOnSurfaceNPwoCEP.append(int(row))
    with open(pathNodes + "/" + "nodesOnSurfaceTZwoCEP.txt", 'r') as f:
        for row in f:
            nodesOnSurfaceTZwoCEP.append(int(row))

    nodesAFwoCEP.sort()
    nodesNPwoCEP.sort()
    nodesOnSurfaceAFwoCEP.sort()
    nodesOnSurfaceNPwoCEP.sort()
    nodesOnSurfaceTZwoCEP.sort()

    # CEP
    if regCEP == 1:
        nodesOnSurfaceCEPupper = list()
        nodesOnSurfaceCEPlower = list()

        with open(pathNodes + "/" + "nodesOnSurfaceCEPupper.txt", 'r') as f:
            for row in f:
                nodesOnSurfaceCEPupper.append(int(row))

        with open(pathNodes + "/" + "nodesOnSurfaceCEPlower.txt", 'r') as f:
            for row in f:
                nodesOnSurfaceCEPlower.append(int(row))

    # defining the nodes to morph
    if WCEP == 1:
        nodesTemplateNumberAF = nodesAFwCEP.copy()
        nodesTemplateNumberNP = nodesNPwCEP.copy()
        nodeTransitionTemplate = nodesOnSurfaceTZwCEP.copy()
    if (WCEP == 0 or surfRegCEP == 1):
        nodesTemplateNumberAF = nodesAFwoCEP.copy()
        nodesTemplateNumberNP = nodesNPwoCEP.copy()
        nodeTransitionTemplate = nodesOnSurfaceTZwoCEP.copy()

    tempCoordTemplate = list()
    for node in nodeTransitionTemplate:
        tempCoordTemplate.append(node)
        nodesTemplateNumberAF.remove(node)

    nodesTemplateNumberAF += tempCoordTemplate

    # reading nodes of the CEP
    nodesCEPupper = list()
    nodesCEPupper_up = list()
    nodesCEPupper_down = list()
    nodesCEPlower = list()
    nodesCEPlower_up = list()
    nodesCEPlower_down = list()
    nodesCEPlower_middle = list()
    nodesOnSurfaceAFCEPUpper = list()
    nodesOnSurfaceAFCEPLower = list()
    nodesOnSurfaceNPCEPUpper = list()
    nodesOnSurfaceNPCEPLower = list()
    nodesOnSurfaceAFMiddle = list()
    nodesOnSurfaceAFMiddleUpper = list()
    nodesOnSurfaceAFMiddleLower = list()
    nodesOnSurfaceNPMiddle = list()
    nodesOnSurfaceNPMiddleUpper = list()
    nodesOnSurfaceNPMiddleLower = list()
    nodesOnSurfaceIVDColumn = list()

    with open(pathNodes + "/" + "nodesCEPupper.txt", 'r') as f:
        for row in f:
            nodesCEPupper.append(int(row))

    with open(pathNodes + "/" + "nodesCEPupper_up.txt", 'r') as f:
        for row in f:
            nodesCEPupper_up.append(int(row))

    with open(pathNodes + "/" + "nodesCEPupper_down.txt", 'r') as f:
        for row in f:
            nodesCEPupper_down.append(int(row))

    with open(pathNodes + "/" + "nodesCEPlower.txt", 'r') as f:
        for row in f:
            nodesCEPlower.append(int(row))

    with open(pathNodes + "/" + "nodesCEPlower_up.txt", 'r') as f:
        for row in f:
            nodesCEPlower_up.append(int(row))

    with open(pathNodes + "/" + "nodesCEPlower_down.txt", 'r') as f:
        for row in f:
            nodesCEPlower_down.append(int(row))

    with open(pathNodes + "/" + "nodesOnSurfaceAFCEPUpper.txt", 'r') as f:
        for row in f:
            nodesOnSurfaceAFCEPUpper.append(int(row))

    with open(pathNodes + "/" + "nodesOnSurfaceAFCEPLower.txt", 'r') as f:
        for row in f:
            nodesOnSurfaceAFCEPLower.append(int(row))

    with open(pathNodes + "/" + "nodesOnSurfaceNPCEPUpper.txt", 'r') as f:
        for row in f:
            nodesOnSurfaceNPCEPUpper.append(int(row))

    with open(pathNodes + "/" + "nodesOnSurfaceNPCEPLower.txt", 'r') as f:
        for row in f:
            nodesOnSurfaceNPCEPLower.append(int(row))

    with open(pathNodes + "/" + "nodesOnSurfaceAFMiddle.txt", 'r') as f:
        for row in f:
            nodesOnSurfaceAFMiddle.append(int(row))

    with open(pathNodes + "/" + "nodesOnSurfaceAFMiddleUpper.txt", 'r') as f:
        for row in f:
            nodesOnSurfaceAFMiddleUpper.append(int(row))

    with open(pathNodes + "/" + "nodesOnSurfaceAFMiddleLower.txt", 'r') as f:
        for row in f:
            nodesOnSurfaceAFMiddleLower.append(int(row))

    with open(pathNodes + "/" + "nodesOnSurfaceNPMiddle.txt", 'r') as f:
        for row in f:
            nodesOnSurfaceNPMiddle.append(int(row))

    with open(pathNodes + "/" + "nodesOnSurfaceNPMiddleUpper.txt", 'r') as f:
        for row in f:
            nodesOnSurfaceNPMiddleUpper.append(int(row))

    with open(pathNodes + "/" + "nodesOnSurfaceNPMiddleLower.txt", 'r') as f:
        for row in f:
            nodesOnSurfaceNPMiddleLower.append(int(row))

    with open(pathNodes + "/" + "nodesOnSurfaceIVDColumn.txt", 'r') as f:
        for row in f:
            nodesOnSurfaceIVDColumn.append(int(row))

    nodesCEPupper.sort()
    nodesCEPupper_up.sort()
    nodesCEPupper_down.sort()
    nodesCEPlower.sort()
    nodesCEPlower_up.sort()
    nodesCEPlower_down.sort()
    nodesOnSurfaceAFCEPUpper.sort()
    nodesOnSurfaceAFCEPLower.sort()
    nodesOnSurfaceNPCEPUpper.sort()
    nodesOnSurfaceNPCEPLower.sort()
    nodesOnSurfaceAFMiddle.sort()
    nodesOnSurfaceAFMiddleUpper.sort()
    nodesOnSurfaceAFMiddleLower.sort()
    nodesOnSurfaceNPMiddle.sort()
    nodesOnSurfaceNPMiddleUpper.sort()
    nodesOnSurfaceNPMiddleLower.sort()
    nodesOnSurfaceIVDColumn.sort()


    #creating the nodes that are in TZ and CEP
    nodesOnSurfaceTZdiffwCEP = nodesOnSurfaceTZwCEP.copy()
    for node in nodesOnSurfaceTZwoCEP:
        nodesOnSurfaceTZdiffwCEP.remove(node)

    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # node number
    # defining how many nodes are in the rigid, AF, NP, and morphed
    line_count_rigid = 0
    line_count_AF = 0
    line_count_NP = 0
    line_count_CEPupper = 0
    line_count_CEPupperUp = 0
    line_count_CEPupperDown = 0
    line_count_CEPlower = 0
    line_count_CEPlowerUp = 0
    line_count_CEPlowerDown = 0

    file = open(pathTarget + "/" + fileToRigid, "r")
    for line in file:
        if line != "\n":
            line_count_rigid += 1
    file.close()


    file = open(pathTarget + "/" + fileTargetAF, "r")
    for line in file:
        if line != "\n":
            line_count_AF += 1
    file.close()

    file = open(pathTarget + "/" + fileTargetNP, "r")
    for line in file:
        if line != "\n":
            line_count_NP += 1
    file.close()

    if regCEP == 1:
        file = open(pathTarget + "/" + fileTargetCEPupper, "r")
        for line in file:
            if line != "\n":
                line_count_CEPupper += 1
        file.close()
        file = open(pathTarget + "/" + fileTargetCEPupper_up, "r")
        for line in file:
            if line != "\n":
                line_count_CEPupperUp += 1
        file.close()
        file = open(pathTarget + "/" + fileTargetCEPupper_down, "r")
        for line in file:
            if line != "\n":
                line_count_CEPupperDown += 1
        file.close()

        file = open(pathTarget + "/" + fileTargetCEPlower, "r")
        for line in file:
            if line != "\n":
                line_count_CEPlower += 1
        file.close()
        file = open(pathTarget + "/" + fileTargetCEPlower_up, "r")
        for line in file:
            if line != "\n":
                line_count_CEPlowerUp += 1
        file.close()
        file = open(pathTarget + "/" + fileTargetCEPlower_down, "r")
        for line in file:
            if line != "\n":
                line_count_CEPlowerDown += 1
        file.close()

    # obtaining the centroid of the NP
    IVDPSCoord = np.empty((0, 3), int)
    AFPSCoord = np.empty((0, 3), int)
    NPPSCoord = np.empty((0, 3), int)

    with open(pathTarget + "/" + fileToRigid, 'r') as fp:
        reader_f = csv.reader(fp, delimiter=',')
        for line in reader_f:
            tempCoord = [float(line[0]), float(line[1]), float(line[2])]
            IVDPSCoord = np.append(
                IVDPSCoord, np.array([tempCoord]), axis=0)

    with open(pathTarget + "/" + fileTargetAF, 'r') as fp:
        reader_f = csv.reader(fp, delimiter=',')
        for line in reader_f:
            tempCoord = [float(line[0]), float(line[1]), float(line[2])]
            AFPSCoord = np.append(
                AFPSCoord, np.array([tempCoord]), axis=0)

    with open(pathTarget + "/" + fileTargetNP, 'r') as fp:
        reader_f = csv.reader(fp, delimiter=',')
        for line in reader_f:
            tempCoord = [float(line[0]), float(line[1]), float(line[2])]
            NPPSCoord = np.append(
                NPPSCoord, np.array([tempCoord]), axis=0)

    if regCEP == 1:
        CEPupperPSCoord = np.empty((0, 3), int)
        CEPlowerPSCoord = np.empty((0, 3), int)

        with open(pathTarget + "/" + fileTargetCEPupper, 'r') as fp:
            reader_f = csv.reader(fp, delimiter=',')
            for line in reader_f:
                tempCoord = [float(line[0]), float(line[1]), float(line[2])]
                CEPupperPSCoord = np.append(
                    CEPupperPSCoord, np.array([tempCoord]), axis=0)

        with open(pathTarget + "/" + fileTargetCEPlower, 'r') as fp:
            reader_f = csv.reader(fp, delimiter=',')
            for line in reader_f:
                tempCoord = [float(line[0]), float(line[1]), float(line[2])]
                CEPlowerPSCoord = np.append(
                    CEPlowerPSCoord, np.array([tempCoord]), axis=0)

    # obtaining the centroid of NP PS model
    centroidNPPS = np.mean(NPPSCoord, axis=0)

    # take the centroid and move it to the (0,0,0) coordinates, and translate the other nodes
    # to the new coordinates

    for i in range(0, len(IVDPSCoord)):
        IVDPSCoord[i] = IVDPSCoord[i] - centroidNPPS

    for i in range(0, len(AFPSCoord)):
        AFPSCoord[i] = AFPSCoord[i] - centroidNPPS

    for i in range(0, len(NPPSCoord)):
        NPPSCoord[i] = NPPSCoord[i] - centroidNPPS

    if regCEP == 1:
        for i in range(0, len(CEPupperPSCoord)):
            CEPupperPSCoord[i] = CEPupperPSCoord[i] - centroidNPPS

        for i in range(0, len(CEPlowerPSCoord)):
            CEPlowerPSCoord[i] = CEPlowerPSCoord[i] - centroidNPPS

    # write the new coordinates in a file in the same path as the old one
    fileToRigid = "IVD_" + numberIVD + \
        "_nodesOnSurface_toRigid_" + patient + "_newCoords.txt"
    fileTargetAF = "IVD_" + numberIVD + \
        "_nodesOnSurface_AF_" + patient + "_newCoords.txt"
    fileTargetNP = "IVD_" + numberIVD + \
        "_nodesOnSurface_NP_" + patient + "_newCoords.txt"


    with open(pathTarget + "/" + fileToRigid, 'w') as fp:
        writer_f = csv.writer(fp, delimiter=',')
        for i in range(0, len(IVDPSCoord)):
            writer_f.writerow(IVDPSCoord[i])

    with open(pathTarget + "/" + fileTargetAF, 'w') as fp:
        writer_f = csv.writer(fp, delimiter=',')
        for i in range(0, len(AFPSCoord)):
            writer_f.writerow(AFPSCoord[i])

    with open(pathTarget + "/" + fileTargetNP, 'w') as fp:
        writer_f = csv.writer(fp, delimiter=',')
        for i in range(0, len(NPPSCoord)):
            writer_f.writerow(NPPSCoord[i])

    if regCEP == 1:
        fileTargetCEPupper = "IVD_" + numberIVD + \
            "_nodesOnSurface_CEPupper_" + patient + "_newCoords.txt"
        fileTargetCEPlower = "IVD_" + numberIVD + \
            "_nodesOnSurface_CEPlower_" + patient + "_newCoords.txt"

        with open(pathTarget + "/" + fileTargetCEPupper, 'w') as fp:
            writer_f = csv.writer(fp, delimiter=',')
            for i in range(0, len(CEPupperPSCoord)):
                writer_f.writerow(CEPupperPSCoord[i])

        with open(pathTarget + "/" + fileTargetCEPlower, 'w') as fp:
            writer_f = csv.writer(fp, delimiter=',')
            for i in range(0, len(CEPlowerPSCoord)):
                writer_f.writerow(CEPlowerPSCoord[i])

    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # rigid registration

    # define the string format to write the rigid registration temporal file
    string = '{:.8f}\t{:.8f}\t{:.8f}'
    string += '\n'

    # exception: if rigid registration is selected (-r)
    if (rigid == 1 and (morph == 1 or morph == 5)):
        #define bcpd function
        # defFuncRigid(targetFile, sourceFile, outPutFileName, nLoops, lenTarget, lenSource)

        funcRigidMorphed = defFuncRigid(pathTarget + "/" + fileToRigid, pathTemplate + "/" +
                                        fileTemplateNoBEP, outPutFileMorphedRigid, 1000, line_count_rigid, len(nodeNoBEPTemplate))

        #excecute rigid registration
        #defRigid(nameMorph, numberIVD, patientID, funcRigid, outPutFileName, pathOut)

        defRigid("Entire Disc", numberIVD, patient, funcRigidMorphed,
                outPutFileMorphedRigid, pathOutToInp)

    if rigid == 1:
        # saving the total nodes with the new coordinates after rigid registration
        with open(pathOutToInp + "/" + outPutFileMorphedRigidE, 'r') as f:
            reader_f = csv.reader(f, delimiter='\t')
            count = 0
            #as the nodes are in the same order, the total nodes is reading using a counter
            for rowf in reader_f:
                nodeTotTemplate[nodeNoBEPTemplate[count]] = rowf
                count += 1

        # the nodes are transfomed from string to float
        for key, value in nodeTotTemplate.items():
            nodeTotTemplate[key] = [
                float(value[0]), float(value[1]), float(value[2])]

        # temporal files of new template nodes are written (AF and NP)
        with open(pathOutToInp + "/" + fileTemplateAFRigid, 'w') as mor:
            for inode in nodesTemplateNumberAF:
                mor.write(string.format(*nodeTotTemplate[inode]))
        with open(pathOutToInp + "/" + fileTemplateNPRigid, 'w') as mor:
            for inode in nodesTemplateNumberNP:
                mor.write(string.format(*nodeTotTemplate[inode]))
        if regCEP == 1:
            with open(pathOutToInp + "/" + fileTemplateCEPupperRigid, 'w') as mor:
                for inode in nodesCEPupper:
                    mor.write(string.format(*nodeTotTemplate[inode]))
            with open(pathOutToInp + "/" + fileTemplateCEPupperUpRigid, 'w') as mor:
                for inode in nodesCEPupper_up:
                    mor.write(string.format(*nodeTotTemplate[inode]))
            with open(pathOutToInp + "/" + fileTemplateCEPupperDownRigid, 'w') as mor:
                for inode in nodesCEPupper_down:
                    mor.write(string.format(*nodeTotTemplate[inode]))

            with open(pathOutToInp + "/" + fileTemplateCEPlowerRigid, 'w') as mor:
                for inode in nodesCEPlower:
                    mor.write(string.format(*nodeTotTemplate[inode]))
            with open(pathOutToInp + "/" + fileTemplateCEPlowerUpRigid, 'w') as mor:
                for inode in nodesCEPlower_up:
                    mor.write(string.format(*nodeTotTemplate[inode]))
            with open(pathOutToInp + "/" + fileTemplateCEPlowerDownRigid, 'w') as mor:
                for inode in nodesCEPlower_down:
                    mor.write(string.format(*nodeTotTemplate[inode]))

    elif rigid == 0:
        # saving the total nodes with the coordinates
        with open(pathTemplate + '/L4-L5_noBEP.txt', 'r') as f:
            reader_f = csv.reader(f)
            for rowf in reader_f:
                nodeTotTemplate[int(rowf[0])] = rowf[1:]

        # the nodes are transfomed from string to float
        for key, value in nodeTotTemplate.items():
            nodeTotTemplate[key] = [
                float(value[0]), float(value[1]), float(value[2])]


    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    ### exception: if rigid registration is enabled (-r)
    if rigid == 1:
        templateAF = pathOutToInp + "/" + fileTemplateAFRigid
        templateNP = pathOutToInp + "/" + fileTemplateNPRigid
        templateMorphed = pathOutToInp + "/" + outPutFileMorphedRigidE
        if regCEP == 1:
            templateCEPupper = pathOutToInp + "/" + fileTemplateCEPupperRigid
            templateCEPupper_up = pathOutToInp + "/" + fileTemplateCEPupperUpRigid
            templateCEPupper_down = pathOutToInp + "/" + fileTemplateCEPupperDownRigid

            templateCEPlower = pathOutToInp + "/" + fileTemplateCEPlowerRigid
            templateCEPlower_up = pathOutToInp + "/" + fileTemplateCEPlowerUpRigid
            templateCEPlower_down = pathOutToInp + "/" + fileTemplateCEPlowerDownRigid

    else:
        templateAF = pathTemplate + "/" + fileTemplateAF
        templateNP = pathTemplate + "/" + fileTemplateNP
        templateMorphed = pathTemplate + "/" + fileTemplateNoBEP
        if regCEP == 1:
            templateCEPupper = pathTemplate + "/" + fileTemplateCEPupper
            templateCEPupper_up = pathTemplate + "/" + fileTemplateCEPupperUpRigid
            templateCEPupper_down = pathTemplate + "/" + fileTemplateCEPupperDownRigid

            templateCEPlower = pathTemplate + "/" + fileTemplateCEPlower
            templateCEPlower_up = pathTemplate + "/" + fileTemplateCEPlowerUpRigid
            templateCEPlower_down = pathTemplate + "/" + fileTemplateCEPlowerDownRigid

    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    ### exception: if external surface registration (including the entire CEP) is enabled (-c)
    if surfRegCEP == 1:
        nodesCEPinIVD = list()
        nodesTransitioninIVD = list()
        nodesNPinIVD = list()
        nodesCEPlowerupInIVD = list()
        nodesOnSurfaceIVDwCEP = list()
        nodesOnSurfaceTempUpper = list()
        nodesExtraCEP = list()
        nodesExtraCEP_AF_Upper = list()
        nodesExtraCEP_NP_Upper = list()
        nodesExtraCEP_AF_Lower = list()
        nodesExtraCEP_NP_Lower = list()

        # firt morph with the external surfaces of AF and NP in

        # creating list with external surfaces of AF and NP with CEP included
        # with CEP
        # nodesOnSurfaceAFwCEP y nodesOnSurfaceNPwCEP
        nodesOnSurfaceAFwoNodesCEP = nodesOnSurfaceAFwCEP.copy()
        nodesOnSurfaceAFwoNodesCEP += nodesOnSurfaceAFMiddle
        # nodesOnSurfaceAFwoNodesCEP += nodesOnSurfaceAFMiddleUpper + nodesOnSurfaceAFMiddleLower
        nodesOnSurfaceAFwoNodesCEP += nodesOnSurfaceTZwCEP
        nodesOnSurfaceAFwoNodesCEP = list(
            dict.fromkeys(nodesOnSurfaceAFwoNodesCEP))

        nodesOnSurfaceNPwoNodesCEP = nodesOnSurfaceNPwCEP.copy()
        # nodesOnSurfaceNPwoNodesCEP += nodesOnSurfaceNPMiddle
        nodesOnSurfaceNPwoNodesCEP += nodesOnSurfaceTZwCEP
        nodesOnSurfaceNPwoNodesCEP = list(
            dict.fromkeys(nodesOnSurfaceNPwoNodesCEP))

        for node in nodesOnSurfaceTZwCEP:
            nodesOnSurfaceAFwoNodesCEP.remove(node)
            nodesOnSurfaceNPwoNodesCEP.remove(node)

        tempCoordCEPUpper = list()
        tempCoordCEPLower = list()

        for node in nodesCEPupper_up:
            if node in nodesOnSurfaceAFwoNodesCEP:
                nodesOnSurfaceAFwoNodesCEP.remove(node)
                tempCoordCEPUpper.append(node)

        for node in nodesCEPlower_down:
            if node in nodesOnSurfaceAFwoNodesCEP:
                nodesOnSurfaceAFwoNodesCEP.remove(node)
                tempCoordCEPLower.append(node)

        nodesOnSurfaceAFwoNodesCEP += tempCoordCEPUpper + tempCoordCEPLower + \
            nodesOnSurfaceTZwoCEP + nodesOnSurfaceTZdiffwCEP
        nodesOnSurfaceNPwoNodesCEP += nodesOnSurfaceTZwoCEP + nodesOnSurfaceTZdiffwCEP

        # defining the stored files
        fileNodesOnSurfaceAFwoNodesCEP = "IVD_" + numberIVD + \
            "_nodesOnSurfaceAFwoNodesCEP_" + patient + ".txt"
        fileNodesOnSurfaceNPwoNodesCEP = "IVD_" + numberIVD + \
            "_nodesOnSurfaceNPwoNodesCEP_" + patient + ".txt"
        fileNodesOnSurfaceCEPupper = "IVD_" + numberIVD + \
            "_nodesOnSurfaceCEPupper_" + patient + ".txt"
        fileNodesOnSurfaceCEPupperUp = "IVD_" + numberIVD + \
            "_nodesOnSurfaceCEPupper_up_" + patient + ".txt"
        fileNodesOnSurfaceCEPupperDown = "IVD_" + numberIVD + \
            "_nodesOnSurfaceCEPupper_down_" + patient + ".txt"
        fileNodesOnSurfaceCEPlower = "IVD_" + numberIVD + \
            "_nodesOnSurfaceCEPlower_" + patient + ".txt"
        fileNodesOnSurfaceCEPlowerUp = "IVD_" + numberIVD + \
            "_nodesOnSurfaceCEPlower_up_" + patient + ".txt"
        fileNodesOnSurfaceCEPlowerDown = "IVD_" + numberIVD + \
            "_nodesOnSurfaceCEPlower_down_" + patient + ".txt"
        print('-------------------------------------------------------------------------------')
        print(' ')
        print('writing the files that will be used to morph the external surfaces of AF and NP without CEP internal nodes included')
        print('')
        string = '{:.8f},{:.8f},{:.8f}'
        string += '\n'

        with open(pathOutToInp + "/" + fileNodesOnSurfaceAFwoNodesCEP, 'w') as f:
            write = csv.writer(f, delimiter='\t')
            for inode, node in enumerate(nodesOnSurfaceAFwoNodesCEP):
                write.writerow(nodeTotTemplate[nodesOnSurfaceAFwoNodesCEP[inode]])

        with open(pathOutToInp + "/" + fileNodesOnSurfaceNPwoNodesCEP, 'w') as f:
            write = csv.writer(f, delimiter='\t')
            for inode, node in enumerate(nodesOnSurfaceNPwoNodesCEP):
                write.writerow(nodeTotTemplate[nodesOnSurfaceNPwoNodesCEP[inode]])

        print('The files nodesOnSurface AF and NP without CEP internal nodes files were move to: ' + pathOutToInp)
        print('')

        if regCEP == 1:
            with open(pathOutToInp + "/" + fileNodesOnSurfaceCEPupper, 'w') as f:
                write = csv.writer(f, delimiter='\t')
                for inode, node in enumerate(nodesOnSurfaceCEPupper):
                    write.writerow(nodeTotTemplate[nodesOnSurfaceCEPupper[inode]])
            with open(pathOutToInp + "/" + fileNodesOnSurfaceCEPupperUp, 'w') as f:
                write = csv.writer(f, delimiter='\t')
                for inode, node in enumerate(nodesCEPupper_up):
                    write.writerow(nodeTotTemplate[nodesCEPupper_up[inode]])
            with open(pathOutToInp + "/" + fileNodesOnSurfaceCEPupperDown, 'w') as f:
                write = csv.writer(f, delimiter='\t')
                for inode, node in enumerate(nodesCEPupper_down):
                    write.writerow(nodeTotTemplate[nodesCEPupper_down[inode]])

            with open(pathOutToInp + "/" + fileNodesOnSurfaceCEPlower, 'w') as f:
                write = csv.writer(f, delimiter='\t')
                for inode, node in enumerate(nodesOnSurfaceCEPlower):
                    write.writerow(nodeTotTemplate[nodesOnSurfaceCEPlower[inode]])
            with open(pathOutToInp + "/" + fileNodesOnSurfaceCEPlowerUp, 'w') as f:
                write = csv.writer(f, delimiter='\t')
                for inode, node in enumerate(nodesCEPlower_up):
                    write.writerow(nodeTotTemplate[nodesCEPlower_up[inode]])
            with open(pathOutToInp + "/" + fileNodesOnSurfaceCEPlowerDown, 'w') as f:
                write = csv.writer(f, delimiter='\t')
                for inode, node in enumerate(nodesCEPlower_down):
                    write.writerow(nodeTotTemplate[nodesCEPlower_down[inode]])

            print('The files nodesOnSurface CEP upper and lower were move to: ' + pathOutToInp)
            print('')

        # defFuncNonRigid(targetFile, sourceFile, outPutFileName, lambdaVal, betaVal, nLoops, lenTarget, lenSource)

        funcNodesOnSurfaceAFwoNodesCEP = defFuncNonRigid(pathTarget + "/" + fileTargetAF, pathOutToInp + "/" + fileNodesOnSurfaceAFwoNodesCEP,
                                                        outPutFileNodesOnSurfaceAFwoNodesCEP, 0.7, 2.0, 1000, line_count_AF, len(nodesOnSurfaceAFwoNodesCEP))

        funcNodesOnSurfaceNPwoNodesCEP = defFuncNonRigid(pathTarget + "/" + fileTargetNP, pathOutToInp + "/" + fileNodesOnSurfaceNPwoNodesCEP,
                                                        outPutFileNodesOnSurfaceNPwoNodesCEP, 0.7, 2.0, 1000, line_count_NP, len(nodesOnSurfaceNPwoNodesCEP))

        if regCEP == 1:

            funcNodesOnSurfaceCEPupperUP = defFuncNonRigid(pathTarget + "/" + fileTargetCEPupper_up, pathOutToInp + "/" + fileNodesOnSurfaceCEPupperUp,
                                                        outPutFileNodesOnSurfaceCEPupperUp, 0.7, 2.0, 1000, line_count_CEPupperUp, len(nodesCEPupper_up))
            funcNodesOnSurfaceCEPupperDown = defFuncNonRigid(pathTarget + "/" + fileTargetCEPupper_down, pathOutToInp + "/" + fileNodesOnSurfaceCEPupperDown,
                                                            outPutFileNodesOnSurfaceCEPupperDown, 0.7, 2.0, 1000, line_count_CEPupperDown, len(nodesCEPupper_down))

            funcNodesOnSurfaceCEPlowerUP = defFuncNonRigid(pathTarget + "/" + fileTargetCEPlower_up, pathOutToInp + "/" + fileNodesOnSurfaceCEPlowerUp,
                                                        outPutFileNodesOnSurfaceCEPlowerUp, 0.7, 2.0, 1000, line_count_CEPlowerUp, len(nodesCEPlower_up))
            funcNodesOnSurfaceCEPlowerDown = defFuncNonRigid(pathTarget + "/" + fileTargetCEPlower_down, pathOutToInp + "/" + fileNodesOnSurfaceCEPlowerDown,
                                                            outPutFileNodesOnSurfaceCEPlowerDown, 0.7, 2.0, 1000, line_count_CEPlowerDown, len(nodesCEPlower_down))

            funcNodesOnSurfaceCEPupper = defFuncNonRigid(pathTarget + "/" + fileTargetCEPupper, pathOutToInp + "/" + fileNodesOnSurfaceCEPupper,
                                                        outPutFileNodesOnSurfaceCEPupper, 0.7, 2.0, 1000, line_count_CEPupper, len(nodesOnSurfaceCEPupper))

            funcNodesOnSurfaceCEPlower = defFuncNonRigid(pathTarget + "/" + fileTargetCEPlower, pathOutToInp + "/" + fileNodesOnSurfaceCEPlower,
                                                        outPutFileNodesOnSurfaceCEPlower, 0.7, 2.0, 1000, line_count_CEPlower, len(nodesOnSurfaceCEPlower))

            #-------------------------------------------------------------------------------
            # CEP upper:

            defNonRigid("CEP upper Up:", numberIVD, patient, funcNodesOnSurfaceCEPupperUP,
                        outPutFileNodesOnSurfaceCEPupperUp, pathOutToInp)
            defNonRigid("CEP upper Down:", numberIVD, patient, funcNodesOnSurfaceCEPupperDown,
                        outPutFileNodesOnSurfaceCEPupperDown, pathOutToInp)
    #        defNonRigid("CEP upper:", numberIVD, patient, funcNodesOnSurfaceCEPupper, outPutFileNodesOnSurfaceCEPupper, pathOutToInp)

            #-------------------------------------------------------------------------------
            # CEP lower:
            defNonRigid("CEP lower Up:", numberIVD, patient, funcNodesOnSurfaceCEPlowerUP,
                        outPutFileNodesOnSurfaceCEPlowerUp, pathOutToInp)
            defNonRigid("CEP lower Down:", numberIVD, patient, funcNodesOnSurfaceCEPlowerDown,
                        outPutFileNodesOnSurfaceCEPlowerDown, pathOutToInp)
    #        defNonRigid("CEP lower:", numberIVD, patient, funcNodesOnSurfaceCEPlower, outPutFileNodesOnSurfaceCEPlower, pathOutToInp)

        if (morph == 4 or morph == 5):
            #-------------------------------------------------------------------------------
            # AF without CEP internal nodes:
            #defNonRigid(nameMorph, numberIVD, patientID, funcNonRigid, outPutFileName, pathOut)

            defNonRigid("AF without CEP internal nodes:", numberIVD, patient,
                        funcNodesOnSurfaceAFwoNodesCEP, outPutFileNodesOnSurfaceAFwoNodesCEP, pathOutToInp)

            #-------------------------------------------------------------------------------
            # NP without CEP internal nodes:

            defNonRigid("NP without CEP internal nodes:", numberIVD, patient,
                        funcNodesOnSurfaceNPwoNodesCEP, outPutFileNodesOnSurfaceNPwoNodesCEP, pathOutToInp)

        # obtaning the nodes on surface of TZ from the NP, and put it in the AF
        coordCEPTZ = list()
        coordTZ = list()
        lenTZAF = len(nodesOnSurfaceAFwoNodesCEP) - len(nodesOnSurfaceTZwCEP)
        lenTZNP = len(nodesOnSurfaceNPwoNodesCEP) - len(nodesOnSurfaceTZwCEP)

        count = 0
        with open(pathOutToInp + "/" + outPutFileNodesOnSurfaceAFwoNodesCEPE, 'r') as fp:
            reader_f = csv.reader(fp, delimiter='\t')
            for line in reader_f:
                if count < lenTZAF:
                    coordCEPTZ.append(
                        [float(line[0]), float(line[1]), float(line[2])])
                count += 1

        count = 0
        with open(pathOutToInp + "/" + outPutFileNodesOnSurfaceNPwoNodesCEPE, 'r') as fp:
            reader_f = csv.reader(fp, delimiter='\t')
            for line in reader_f:
                if count >= lenTZNP:
                    coordCEPTZ.append(
                        [float(line[0]), float(line[1]), float(line[2])])
                    coordTZ.append(
                        [float(line[0]), float(line[1]), float(line[2])])
                count += 1

        if (morph == 4 or morph == 5):
            with open(pathOutToInp + "/" + outPutFileNodesOnSurfaceAFwoNodesCEPE, 'w') as f:
                write = csv.writer(f, delimiter='\t')
                for inode, node in enumerate(coordCEPTZ):
                    write.writerow(coordCEPTZ[inode])

    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # THIS PART IT IS JUST TO OBTAIN THE INTERNAL CEP NODES

        #-------------------------------------------------------------------------------
        # creating nodes of CEP that are in AF and NP respectively
        # nodesExtraCEP: internal nodes of CEP

        for node in nodesCEPupper:
            if node in nodesAFwCEP:
                nodesExtraCEP_AF_Upper.append(node)
            if node in nodesNPwCEP:
                nodesExtraCEP_NP_Upper.append(node)

        for node in nodesCEPlower:
            if node in nodesAFwCEP:
                nodesExtraCEP_AF_Lower.append(node)
            if node in nodesNPwCEP:
                nodesExtraCEP_NP_Lower.append(node)

        # creating the surfaces of Af and NP with the respectively CEP nodes
        nodesOnSurfaceAFwNodesCEP = nodesOnSurfaceAFwoCEP.copy()
        nodesOnSurfaceAFwNodesCEP += nodesOnSurfaceAFMiddle
        # nodesOnSurfaceAFwNodesCEP += nodesOnSurfaceAFMiddleUpper + nodesOnSurfaceAFMiddleLower
        nodesOnSurfaceAFwNodesCEP = list(dict.fromkeys(nodesOnSurfaceAFwNodesCEP))

        nodesOnSurfaceNPwNodesCEP = nodesOnSurfaceNPwoCEP.copy()
        nodesOnSurfaceNPwNodesCEP = list(dict.fromkeys(nodesOnSurfaceNPwNodesCEP))

        nodesOnSurfaceAFwNodesCEP = list(
            set(nodesOnSurfaceAFwNodesCEP) - set(nodesOnSurfaceAFCEPUpper))
        nodesOnSurfaceAFwNodesCEP = list(
            set(nodesOnSurfaceAFwNodesCEP) - set(nodesOnSurfaceAFCEPLower))
        nodesOnSurfaceAFwNodesCEP = list(dict.fromkeys(nodesOnSurfaceAFwNodesCEP))
        nodesOnSurfaceAFwNodesCEP += nodesExtraCEP_AF_Upper + nodesExtraCEP_AF_Lower

        nodesOnSurfaceNPwNodesCEP = list(
            set(nodesOnSurfaceNPwNodesCEP) - set(nodesOnSurfaceNPCEPUpper))
        nodesOnSurfaceNPwNodesCEP = list(
            set(nodesOnSurfaceNPwNodesCEP) - set(nodesOnSurfaceNPCEPLower))
        nodesOnSurfaceNPwNodesCEP = list(dict.fromkeys(nodesOnSurfaceNPwNodesCEP))
        nodesOnSurfaceNPwNodesCEP += nodesExtraCEP_NP_Upper + nodesExtraCEP_NP_Lower

        # for AF is necessary extract TZ nodes to use the TZ of NP in the future

        for node in nodesOnSurfaceTZwCEP:

            #removing TZ in the complete surface model
            nodesOnSurfaceAFwNodesCEP.remove(node)
            nodesOnSurfaceNPwNodesCEP.remove(node)

            #removing TZ of the internal nodes of CEP
            if node in nodesExtraCEP_AF_Upper:
                nodesExtraCEP_AF_Upper.remove(node)
            if node in nodesExtraCEP_AF_Lower:
                nodesExtraCEP_AF_Lower.remove(node)

            if node in nodesExtraCEP_NP_Upper:
                nodesExtraCEP_NP_Upper.remove(node)
            if node in nodesExtraCEP_NP_Lower:
                nodesExtraCEP_NP_Lower.remove(node)

            # removing TZ of the contact surface between CEP and AF-NP
            if node in nodesOnSurfaceAFCEPUpper:
                nodesOnSurfaceAFCEPUpper.remove(node)
            if node in nodesOnSurfaceAFCEPLower:
                nodesOnSurfaceAFCEPLower.remove(node)

            if node in nodesOnSurfaceNPCEPUpper:
                nodesOnSurfaceNPCEPUpper.remove(node)
            if node in nodesOnSurfaceNPCEPLower:
                nodesOnSurfaceNPCEPLower.remove(node)

        # extracting the nodes that share AF and CEP to the AF-CEP
        nodesOnSurfaceTempAFUpper = nodesExtraCEP_AF_Upper.copy()
        for node in nodesOnSurfaceAFCEPUpper:
            nodesOnSurfaceTempAFUpper.remove(node)

        nodesOnSurfaceTempAFLower = nodesExtraCEP_AF_Lower.copy()
        for node in nodesOnSurfaceAFCEPLower:
            nodesOnSurfaceTempAFLower.remove(node)

        # extracting the nodes that share NP and CEP to the NP-CEP
        nodesOnSurfaceTempNPUpper = nodesExtraCEP_NP_Upper.copy()
        for node in nodesOnSurfaceNPCEPUpper:
            nodesOnSurfaceTempNPUpper.remove(node)

        nodesOnSurfaceTempNPLower = nodesExtraCEP_NP_Lower.copy()
        for node in nodesOnSurfaceNPCEPLower:
            nodesOnSurfaceTempNPLower.remove(node)

        # extracting the CEP nodes from AF and NP to reorganizing them
        for node in nodesCEPupper:
            if node in nodesOnSurfaceAFwNodesCEP:
                nodesOnSurfaceAFwNodesCEP.remove(node)
            if node in nodesOnSurfaceNPwNodesCEP:
                nodesOnSurfaceNPwNodesCEP.remove(node)

        for node in nodesCEPlower:
            if node in nodesOnSurfaceAFwNodesCEP:
                nodesOnSurfaceAFwNodesCEP.remove(node)
            if node in nodesOnSurfaceNPwNodesCEP:
                nodesOnSurfaceNPwNodesCEP.remove(node)

        # establish the nodes in the requiered order
        nodesOnSurfaceAFwNodesCEP += nodesOnSurfaceAFCEPUpper + nodesOnSurfaceAFCEPLower + \
            nodesOnSurfaceTZwoCEP + nodesOnSurfaceTZdiffwCEP + \
            nodesOnSurfaceTempAFUpper + nodesOnSurfaceTempAFLower
        nodesOnSurfaceNPwNodesCEP += nodesOnSurfaceNPCEPUpper + nodesOnSurfaceNPCEPLower + \
            nodesOnSurfaceTZwoCEP + nodesOnSurfaceTZdiffwCEP + \
            nodesOnSurfaceTempNPUpper + nodesOnSurfaceTempNPLower

        # defining the stored files
        fileNodesOnSurfaceAFwNodesCEP = "IVD_" + numberIVD + \
            "_nodesOnSurfaceAFwNodesCEP_" + patient + ".txt"
        fileNodesOnSurfaceNPwNodesCEP = "IVD_" + numberIVD + \
            "_nodesOnSurfaceNPwNodesCEP_" + patient + ".txt"
        print('-------------------------------------------------------------------------------')
        print(' ')
        print('writing the files that will be used to morph the external surfaces of AF and NP with CEP included')
        print('')
        string = '{:.8f},{:.8f},{:.8f}'
        string += '\n'

        with open(pathOutToInp + "/" + fileNodesOnSurfaceAFwNodesCEP, 'w') as f:
            write = csv.writer(f, delimiter='\t')
            for inode, node in enumerate(nodesOnSurfaceAFwNodesCEP):
                write.writerow(nodeTotTemplate[nodesOnSurfaceAFwNodesCEP[inode]])

        with open(pathOutToInp + "/" + fileNodesOnSurfaceNPwNodesCEP, 'w') as f:
            write = csv.writer(f, delimiter='\t')
            for inode, node in enumerate(nodesOnSurfaceNPwNodesCEP):
                write.writerow(nodeTotTemplate[nodesOnSurfaceNPwNodesCEP[inode]])

        print('The files nodesOnSurface AF and NP with CEP files were move to: ' + pathOutToInp)
        print('')

        # defFuncNonRigid(targetFile, sourceFile, outPutFileName, lambdaVal, betaVal, nLoops, lenTarget, lenSource)

        funcNodesOnSurfaceAFwNodesCEP = defFuncNonRigid(pathTarget + "/" + fileTargetAF, pathOutToInp + "/" + fileNodesOnSurfaceAFwNodesCEP,
                                                        outPutFileNodesOnSurfaceAFwNodesCEP, 2.0, 2.0, 1000, line_count_AF, len(nodesOnSurfaceAFwNodesCEP))

        funcNodesOnSurfaceNPwNodesCEP = defFuncNonRigid(pathTarget + "/" + fileTargetNP, pathOutToInp + "/" + fileNodesOnSurfaceNPwNodesCEP,
                                                        outPutFileNodesOnSurfaceNPwNodesCEP, 2.0, 2.0, 1000, line_count_NP, len(nodesOnSurfaceNPwNodesCEP))

        if (morph == 4 or morph == 5):
            #-------------------------------------------------------------------------------
            # AF with CEP internal nodes:
            #defNonRigid(nameMorph, numberIVD, patientID, funcNonRigid, outPutFileName, pathOut)

            defNonRigid("AF with CEP internal nodes:", numberIVD, patient,
                        funcNodesOnSurfaceAFwNodesCEP, outPutFileNodesOnSurfaceAFwNodesCEP, pathOutToInp)

            #-------------------------------------------------------------------------------
            # NP with CEP internal nodes:

            defNonRigid("NP with CEP internal nodes:", numberIVD, patient,
                        funcNodesOnSurfaceNPwNodesCEP, outPutFileNodesOnSurfaceNPwNodesCEP, pathOutToInp)

        # larges to identify limits
        len_AF_replace_TZ = len(nodesOnSurfaceAFwNodesCEP) - len(nodesOnSurfaceTZwCEP) - \
            len(nodesOnSurfaceTempAFUpper) - len(nodesOnSurfaceTempAFLower)
        len_NP_replace_TZ = len(nodesOnSurfaceNPwNodesCEP) - len(nodesOnSurfaceTZwCEP) - \
            len(nodesOnSurfaceTempNPUpper) - len(nodesOnSurfaceTempNPLower)
        len_CEP_AF = len(nodesOnSurfaceAFwNodesCEP) - \
            len(nodesOnSurfaceTempAFUpper) - len(nodesOnSurfaceTempAFLower)
        len_CEP_AF_TZ = len(nodesOnSurfaceAFwNodesCEP) - len(nodesOnSurfaceTZdiffwCEP) - \
            len(nodesOnSurfaceTempAFUpper) - len(nodesOnSurfaceTempAFLower)
        len_CEP_NP_1 = len(nodesOnSurfaceNPwNodesCEP) - \
            len(nodesOnSurfaceTempNPUpper) - len(nodesOnSurfaceTempNPLower)
        len_CEP_NP_2 = len(nodesOnSurfaceNPwNodesCEP) - len(nodesOnSurfaceTZdiffwCEP) - \
            len(nodesOnSurfaceTempNPUpper) - len(nodesOnSurfaceTempNPLower)
        len_CEP_AF_contact = len(nodesOnSurfaceAFwNodesCEP) - len(nodesOnSurfaceAFCEPUpper) - len(nodesOnSurfaceAFCEPLower) - \
            len(nodesOnSurfaceTZwCEP) - len(nodesOnSurfaceTempAFUpper) - \
            len(nodesOnSurfaceTempAFLower)
        len_CEP_AF_contact2 = len(nodesOnSurfaceAFwoNodesCEP) - len(
            tempCoordCEPUpper) - len(tempCoordCEPLower) - len(nodesOnSurfaceTZwCEP)
        len_CEP_AF_contact3 = len(
            nodesOnSurfaceAFwoNodesCEP) - len(nodesOnSurfaceTZwCEP)
        len_CEP_AF_contact4 = len(nodesOnSurfaceAFwoNodesCEP) - \
            len(nodesOnSurfaceTZdiffwCEP)

        coordAF = list()
        coordAF_final = list()
        coordNP = list()

        # reeplacing TZ nodes for the initials
        # AF
        with open(pathOutToInp + "/" + outPutFileNodesOnSurfaceAFwNodesCEPE, 'r') as fp:
            reader_f = csv.reader(fp, delimiter='\t')
            for line in reader_f:
                coordAF.append([float(line[0]), float(line[1]), float(line[2])])

        count = 0
        for inode, node in enumerate(nodesOnSurfaceAFwNodesCEP):
            if (inode >= len_AF_replace_TZ and inode < len_CEP_AF):
                coordAF[inode] = coordTZ[count]
                count += 1

        with open(pathOutToInp + "/" + outPutFileNodesOnSurfaceAFwNodesCEPE, 'w') as f:
            write = csv.writer(f, delimiter='\t')
            for inode, node in enumerate(coordAF):
                write.writerow(coordAF[inode])

        # NP
        with open(pathOutToInp + "/" + outPutFileNodesOnSurfaceNPwNodesCEPE, 'r') as fp:
            reader_f = csv.reader(fp, delimiter='\t')
            for line in reader_f:
                coordNP.append([float(line[0]), float(line[1]), float(line[2])])

        count = 0
        for inode, node in enumerate(nodesOnSurfaceNPwNodesCEP):
            if (inode >= len_NP_replace_TZ and inode < len_CEP_NP_1):
                coordNP[inode] = coordTZ[count]
                count += 1

        with open(pathOutToInp + "/" + outPutFileNodesOnSurfaceNPwNodesCEPE, 'w') as f:
            write = csv.writer(f, delimiter='\t')
            for inode, node in enumerate(coordNP):
                write.writerow(coordNP[inode])

        # editing the files and obtaining the CEP morphing nodes
        coordCEPtotAF = list()
        coordCEPtotNP = list()
        coordCEPtotFinal = list()

        count = 0
        with open(pathOutToInp + "/" + outPutFileNodesOnSurfaceAFwNodesCEPE, 'r') as fp:
            reader_f = csv.reader(fp, delimiter='\t')
            for line in reader_f:
                if count >= len_CEP_AF:
                    coordCEPtotFinal.append(
                        [float(line[0]), float(line[1]), float(line[2])])
                count += 1

        for inode, node in enumerate(coordAF):
            if (inode >= len_CEP_AF_contact and inode < len_AF_replace_TZ):
                coordCEPtotAF.append(coordAF[inode])

        for inode, node in enumerate(coordCEPTZ):
            if (inode < len_CEP_AF_contact2 or (inode >= len_CEP_AF_contact3 and inode < len_CEP_AF_contact4)):
                coordCEPtotAF.append(coordCEPTZ[inode])

        count = 0
        with open(pathOutToInp + "/" + outPutFileNodesOnSurfaceNPwNodesCEPE, 'r') as fp:
            reader_f = csv.reader(fp, delimiter='\t')
            for line in reader_f:
                if count < len_CEP_NP_2:
                    coordCEPtotNP.append(
                        [float(line[0]), float(line[1]), float(line[2])])
                elif count >= len_CEP_NP_2:
                    coordCEPtotFinal.append(
                        [float(line[0]), float(line[1]), float(line[2])])
                count += 1

        outPutFileNodesOnSurfaceAFwoCEP_final = "IVD_" + numberIVD + \
            "_nodesOnSurfaceAFwoCEP_" + patient + "_final.txt"
        outPutFileNodesOnSurfaceNPwoCEP_final = "IVD_" + numberIVD + \
            "_nodesOnSurfaceNPwoCEP_" + patient + "_final.txt"

        with open(pathOutToInp + "/" + outPutFileNodesOnSurfaceAFwoCEP_final, 'w') as f:
            write = csv.writer(f, delimiter='\t')
            for inode, node in enumerate(coordCEPtotAF):
                write.writerow(coordCEPtotAF[inode])

        with open(pathOutToInp + "/" + outPutFileNodesOnSurfaceNPwoCEP_final, 'w') as f:
            write = csv.writer(f, delimiter='\t')
            for inode, node in enumerate(coordCEPtotNP):
                write.writerow(coordCEPtotNP[inode])


    ### exception: if external surface registration (including the entire CEP) is enabled (-c)
    if surfRegCEP == 1:
        targetAF = pathOutToInp + "/" + outPutFileNodesOnSurfaceAFwoCEP_final
        targetNP = pathOutToInp + "/" + outPutFileNodesOnSurfaceNPwoCEP_final
        lenNodesTargetNumberAF = len(coordCEPtotAF)
        lenNodesTemplateNumberAF = len(nodesTemplateNumberAF)
        lenNodesTargetNumberNP = len(coordCEPtotNP)
        lenNodesTemplateNumberNP = len(nodesTemplateNumberNP)
        lenNodeMorphed = len(nodeNoBEPTemplate)

    else:
        targetAF = pathTarget + "/" + fileTargetAF
        targetNP = pathTarget + "/" + fileTargetNP
        lenNodesTargetNumberAF = line_count_AF
        lenNodesTemplateNumberAF = len(nodesTemplateNumberAF)
        lenNodesTargetNumberNP = line_count_NP
        lenNodesTemplateNumberNP = len(nodesTemplateNumberNP)
        lenNodeMorphed = len(nodeNoBEPTemplate)

    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # bcpd functions for AF, NP, al final merged morphed

    # defFuncNonRigid(targetFile, sourceFile, outPutFileName, lambdaVal, betaVal, nLoops, lenTarget, lenSource)
    # defFuncRigid(targetFile, sourceFile, outPutFileName, nLoops, lenTarget, lenSource)

    funcAF = defFuncNonRigid(targetAF, templateAF, outPutFileAF,
                            2.0, 2.0, 1000, lenNodesTargetNumberAF, lenNodesTemplateNumberAF)

    funcRigidNP = defFuncRigid(targetNP, templateNP, outPutFileNP,
                            1000, lenNodesTargetNumberNP, lenNodesTemplateNumberNP)

    funcNP = defFuncNonRigid(targetNP, pathOutToInp + "/" + outPutFileNPE, outPutFileNP,
                            2.0, 2.0, 1000, lenNodesTargetNumberNP, lenNodesTemplateNumberNP)

    funcMorphed = defFuncNonRigid(pathOutToInp + "/" + fileMorphed, templateMorphed, outPutFileMorphed,
                                2.0, 2.0, 1000, lenNodeMorphed, lenNodeMorphed)

    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # non-rigid registration

    # AF:
    if (morph == 1 or morph == 5):
        defNonRigid("AF", numberIVD, patient, funcAF, outPutFileAF, pathOutToInp)

    # NP:
    if (morph == 2 or morph == 5):
        defRigid("NP", numberIVD, patient, funcRigidNP, outPutFileNP, pathOutToInp)

        defNonRigid("NP", numberIVD, patient, funcNP, outPutFileNP, pathOutToInp)

    # merged morphed:

    string = '{:.8f}\t{:.8f}\t{:.8f}'
    string += '\n'
    if (morph == 3 or morph == 5):
        ###exception: if fusion (merge AF and NP) is selected (-f, by default == 1)
        if fusion == 0:
            print("reading the morphed file: " +
                fileMorphed + " in " + pathOutToInp)
            print("")
        elif fusion == 1:
            print("creating the morphed file: " +
                fileMorphed + " in " + pathOutToInp)
            print("")
            dataMerged = list()

            len_AF_TZ = len(nodesTemplateNumberAF) - len(nodeTransitionTemplate)

            count = 0
            # Reading data from AF
            with open(pathOutToInp + "/" + outPutFileAFE, 'r') as fp:
                reader_f = csv.reader(fp, delimiter='\t')
                for line in reader_f:
                    if count < len_AF_TZ:
                        dataMerged.append(
                            [float(line[0]), float(line[1]), float(line[2])])
                        count += 1

            count = 0
            # Reading data from NP
            with open(pathOutToInp + "/" + outPutFileNPE, 'r') as fp:
                reader_f = csv.reader(fp, delimiter='\t')
                for line in reader_f:
                    dataMerged.append(
                        [float(line[0]), float(line[1]), float(line[2])])
                    count += 1

            with open(pathOutToInp + "/" + fileMorphed, 'w') as fp:
                for inode, node in enumerate(dataMerged):
                    fp.write(string.format(*dataMerged[inode]))
                if surfRegCEP == 1:
                    for inode, node in enumerate(coordCEPtotFinal):
                        fp.write(string.format(*coordCEPtotFinal[inode]))

        defNonRigid("Entire IVD", numberIVD, patient,
                    funcMorphed, outPutFileMorphed, pathOutToInp)

    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # creating .inp files

    # obtaining the coordinates of the node 71143

    coordCentralNode = ObtainCentroid(
        outPutFileMorphedE, pathOutToInp, nodeNoBEPTemplate)

    # define the string format to write the rigid registration temporal file
    stringFormat = '{},{:.8f},{:.8f},{:.8f}'
    stringFormat += '\n'

    # AF:
    if (toINP == 1 or toINP == 4):

        createInpFile("AF", numberIVD, patient, outPutFileAFE, outPutFileMorphedAF, pathOutToInp,
                    pathParts, pathInpTemplateAF, nodesTemplateNumberAF, stringFormat, coordCentralNode)

    # NP:
    if (toINP == 2 or toINP == 4):

        createInpFile("NP", numberIVD, patient, outPutFileNPE, outPutFileMorphedNP, pathOutToInp,
                    pathParts, pathInpTemplateNP, nodesTemplateNumberNP, stringFormat, coordCentralNode)

    # morphed:
    if (toINP == 3 or toINP == 4):

        createInpFile("Morphed", numberIVD, patient, outPutFileMorphedE, outPutFileMorphedIVD, pathOutToInp,
                    pathCompleted, pathInpTemplateMorphed, nodeNoBEPTemplate, stringFormat, coordCentralNode)

    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #failedElem:

    if (checkFElem == 1 or checkFElem == 2):
        gap = 0

        # checkFailedElem(outPutFileFailedElem, outPutFileMorphedIVD, pathInp, numberIVD, patientID, gap)
        lenFailedElem = checkFailedElem(
            outPutFileFailedElem, outPutFileMorphedIVD, pathCompleted, numberIVD, patient, gap)

        gap = 0.5

        if checkFElem == 2:
            while (lenFailedElem > 0 and gap < 15):

                funcMorphed = defFuncNonRigid(pathOutToInp + "/" + fileMorphed, templateMorphed, outPutFileMorphed,
                                            3.0+gap, 2.0, 1000, lenNodeMorphed, lenNodeMorphed)

                defNonRigid("Entire IVD", numberIVD, patient,
                            funcMorphed, outPutFileMorphed, pathOutToInp)

                #-----------------------------------------------------------------------
                # creating .inp

                coordCentralNode = ObtainCentroid(
                    outPutFileMorphedE, pathOutToInp, nodeNoBEPTemplate)

                createInpFile("Morphed", numberIVD, patient, outPutFileMorphedE, outPutFileMorphedIVD,
                            pathOutToInp, pathCompleted, pathInpTemplateMorphed, nodeNoBEPTemplate, stringFormat, coordCentralNode)

                #-----------------------------------------------------------------------
                # check failed elements

                # checkFailedElem(outPutFileFailedElem, outPutFileMorphedIVD, pathInp, numberIVD, patientID, gap)
                lenFailedElem = checkFailedElem(
                    outPutFileFailedElem, outPutFileMorphedIVD, pathCompleted, numberIVD, patient, gap)

                gap += 0.5

    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #euclidean distance:

    if checkHaus == 1:
        print('-------------------------------------------------------------------------------')
        print("")
        print("Cheking the accuracy of the morphing process...")
        print("")
        totCoordToCheck = dict()
        AFCoordToCheckMorph = np.empty((0, 3), int)
        NPCoordToCheckMorph = np.empty((0, 3), int)
        AFCoordToCheckPS = np.empty((0, 3), int)
        NPCoordToCheckPS = np.empty((0, 3), int)
        AFCoordToCheckScale = np.empty((0, 3), int)
        NPCoordToCheckScale = np.empty((0, 3), int)
        tempCoord = list()

        #-----------------------------------------------------------------------
        # reading the .inp morphed file
        count = 1
        with open(pathCompleted + "/" + outPutFileMorphedIVD, 'r') as fp:
            reader_f = csv.reader(fp, delimiter=',')
            for line in reader_f:
                if (count >= 10) and (count <= 83490):
                    totCoordToCheck[int(line[0])] = [float(
                        line[1]), float(line[2]), float(line[3])]
                count += 1

        #-----------------------------------------------------------------------
        # storing the coordinates of the morphed AF and NP by separately
        for key, value in totCoordToCheck.items():
            # AF
            if key in nodesOnSurfaceAFwCEP:
                tempCoord = [float(value[0]), float(value[1]), float(value[2])]
                AFCoordToCheckMorph = np.append(
                    AFCoordToCheckMorph, np.array([tempCoord]), axis=0)

            # NP
            if key in nodesOnSurfaceNPwCEP:
                tempCoord = [float(value[0]), float(value[1]), float(value[2])]
                NPCoordToCheckMorph = np.append(
                    NPCoordToCheckMorph, np.array([tempCoord]), axis=0)

        #-----------------------------------------------------------------------
        # storing the coordinates of the PS AF and NP by separately
        # AF
        with open(pathTarget + "/" + fileTargetAF, 'r') as fp:
            reader_f = csv.reader(fp, delimiter=',')
            for line in reader_f:
                tempCoord = [float(line[0]), float(line[1]), float(line[2])]
                AFCoordToCheckPS = np.append(
                    AFCoordToCheckPS, np.array([tempCoord]), axis=0)

        # NP
        with open(pathTarget + "/" + fileTargetNP, 'r') as fp:
            reader_f = csv.reader(fp, delimiter=',')
            for line in reader_f:
                tempCoord = [float(line[0]), float(line[1]), float(line[2])]
                NPCoordToCheckPS = np.append(
                    NPCoordToCheckPS, np.array([tempCoord]), axis=0)

        # obtaining the centroid of AF and NP PS models
        centroidAFPS = np.mean(AFCoordToCheckPS, axis=0)
        centroidNPPS = np.mean(AFCoordToCheckPS, axis=0)
        centroidAFMorph = np.mean(AFCoordToCheckMorph, axis=0)
        centroidNPMorph = np.mean(NPCoordToCheckMorph, axis=0)

        # move all the nodes from the centroid to the (0,0,0)
        # PS
        for i in range(0, len(AFCoordToCheckPS)):
            AFCoordToCheckPS[i] = AFCoordToCheckPS[i] - centroidAFPS
        for i in range(0, len(NPCoordToCheckPS)):
            NPCoordToCheckPS[i] = NPCoordToCheckPS[i] - centroidNPPS

        # Morphed
        # for i in range(0, len(AFCoordToCheckMorph)):
        #     AFCoordToCheckMorph[i] = AFCoordToCheckMorph[i] - centroidAFMorph
        # for i in range(0, len(NPCoordToCheckMorph)):
        #     NPCoordToCheckMorph[i] = NPCoordToCheckMorph[i] - centroidNPMorph

        #-----------------------------------------------------------------------
        # scaling the coordinates of the PS AF and NP
        scaleFactor = 1.1
        # AF
        for i in range(0, len(AFCoordToCheckPS)):
            AFCoordToCheckScale = np.append(AFCoordToCheckScale, np.array(
                [[AFCoordToCheckPS[i][0]*scaleFactor, AFCoordToCheckPS[i][1]*scaleFactor, AFCoordToCheckPS[i][2]*scaleFactor]]), axis=0)
        # NP
        for i in range(0, len(NPCoordToCheckPS)):
            NPCoordToCheckScale = np.append(NPCoordToCheckScale, np.array(
                [[NPCoordToCheckPS[i][0]*scaleFactor, NPCoordToCheckPS[i][1]*scaleFactor, NPCoordToCheckPS[i][2]*scaleFactor]]), axis=0)

        #-----------------------------------------------------------------------
        # checking max distance
        print("comparing the AF PS with the scaled one...")
        print("")
        distAFscale, avgAFscale, medianAFscale = hausdorff(
            AFCoordToCheckPS, AFCoordToCheckScale)

        print("comparing the NP PS with the scaled one...")
        print("")
        distNPscale, avgNPscale, medianNPscale = hausdorff(
            NPCoordToCheckPS, NPCoordToCheckScale)

        print("Max distance between the nodes of the PS and the scale PS models of AF and NP are:")
        print("")
        print("AF max distance, average distance, median distance: " +
            str(distAFscale), str(avgAFscale), str(medianAFscale))
        print("NP max distance, average distance, median distance: " +
            str(distNPscale), str(avgNPscale), str(medianNPscale))
        print("")

        # move all the nodes from the (0,0,0) to the original centroid
        for i in range(0, len(AFCoordToCheckPS)):
            AFCoordToCheckPS[i] = AFCoordToCheckPS[i] + centroidAFPS
        for i in range(0, len(NPCoordToCheckPS)):
            NPCoordToCheckPS[i] = NPCoordToCheckPS[i] + centroidNPPS

        print("comparing the AF external surface...")
        print("")
        distAF, avgAF, medianAF = hausdorff(AFCoordToCheckPS, AFCoordToCheckMorph)

        print("comparing the NP external surface...")
        print("")
        distNP, avgNP, medianNP = hausdorff(NPCoordToCheckPS, NPCoordToCheckMorph)

        print("Max distance between the nodes of the morphed and PS models of AF and NP are:")
        print("")
        print("AF max distance, average distance, median distance: " +
            str(distAF), str(avgAF), str(medianAF))
        print("NP max distance, average distance, median distance: " +
            str(distNP), str(avgNP), str(medianNP))
        print("")

        #-----------------------------------------------------------------------
        # normalization

        valRef = (scaleFactor - 1.0) * 100.0
        errorPercentageAF = (medianAF*valRef)/medianAFscale
        errorPercentageNP = (medianNP*valRef)/medianNPscale

        print("error percentage of the AF external surface: " +
            str(errorPercentageAF) + "%")
        print("error percentage of the NP external surface: " +
            str(errorPercentageNP) + "%")
        print("")

        # writing the results in a file
        header = "distAFscale, avgAFscale, medianAFscale, distNPscale, avgNPscale, medianNPscale, distAF, avgAF, medianAF, distNP, avgNP, medianNP, errorPercentageAF, errorPercentageNP"

        with open(pathCompleted + "/" + outPutFileEuclidean, "w") as filenodesOn3dOut:
            filenodesOn3dOut.write(header + "\n")
            filenodesOn3dOut.write(str(distAFscale) + ',' + str(avgAFscale) + ',' + str(medianAFscale) + ',' + str(distNPscale) + ',' + str(avgNPscale) + ',' + str(medianNPscale) + ',' + str(
                distAF) + ',' + str(avgAF) + ',' + str(medianAF) + ',' + str(distNP) + ',' + str(avgNP) + ',' + str(medianNP) + ',' + str(errorPercentageAF) + ',' + str(errorPercentageNP))

    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    print("the file " + outPutFileEuclidean +
        " has been created in the folder " + pathCompleted)
    print("")
    print("end of the program...")
    print("")



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# define functions for rigid and non-rigid registrations

# Rigid

def defFuncRigid(targetFile, sourceFile, outPutFileName, nLoops, lenTarget, lenSource):

    nLoops = str(nLoops)
    lenTarget = str(lenTarget)
    lenSource = str(lenSource)

    if int(lenTarget) == int(lenSource):
        funcBCPD = ["bcpd", "-x", targetFile, "-y", sourceFile, "-o", outPutFileName, "-l", "1e9", "-b", "2.0", "-w", "0.1", "-J", "300", "-K", "70",
                    "-p", "-d", "5", "-e", "0.3", "-f", "0.3", "-g", "3", "-c", "1e-15", "-n", nLoops, "-ux", "-Db," + lenTarget + ",1", "-L", "300", "-sY"]
    else:
        funcBCPD = ["bcpd", "-x", targetFile, "-y", sourceFile, "-o", outPutFileName, "-l", "1e9", "-b", "2.0", "-w", "0.1", "-J", "300", "-K", "70", "-p", "-d",
                    "5", "-e", "0.3", "-f", "0.3", "-g", "3", "-c", "1e-15", "-n", nLoops, "-ux", "-Dx," + lenTarget + ",1", "-Dy," + lenSource + ",1", "-L", "300", "-sY"]

    return funcBCPD


# non-Rigid
def defFuncNonRigid(targetFile, sourceFile, outPutFileName, lambdaVal, betaVal, nLoops, lenTarget, lenSource):

    lambdaVal = str(lambdaVal)
    betaVal = str(betaVal)
    nLoops = str(nLoops)
    lenTarget = str(lenTarget)
    lenSource = str(lenSource)

    if int(lenTarget) == int(lenSource):
        funcBCPD = ["bcpd", "-x", targetFile, "-y", sourceFile, "-o", outPutFileName, "-l", lambdaVal, "-b", betaVal, "-w", "0.0000001", "-J", "300", "-K",
                    "70", "-p", "-d", "7", "-e", "0.15", "-f", "0.2", "-g", "0.1", "-c", "1e-15", "-n", nLoops, "-uy", "-Db," + lenTarget + ",1", "-L", "300", "-sY"]
    else:
        funcBCPD = ["bcpd", "-x", targetFile, "-y", sourceFile, "-o", outPutFileName, "-l", lambdaVal, "-b", betaVal, "-w", "0.0000001", "-J", "300", "-K", "70", "-p",
                    "-d", "7", "-e", "0.15", "-f", "0.2", "-g", "0.1", "-c", "1e-15", "-n", nLoops, "-uy", "-Dx," + lenTarget + ",1", "-Dy," + lenSource + ",1", "-L", "300", "-sY"]

    return funcBCPD

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# excecuting the BCPD registrations

# Rigid


def defRigid(nameMorph, numberIVD, patientID, funcRigid, outPutFileName, pathOut):
    print('-------------------------------------------------------------------------------')
    print("")
    print("Rigid registratio of the " + nameMorph +
          ": " + numberIVD + " " + patientID)
    print("")
    #print the bcpd function
    print(funcRigid)
    print("")
    morphingFunc = subprocess.run(funcRigid)
    print('-------------------------------------------------------------------------------')
    print(' ')
    #moving the temporal file to pathOut folder
    files = [filename for filename in os.listdir(
        '.') if filename.startswith(outPutFileName)]
    for filename in files:
        morphingFunc = subprocess.run(["mv", filename, pathOut])
    print("The rigid files of the " + nameMorph + " were move to: " + pathOut)
    print('')

# non-Rigid


def defNonRigid(nameMorph, numberIVD, patientID, funcNonRigid, outPutFileName, pathOut):
    print('-------------------------------------------------------------------------------')
    print("")
    print("Non-Rigid registratio of the " +
          nameMorph + ": " + numberIVD + " " + patientID)
    print("")
    print(funcNonRigid)
    print("")
    morphingFunc = subprocess.run(funcNonRigid)
    print('-------------------------------------------------------------------------------')
    print(' ')
    #moving the temporal file to pathOut folder
    files = [filename for filename in os.listdir(
        '.') if filename.startswith(outPutFileName)]
    for filename in files:
        morphingFunc = subprocess.run(["mv", filename, pathOut])
    print("The " + nameMorph + " files were move to: " + pathOut)
    print('')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# obtaining the coordinates of the node 71143 from the morphed file without indexing


def ObtainCentroid(fileIn, pathIn, nodes):
    print('-------------------------------------------------------------------------------')
    print("Obtaining the coordinates of the node 71143 of the morphed model")
    print("")

    nodesCoord = dict()

    with open(pathIn + "/" + fileIn, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        count = 0
        for row in reader:
            nodesCoord[nodes[count]] = row
            count += 1
    f.close()

    coordCentralNode = nodesCoord[71143]

    return coordCentralNode


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# creating inputs files (.inp)


def createInpFile(nameMorph, numberIVD, patientID, fileIn, fileOut, pathIn, pathOut, inpTemplatePath, nodes, stringFormat, coordCentralNode):
    print('-------------------------------------------------------------------------------')
    print("Creating " + nameMorph + " model in a .inp file of " +
          numberIVD + " " + patientID)
    print("")

    nodesCoord = dict()

    with open(pathIn + "/" + fileIn, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        count = 0
        for row in reader:
            nodesCoord[nodes[count]] = row
            count += 1
    f.close()

    # store the coordinates and the index in the dictionary nodesCoord and rest the value of coordCentralNode

    for key, value in nodesCoord.items():
        nodesCoord[key] = [float(value[0]) - float(coordCentralNode[0]), float(
            value[1]) - float(coordCentralNode[1]), float(value[2]) - float(coordCentralNode[2])]

    nodesOn3dFileOutPath = "./" + pathOut + "/" + fileOut

    with open(nodesOn3dFileOutPath, "w") as filenodesOn3dOut:
        with open(inpTemplatePath) as f:
            lines = f.readlines()
        count = 1
        for line in lines:
            if count == 10:
                for inode in sorted(nodes):
                    filenodesOn3dOut.write(
                        stringFormat.format(inode, *nodesCoord[inode]))
            filenodesOn3dOut.write(line)
            count += 1
    filenodesOn3dOut.close()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Cheking failed elements in the final .inp file


def checkFailedElem(outPutFileFailedElem, outPutFileMorphedIVD, pathInp, numberIVD, patientID, gap):

    nameDic = list()
    cwd = os.getcwd()
    nodesOn3dFileOutPath = cwd + "/" + pathInp + "/" + outPutFileMorphedIVD
    name = outPutFileMorphedIVD.split(".")[0]
    nameDic.append(nodesOn3dFileOutPath)
    nameDic.append(name)
    nameDicFile = numberIVD + '_' + patientID + '_' + 'nameDicFile.txt'

    lenFailedElem = int()

    with open(nameDicFile, "w") as filenameDicOut:
        for line in nameDic:
            filenameDicOut.write(line+'\n')
    filenameDicOut.close()

    #funcFailedElem = ['LANG=en_US.utf8 abaqus cae noGUI="failedElem.py"']
    funcFailedElem = ['abaqus', 'cae', 'noGUI={}'.format(
        cwd + "/sources/functions/failedElem.py"), '--', nameDicFile]

    print('-------------------------------------------------------------------------------')
    print("")
    print("Cheking if there are failed elements in " +
          numberIVD + " " + patientID)
    print("")
    print(funcFailedElem)
    print("")
    morphingFunc = subprocess.run(funcFailedElem)
    print("")

    lenFailedElem = int()

    with open(nameDicFile, "r") as filenodesOn3dOut:
        for line in filenodesOn3dOut:
            lenFailedElem = int(line)

    if lenFailedElem == 0:
        print("The .inp file doesn't have failed elements, it's ready to be simulated")

    elif lenFailedElem > 0:
        print("There are " + str(lenFailedElem) + " failed elements")
        print("the morphed process for the merged file need to be repeated")
    print('')

    morphingFunc = subprocess.run(["rm", nameDicFile])

    #file with the name of the inp file on the input folder that contains the number of failed elements and the gap value
    header = "NfailedElem, gap"

    with open(pathInp + "/" + outPutFileFailedElem, "w") as filenodesOn3dOut:
        filenodesOn3dOut.write(header + "\n")
        filenodesOn3dOut.write(str(lenFailedElem) + ',' + str(gap))

    return lenFailedElem

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Cheking the accuracy of the morphing process
# Hausdorff distance between 3D grids (Euclidean distance)


def bbox(array, point, radius):
    a = array[np.where(np.logical_and(
        array[:, 0] >= point[0] - radius, array[:, 0] <= point[0] + radius))]
    b = a[np.where(np.logical_and(a[:, 1] >= point[1] -
                   radius, a[:, 1] <= point[1] + radius))]
    c = b[np.where(np.logical_and(b[:, 2] >= point[2] -
                   radius, b[:, 2] <= point[2] + radius))]
    return c


def hausdorff(surface_a, surface_b):

    # Taking two arrays as input file, the function is searching for the Hausdorff distane of "surface_a" to "surface_b"
    dists = []

    l = len(surface_a)
    print("the model has " + str(l) + " nodes")
    print("")
    try:
        # Python 2
        xrange
    except NameError:
        # Python 3, xrange is now named range
        xrange = range

    for i in xrange(l):

        # walking through all the points of surface_a
        dist_min = 1000.0
        radius = 0
        b_mod = np.empty(shape=(0, 0, 0))

        # increasing the cube size around the point until the cube contains at least 1 point
        while b_mod.shape[0] == 0:
            b_mod = bbox(surface_b, surface_a[i], radius)
            radius += 0.5

        # to avoid getting false result (point is close to the edge, but along an axis another one is closer),
        # increasing the size of the cube
        b_mod = bbox(surface_b, surface_a[i], radius * math.sqrt(3))

        for j in range(len(b_mod)):
            # walking through the small number of points to find the minimum distance
            dist = np.linalg.norm(surface_a[i] - b_mod[j])
            if dist_min > dist:
                dist_min = dist

        dists.append(dist_min)

        maxDist = np.max(dists)
        avg = mean(dists)
        meanVal = median(dists)

    return maxDist, avg, meanVal
