import FWCore.ParameterSet.Config as cms

from L1Trigger.L1IntegratedMuonTrigger.RPCChamberMasker_cfi import RPCChamberMasker

#def appendChamberMaskerAtUnpacking(process, doDigis, doTrigger, chambRegEx):
def appendRPCChamberMaskerAtUnpacking(process, doDigis, maskedRPCs):

    if doDigis and hasattr(process,'muonRPCDigis') :

        print "[appendChamberMasker] : Found muonRPCDigis, applying filter"

        process.preRPCDigis = process.muonRPCDigis.clone()
        process.muonRPCDigis = RPCChamberMasker.clone()
#        if len(chambRegEx) > 0 :
#            process.muonDTDigis.maskedChRegEx = chambRegEx
#        process.filteredDigiSequence = cms.Sequence(process.preRPCDigis + process.muonRPCDigis)
        if len(maskedRPCs) > 0 :
		process.muonRPCDigis.maskedRPCIDs = maskedRPCs
	process.filteredRPCDigiSequence = cms.Sequence(process.preRPCDigis + process.muonRPCDigis)
#        process.RawToDigi.replace(process.muonRPCDigis, process.filteredDigiSequence)
        process.RawToDigi.replace(process.muonRPCDigis, process.filteredRPCDigiSequence)

