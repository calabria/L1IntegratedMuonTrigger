# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --filein file:BPH-Phys14DR-00003_step1.root --fileout file:BPH-Phys14DR-00003_step2.root --mc --eventcontent AODSIM,DQM,RECOSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM,DQMIO,RECO --conditions PHYS14_25_V1 --step RAW2DIGI,L1Reco,RECO,EI,DQM:DQMOfflinePOGMC --magField 38T_PostLS1 --python_filename /afs/cern.ch/cms/PPD/PdmV/work/McM/submit/BPH-Phys14DR-00003/BPH-Phys14DR-00003_2_cfg.py --no_exec -n 38
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('CommonTools.ParticleFlow.EITopPAG_cff')
process.load('DQMOffline.Configuration.DQMOfflineMC_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(38)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    #fileNames = cms.untracked.vstring('root://xrootd.ba.infn.it//store/mc/Phys14DR/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/GEN-SIM-RAW/PU20bx25_tsg_PHYS14_25_V1-v1/00000/18AEDFF5-9B6E-E411-8D4D-00266CFFA1E4.root')
    #fileNames = cms.untracked.vstring('root://xrootd.unl.edu//store/mc/Phys14DR/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/GEN-SIM-RAW/PU20bx25_tsg_PHYS14_25_V1-v1/00000/18AEDFF5-9B6E-E411-8D4D-00266CFFA1E4.root')
    fileNames = cms.untracked.vstring('root://xrootd.unl.edu//store/mc/Phys14DR/DYToMuMu_M-50_Tune4C_13TeV-pythia8/GEN-SIM-RAW/PU20bx25_tsg_castor_PHYS14_25_V1-v1/10000/044B58B4-9D75-E411-AB6C-002590A83218.root')
   #fileNames = cms.untracked.vstring('file:///tmp/gcodispo/044B58B4-9D75-E411-AB6C-002590A83218.root')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('step2 nevts:38'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionLevel = cms.untracked.int32(4),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands = process.AODSIMEventContent.outputCommands,
    fileName = cms.untracked.string('file:BPH-Phys14DR-00003_step2.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('AODSIM')
    )
)

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    splitLevel = cms.untracked.int32(0),
    outputCommands = process.DQMEventContent.outputCommands,
    fileName = cms.untracked.string('file:BPH-Phys14DR-00003_step2_inDQM.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('DQMIO')
    )
)

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    fileName = cms.untracked.string('file:BPH-Phys14DR-00003_step2_inRECOSIM.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('RECO')
    )
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'PHYS14_25_V1', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.eventinterpretaion_step = cms.Path(process.EIsequence)
process.dqmoffline_step = cms.Path(process.DQMOfflinePOGMC)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.eventinterpretaion_step,process.dqmoffline_step,process.AODSIMoutput_step,process.DQMoutput_step,process.RECOSIMoutput_step)

# customisation of the process.


# Adding chamber mask
from L1Trigger.L1IntegratedMuonTrigger.DTChamberMasker_cff import *
appendChamberMaskerAtUnpacking(process,True,True,["WH0_ST1_SEC1",
                                                  "WH0_ST2_SEC1",
                                                  "WH0_ST3_SEC1",
                                                  "WH0_ST4_SEC1",
                                                  "WH0_ST1_SEC2",
                                                  "WH0_ST2_SEC2",
                                                  "WH0_ST3_SEC2",
                                                  "WH0_ST4_SEC2",
                                                  "WH0_ST1_SEC3",
                                                  "WH0_ST2_SEC3",
                                                  "WH0_ST3_SEC3",
                                                  "WH0_ST4_SEC3",
                                                  "WH0_ST1_SEC4",
                                                  "WH0_ST2_SEC4",
                                                  "WH0_ST3_SEC4",
                                                  "WH0_ST4_SEC4",
                                                  "WH0_ST1_SEC5",
                                                  "WH0_ST2_SEC5",
                                                  "WH0_ST3_SEC5",
                                                  "WH0_ST4_SEC5",
                                                  "WH0_ST1_SEC6",
                                                  "WH0_ST2_SEC6",
                                                  "WH0_ST3_SEC6",
                                                  "WH0_ST4_SEC6",
                                                  "WH0_ST1_SEC7",
                                                  "WH0_ST2_SEC7",
                                                  "WH0_ST3_SEC7",
                                                  "WH0_ST4_SEC7",
                                                  "WH0_ST1_SEC8",
                                                  "WH0_ST2_SEC8",
                                                  "WH0_ST3_SEC8",
                                                  "WH0_ST4_SEC8",
                                                  "WH0_ST1_SEC9",
                                                  "WH0_ST2_SEC9",
                                                  "WH0_ST3_SEC9",
                                                  "WH0_ST4_SEC9",
                                                  "WH0_ST1_SEC10",
                                                  "WH0_ST2_SEC10",
                                                  "WH0_ST3_SEC10",
                                                  "WH0_ST4_SEC10",
                                                  "WH0_ST1_SEC11",
                                                  "WH0_ST2_SEC11",
                                                  "WH0_ST3_SEC11",
                                                  "WH0_ST4_SEC11",
                                                  "WH0_ST1_SEC12",
                                                  "WH0_ST2_SEC12",
                                                  "WH0_ST3_SEC12",
                                                  "WH0_ST4_SEC12" ])

reRunDttf( process )


# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

#process.AODSIMoutput.outputCommands.extend(['keep *dttfDigis*'])

# End of customisation functions

f = file("debug_mask.cfg", 'w')
f.write(process.dumpPython())
f.close()

