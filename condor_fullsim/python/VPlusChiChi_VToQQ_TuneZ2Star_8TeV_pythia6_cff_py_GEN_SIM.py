# Auto generated configuration file
# using: 
# Revision: 1.381.2.28 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: Configuration/Generator/python/H_test_8TeV_cfi.py --mc -s GEN,SIM --beamspot Realistic8TeVCollision --conditions START53_V19::All --pileup NoPileUp --datamix NODATAMIXER --eventcontent RAWSIM --datatier GEN-SIM -n 300 --filein file:unweighted_events.lhe --customise Configuration/GenProductions/randomizeSeeds.randomizeSeeds --fileout file:GEN_SIM_file.root --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('GEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
# process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
# process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("LHESource",
    fileNames = cms.untracked.vstring('file:events.lhe')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.28 $'),
    annotation = cms.untracked.string('Configuration/Generator/python/Hadronizer_MgmMatchTuneZ2star_8TeV_madgraph_cff.py nevts:300'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('file:decayed.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:mc', '')
# process.GlobalTag = GlobalTag(process.GlobalTag, 'START53_V19::All', '')
# from Configuration.Generator.PythiaUEZ2starSettings_cfi import *

process.generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(True),
    comEnergy = cms.double(8000.0),
    crossSection = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    PythiaParameters = cms.PSet(
        # pythiaUESettingsBlock,
        pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution', 
            'MSTJ(22)=2     ! Decay those unstable particles', 
            'PARJ(71)=10 .  ! for which ctau  10 mm', 
            'MSTP(33)=0     ! no K factors in hard cross sections', 
            'MSTP(2)=1      ! which order running alphaS', 
            'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)', 
            'MSTP(52)=2     ! work with LHAPDF', 
            'PARP(82)=1.921 ! pt cutoff for multiparton interactions', 
            'PARP(89)=1800. ! sqrts for which PARP82 is set', 
            'PARP(90)=0.227 ! Multiple interactions: rescaling power', 
            'MSTP(95)=6     ! CR (color reconnection parameters)', 
            'PARP(77)=1.016 ! CR', 
            'PARP(78)=0.538 ! CR', 
            'PARP(80)=0.1   ! Prob. colored parton from BBR', 
            'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter', 
            'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter', 
            'PARP(62)=1.025 ! ISR cutoff', 
            'MSTP(91)=1     ! Gaussian primordial kT', 
            'PARP(93)=10.0  ! primordial kT-max', 
            'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default', 
            'MSTP(82)=4     ! Defines the multi-parton model'),
        processParameters = cms.vstring('MSEL=0         ! User defined processes', 
            'PMAS(5,1)=4.8   ! b quark mass', 
            'PMAS(6,1)=172.5 ! t quark mass', 
            'MSTJ(1)=1       ! Fragmentation/hadronization on or off', 
            'MSTP(61)=1      ! Parton showering on or off',
            'MDME(190,1)=1      !W decay into dbar u',
            'MDME(191,1)=1      !W decay into dbar c',
            'MDME(192,1)=1      !W decay into dbar t',
            'MDME(194,1)=1      !W decay into sbar u',
            'MDME(195,1)=1      !W decay into sbar c',
            'MDME(196,1)=1      !W decay into sbar t',
            'MDME(198,1)=1      !W decay into bbar u',
            'MDME(199,1)=1      !W decay into bbar c',
            'MDME(200,1)=1      !W decay into bbar t',
            'MDME(206,1)=0      !W decay into e+ nu_e',
            'MDME(207,1)=0      !W decay into mu+ nu_mu',
            'MDME(208,1)=0      !W decay into tau+ nu_tau',
            'MDME(174,1)=1            !Z decay into d dbar',
            'MDME(175,1)=1            !Z decay into u ubar',
            'MDME(176,1)=1            !Z decay into s sbar',
            'MDME(177,1)=1            !Z decay into c cbar',
            'MDME(178,1)=1            !Z decay into b bbar',
            'MDME(179,1)=1            !Z decay into t tbar',
            'MDME(182,1)=0            !Z decay into e- e+',
            'MDME(183,1)=0            !Z decay into nu_e nu_ebar',
            'MDME(184,1)=0            !Z decay into mu- mu+',
            'MDME(185,1)=0            !Z decay into nu_mu nu_mubar',
            'MDME(186,1)=0            !Z decay into tau- tau+',
            'MDME(187,1)=0            !Z decay into nu_tau nu_taubar'),
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)

# customisation of the process.
for path in process.paths:
    getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# Automatic addition of the customisation function from Configuration.GenProductions.randomizeSeeds
from Configuration.GenProductions.randomizeSeeds import randomizeSeeds 

#call to customisation function randomizeSeeds imported from Configuration.GenProductions.randomizeSeeds
process = randomizeSeeds(process)

# Customisation from command line
process.source.skipEvents = cms.untracked.uint32(0)
process.source.firstLuminosityBlock = cms.untracked.uint32(1)

# End of customisation functions


