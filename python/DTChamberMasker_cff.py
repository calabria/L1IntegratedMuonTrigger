import FWCore.ParameterSet.Config as cms

from L1Trigger.L1IntegratedMuonTrigger.DTChamberMasker_cfi import DTChamberMasker

def appendChamberMaskerAtUnpacking(process, doDigis, doTrigger, chambRegEx):

    if doDigis and hasattr(process,'muonDTDigis') :

        print "[appendChamberMasker] : Found muonDTDigis, applying filter"

        process.preDtDigis = process.muonDTDigis.clone()
        process.muonDTDigis = DTChamberMasker.clone()
        if len(chambRegEx) > 0 :
            process.muonDTDigis.maskedChRegEx = chambRegEx
        process.muonDTDigis.triggerPrimPhTag = cms.InputTag('')
        process.muonDTDigis.triggerPrimThTag = cms.InputTag('')
        process.filteredDigiSequence = cms.Sequence(process.preDtDigis + process.muonDTDigis)
        process.RawToDigi.replace(process.muonDTDigis, process.filteredDigiSequence)

    if doDigis and hasattr(process,'dttfDigis') :

        print "[appendChamberMasker] : Found dttfDigis, applying filter"

        process.preDttfDigis = process.dttfDigis.clone()
        process.dttfDigis = DTChamberMasker.clone()
        if len(chambRegEx) > 0 :
            process.dttfDigis.maskedChRegEx = chambRegEx
        process.dttfDigis.digiTag = cms.InputTag('')
        process.filteredTrigSequence = cms.Sequence(process.preDttfDigis + process.dttfDigis)
        process.RawToDigi.replace(process.dttfDigis, process.filteredTrigSequence)

        
def reRunDttf( process ):

    #process.dttfDigisMasked = process.valDttfDigis.clone()
    #process.dttfDigisMasked.DTDigi_Source = cms.InputTag("muonDTDigis", "DT")
    #from L1Trigger.GlobalMuonTrigger.gmtDigis_cfi import gmtDigis
    #from L1Trigger.CSCTrackFinder.csctfTrackDigis_cfi import csctfTrackDigis
    process.load ( "L1Trigger.GlobalMuonTrigger.gmtDigis_cfi")
    process.load ( "L1Trigger.CSCTrackFinder.csctfTrackDigis_cfi")

    from L1Trigger.DTTrackFinder.dttfDigis_cfi import dttfDigis as dttfTrackFinder
    process.dttfTrackDigis = dttfTrackFinder.clone()
    process.dttfTrackDigis.DTDigi_Source = cms.InputTag("dttfDigis")
    if hasattr(process.dttfTrackDigis, 'DTDigi_Theta_Source'):
        process.dttfTrackDigis.DTDigi_Theta_Source = cms.InputTag("dttfDigis") 
    #process.csctfTrackDigis.SectorReceiverInput = cms.untracked.InputTag("simMuonCSCDigis")
    process.csctfTrackDigis.SectorReceiverInput = cms.untracked.InputTag("csctfDigis")
    process.csctfTrackDigis.DTproducer = cms.untracked.InputTag("dttfDigis")
    process.gmtDigis.DTCandidates = cms.InputTag("dttfTrackDigis","DT")
    process.gmtDigis.RPCbCandidates = cms.InputTag("gtDigis","RPCb")
    process.gmtDigis.RPCfCandidates = cms.InputTag("gtDigis","RPCf")
    process.gmtDigis.CSCCandidates  = cms.InputTag("gtDigis","CSC")
    process.RawToDigiL1MuonEmulator = cms.Sequence( process.RawToDigi
                                                    * process.csctfTrackDigis
                                                    * process.dttfTrackDigis
                                                    * process.gmtDigis )
    process.raw2digi_step.replace( process.RawToDigi, process.RawToDigiL1MuonEmulator )

    # process.ValL1MuTrackFinders.replace(process.valGmtDigis, process.gmtDigis)
    # process.ValL1Emulator.replace(process.valGmtDigis, process.gmtDigis)
    # process.gmtDigis.DTCandidates = cms.InputTag("dttfDigis", "DT")
    # process.l1compare.GMTsourceEmul = cms.InputTag("gmtDigis")
    # process.deGmt.replace(process.valGmtDigis, process.gmtDigis)
    process.RECOSIMoutput.outputCommands.extend( ['keep *_dttfDigis_*_*', 
                                                  'keep *_dttfTrackDigis_*_*', 
                                                  'keep *_gmtDigis_*_*'] )
    process.AODSIMoutput.outputCommands.extend( ['keep *_dttfDigis_*_*',
                                                  'keep *_dttfTrackDigis_*_*',
                                                  'keep *_gmtDigis_*_*'] )
