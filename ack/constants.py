#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Channels:
    NucleusSegmentation = "nucleus_segmentation"
    MembraneSegmentation = "membrane_segmentation"
    DNA = "dna"
    Membrane = "membrane"
    Structure = "structure"
    Brightfield = "brightfield"
    DefaultOrderList = [
        NucleusSegmentation,
        MembraneSegmentation,
        DNA,
        Membrane,
        Structure,
        Brightfield,
    ]


class DatasetFields:
    CellId = "CellId"
    CellIndex = "CellIndex"
    FOVId = "FOVId"
    SourceReadPath = "SourceReadPath"
    NucleusSegmentationReadPath = "NucleusSegmentationReadPath"
    MembraneSegmentationReadPath = "MembraneSegmentationReadPath"
    ChannelIndexDNA = "ChannelIndexDNA"
    ChannelIndexMembrane = "ChannelIndexMembrane"
    ChannelIndexStructure = "ChannelIndexStructure"
    ChannelIndexBrightfield = "ChannelIndexBrightfield"
    StandardizedFOVPath = "StandardizedFOVPath"
    CellFeaturesPath = "CellFeaturesPath"
    AllExpectedInputs = [
        CellId,
        CellIndex,
        FOVId,
        SourceReadPath,
        NucleusSegmentationReadPath,
        MembraneSegmentationReadPath,
        ChannelIndexDNA,
        ChannelIndexMembrane,
        ChannelIndexStructure,
        ChannelIndexBrightfield,
    ]
