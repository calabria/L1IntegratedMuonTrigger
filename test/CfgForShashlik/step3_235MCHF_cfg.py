# Auto generated configuration file
# using:
# Revision: 1.20
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step3 --filein file:HIG-TP2023HGCALDR-00029_step1.root --fileout file:HIG-TP2023HGCALDR-00029.root --pileup_input dbs:/MinBias_TuneZ2star_14TeV-pythia6/TP2023HGCALGS-DES23_62_V1-v3/GEN-SIM --mc --eventcontent RECOSIM --pileup AVE_140_BX_25ns --customise RecoParticleFlow/PandoraTranslator/customizeHGCalPandora_cff.cust_2023HGCalPandoraMuon,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RECO --conditions PH2_1K_FB_V6::All --step RAW2DIGI,L1Reco,RECO --magField 38T_PostLS1 --geometry Extended2023HGCalMuon,Extended2023HGCalMuonReco --python_filename step3_235MCHF_cfg.py --no_exec -n 1
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('Configuration.Geometry.GeometryExtended2023SHCalNoTaperReco_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
                                       input = cms.untracked.int32(-1)
                                       )

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring('file:/lustre/cms/store/group/upgrade/muon/RecoFolder/DYToMuMu_2023_2Step_2/DYToMuMu_M-20_TuneZ2star_14TeV-pythia6-tauola/calabria_DYToMuMu_GEN-SIM-DIGI-RAW_CMSSW_6_2_0_SLHC23patch1_2023Scenario_2Step_GEMSH2/75266629395cd3363487f66c667220a2/step2_1000_1_h9c.root')
)

process.options = cms.untracked.PSet(

)

#--------------------------------------------------------------------------

# CSC
# case 0  :: all detectors in
# case 1  :: ME1/1 switched off
# case 2  :: ME2/1 switched off
# case 3  :: ME3/1 switched off
# case 4  :: ME4/1 switched off
# default :: all detectors in

# RPC
# case 0  :: NO RPC Upgrade
# case 1  :: RE3/1 switched off
# case 2  :: RE4/1 switched off
# case 3  :: RPC Upgrade switched on
# default :: all detectors in

#GEM
# case 0  :: all detectors off
# case 1  :: GE1/1 switched on
# case 2  :: GE2/1 switched on
# case 3  :: all detectors in
# default :: all detectors in

process.load('RecoLocalMuon.RPCRecHit.rpcRecHits_cfi')
process.load('RecoLocalMuon.GEMRecHit.gemRecHits_cfi')
process.load('RecoLocalMuon.CSCRecHitD.cscRecHitD_cfi')

#235 MCHF: RE3/1 + RE4/1 switched off
process.csc2DRecHits.stationToUse = cms.untracked.int32(0)
process.rpcRecHits.recAlgoConfig.stationToUse = cms.untracked.int32(0)
process.gemRecHits.recAlgoConfig.stationToUse = cms.untracked.int32(3)

#--------------------------------------------------------------------------

# Production Info
process.configurationMetadata = cms.untracked.PSet(
                                                   version = cms.untracked.string('$Revision: 1.20 $'),
                                                   annotation = cms.untracked.string('step3 nevts:1'),
                                                   name = cms.untracked.string('Applications')
                                                   )

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
                                         splitLevel = cms.untracked.int32(0),
                                         eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
                                         outputCommands = process.RECOSIMEventContent.outputCommands,
                                         fileName = cms.untracked.string('step3.root'),
                                         dataset = cms.untracked.PSet(
                                                                      filterName = cms.untracked.string(''),
                                                                      dataTier = cms.untracked.string('GEN-SIM-RECO')
                                                                      )
                                         )

# Additional output definition

# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(140.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-12)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring(['/store/mc/TP2023SHCALGS/MinBias_TuneZ2star_14TeV-pythia6/GEN-SIM/DES23_62_V1-v1/00000/0001C125-E46B-E411-B05A-0026B92779BD.root', '/store/mc/TP2023SHCALGS/MinBias_TuneZ2star_14TeV-pythia6/GEN-SIM/DES23_62_V1-v1/00000/00156B8D-E66B-E411-892A-001E6739AD61.root', '/store/mc/TP2023SHCALGS/MinBias_TuneZ2star_14TeV-pythia6/GEN-SIM/DES23_62_V1-v1/00000/00355596-286C-E411-8929-001CC416C686.root', '/store/mc/TP2023SHCALGS/MinBias_TuneZ2star_14TeV-pythia6/GEN-SIM/DES23_62_V1-v1/00000/004FC0E7-876D-E411-973B-AC853D9DAC29.root', '/store/mc/TP2023SHCALGS/MinBias_TuneZ2star_14TeV-pythia6/GEN-SIM/DES23_62_V1-v1/00000/0089DCA0-476C-E411-A4C2-00221923172A.root', '/store/mc/TP2023SHCALGS/MinBias_TuneZ2star_14TeV-pythia6/GEN-SIM/DES23_62_V1-v1/00000/00CC120E-E46B-E411-AA8E-0023AEFDE9DC.root', '/store/mc/TP2023SHCALGS/MinBias_TuneZ2star_14TeV-pythia6/GEN-SIM/DES23_62_V1-v1/00000/024A3620-2E6C-E411-98BC-001E67248142.root', '/store/mc/TP2023SHCALGS/MinBias_TuneZ2star_14TeV-pythia6/GEN-SIM/DES23_62_V1-v1/00000/041D11C5-B06C-E411-B729-0025904403AE.root', '/store/mc/TP2023SHCALGS/MinBias_TuneZ2star_14TeV-pythia6/GEN-SIM/DES23_62_V1-v1/00000/04814AAF-786D-E411-9E17-A0369F301924.root', '/store/mc/TP2023SHCALGS/MinBias_TuneZ2star_14TeV-pythia6/GEN-SIM/DES23_62_V1-v1/00000/04A93303-F76B-E411-AA23-D4AE526A05C8.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'PH2_1K_FB_V6::All', '')

#--------------------------------------------------------------------------
# CSC aging

process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    csc2DRecHitsOverload = cms.PSet(
        initialSeed = cms.untracked.uint32(81)
    ),
)

process.csc2DRecHitsOverload = cms.EDProducer('CFEBBufferOverloadProducer',
    cscRecHitTag = cms.InputTag("csc2DRecHits"),
    failureRate = cms.untracked.double(0.15),
    doUniformFailure = cms.untracked.bool(True),
    doCFEBFailure = cms.untracked.bool(True),
)

# change input to cscSegments
process.cscSegments.inputObjects = "csc2DRecHitsOverload"

process.csclocalreco.replace(process.cscSegments, process.csc2DRecHitsOverload)
process.csclocalreco += process.cscSegments

#--------------------------------------------------------------------------

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.RECOSIMoutput_step)

#--------------------------------------------------------------------------
# RPC aging

from L1Trigger.L1IntegratedMuonTrigger.DTChamberMasker_cff import *
from L1Trigger.L1IntegratedMuonTrigger.RPCChamberMasker_cff import *
appendRPCChamberMaskerAtUnpacking(process,True,[637570221,637602989,637635757,637569201,637634737,637571545,637571677,637637213,637567793,637600561,637633329,637566989,637632525,637566993,637632529,637569037,637634573,637571565,637637101,637571449,637636985,637572317,637637853,637568057,637600825,637633593,637568025,637633561,637567381,637632917,637571805,637637341,637569325,637602093,637634861,637572569,637638105,637571569,637637105,637567065,637632601,637570229,637635765,637567285,637600053,637632821,637572589,637638125,637571157,637636693,637570485,637636021,637571181,637636717,637567069,637632605,637570365,637603133,637635901,637570481,637636017,637572445,637637981,637567005,637632541,637567373,637632909,637568509,637634045,637569425,637634961,637572561,637638097,637568409,637633945,637571281,637636817,637569973,637635509,637567157,637599925,637632693,637571197,637636733,637571321,637636857,637570237,637603005,637635773,637569453,637602221,637634989,637569977,637635513,637568305,637601073,637633841,637570097,637635633,637570197,637635733,637569709,637602477,637635245,637571161,637636697,637572429,637637965,637567669,637600437,637633205,637572045,637637581,637568301,637633837,637567213,637632749,637567801,637600569,637633337,637568053,637600821,637633589,637570109,637602877,637635645,637567965,637633501,637567993,637633529,637637081,637571193,637636729,637567281,637600049,637632817,637567469,637633005,637567953,637633489,637568177,637600945,637633713])

reRunDttf( process )

#--------------------------------------------------------------------------

# customisation of the process.

# Automatic addition of the customisation function from RecoParticleFlow.PandoraTranslator.customizeHGCalPandora_cff
from SLHCUpgradeSimulations.Configuration.combinedCustoms import cust_2023SHCal

#call to customisation function cust_2023HGCalPandoraMuon imported from RecoParticleFlow.PandoraTranslator.customizeHGCalPandora_cff
process = cust_2023SHCal(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions
