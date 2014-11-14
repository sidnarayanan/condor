# Auto generated configuration file
# using: 
# Revision: 1.381.2.28 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProductions/python/FourteenTeV/Hadronizer_TuneZ2star_14TeV_madgraph_tauola_cff.py --step GEN,SIM --beamspot Realistic8TeVCollision --conditions START53_V7C::All --pileup NoPileUp --datamix NODATAMIXER --eventcontent RAWSIM --datatier GEN-SIM -n 100 --filein file:test.lhe --customise Configuration/GenProductions/randomizeSeeds.randomizeSeeds --customise_commands process.source.skipEvents = cms.untracked.uint32(100)
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5)
)

# Input source
process.source = cms.Source("LHESource",
    fileNames = cms.untracked.vstring('file:/afs/cern.ch/work/a/arapyan/public/mad5hhlhefiles/mg41lam/hh14comp_events.lhe')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.28 $'),
    annotation = cms.untracked.string('Configuration/GenProductions/python/FourteenTeV/Hadronizer_TuneZ2star_14TeV_madgraph_tauola_cff.py nevts:100'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('Hadronizer_TuneZ2star_14TeV_madgraph_tauola_cff_py_GEN_SIM.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'START53_V7C::All', '')

process.generator = cms.EDFilter("Pythia6HadronizerFilter",
    ExternalDecays = cms.PSet(
        Tauola = cms.untracked.PSet(
            UseTauolaPolarization = cms.bool(True),
            InputCards = cms.PSet(
                mdtau = cms.int32(0),
                pjak2 = cms.int32(0),
                pjak1 = cms.int32(0)
            )
        ),
        parameterSets = cms.vstring('Tauola')
    ),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(True),
    comEnergy = cms.double(14000.0),
    UseExternalGenerators = cms.untracked.bool(True),
    PythiaParameters = cms.PSet(
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
            'MDME(210,1)=0  ! Higgs(h) decay                            ', 
            'MDME(211,1)=0  ! Higgs(h) decay                            ', 
            'MDME(212,1)=0  ! Higgs(h) decay                            ', 
            'MDME(213,1)=0  ! Higgs(h) decay                            ', 
            'MDME(214,1)=4  ! Higgs(h) decay   b b_bar                  ', 
            'MDME(215,1)=0  ! Higgs(h) decay                            ', 
            'MDME(216,1)=0  ! Higgs(h) decay                            ', 
            'MDME(217,1)=0  ! Higgs(h) decay                            ', 
            'MDME(218,1)=0  ! Higgs(h) decay                            ', 
            'MDME(219,1)=0  ! Higgs(h) decay                            ', 
            'MDME(220,1)=5  ! Higgs(h) decay   tau tau                  ', 
            'MDME(221,1)=0  ! Higgs(h) decay                            ', 
            'MDME(222,1)=0  ! Higgs(h) decay                            ', 
            'MDME(223,1)=0  ! Higgs(h) decay                            ', 
            'MDME(224,1)=0  ! Higgs(h) decay                            ', 
            'MDME(225,1)=0  ! Higgs(h) decay                            ', 
            'MDME(226,1)=0  ! Higgs(h) decay                            ', 
            'MDME(227,1)=0  ! Higgs(h) decay                            ', 
            'MDME(228,1)=0  ! Higgs(h) decay                            ', 
            'MDME(229,1)=0  ! Higgs(h) decay                            ', 
            'MDME(230,1)=0  ! Higgs(h) decay                            ', 
            'MDME(231,1)=0  ! Higgs(h) decay                            ', 
            'MDME(232,1)=0  ! Higgs(h) decay                            ', 
            'MDME(233,1)=0  ! Higgs(h) decay                            ', 
            'MDME(234,1)=0  ! Higgs(h) decay                            ', 
            'MDME(235,1)=0  ! Higgs(h) decay                            ', 
            'MDME(236,1)=0  ! Higgs(h) decay                            ', 
            'MDME(237,1)=0  ! Higgs(h) decay                            ', 
            'MDME(238,1)=0  ! Higgs(h) decay                            ', 
            'MDME(239,1)=0  ! Higgs(h) decay                            ', 
            'MDME(240,1)=0  ! Higgs(h) decay                            ', 
            'MDME(241,1)=0  ! Higgs(h) decay                            ', 
            'MDME(242,1)=0  ! Higgs(h) decay                            ', 
            'MDME(243,1)=0  ! Higgs(h) decay                            ', 
            'MDME(244,1)=0  ! Higgs(h) decay                            ', 
            'MDME(245,1)=0  ! Higgs(h) decay                            ', 
            'MDME(246,1)=0  ! Higgs(h) decay                            ', 
            'MDME(247,1)=0  ! Higgs(h) decay                            ', 
            'MDME(248,1)=0  ! Higgs(h) decay                            ', 
            'MDME(249,1)=0  ! Higgs(h) decay                            ', 
            'MDME(250,1)=0  ! Higgs(h) decay                            ', 
            'MDME(251,1)=0  ! Higgs(h) decay                            ', 
            'MDME(252,1)=0  ! Higgs(h) decay                            ', 
            'MDME(253,1)=0  ! Higgs(h) decay                            ', 
            'MDME(254,1)=0  ! Higgs(h) decay                            ', 
            'MDME(255,1)=0  ! Higgs(h) decay                            ', 
            'MDME(256,1)=0  ! Higgs(h) decay                            ', 
            'MDME(257,1)=0  ! Higgs(h) decay                            ', 
            'MDME(258,1)=0  ! Higgs(h) decay                            ', 
            'MDME(259,1)=0  ! Higgs(h) decay                            ', 
            'MDME(260,1)=0  ! Higgs(h) decay                            ', 
            'MDME(261,1)=0  ! Higgs(h) decay                            ', 
            'MDME(262,1)=0  ! Higgs(h) decay                            ', 
            'MDME(263,1)=0  ! Higgs(h) decay                            ', 
            'MDME(264,1)=0  ! Higgs(h) decay                            ', 
            'MDME(265,1)=0  ! Higgs(h) decay                            ', 
            'MDME(266,1)=0  ! Higgs(h) decay                            ', 
            'MDME(267,1)=0  ! Higgs(h) decay                            ', 
            'MDME(268,1)=0  ! Higgs(h) decay                            ', 
            'MDME(269,1)=0  ! Higgs(h) decay                            ', 
            'MDME(270,1)=0  ! Higgs(h) decay                            ', 
            'MDME(271,1)=0  ! Higgs(h) decay                            ', 
            'MDME(272,1)=0  ! Higgs(h) decay                            ', 
            'MDME(273,1)=0  ! Higgs(h) decay                            ', 
            'MDME(274,1)=0  ! Higgs(h) decay                            ', 
            'MDME(275,1)=0  ! Higgs(h) decay                            ', 
            'MDME(276,1)=0  ! Higgs(h) decay                            ', 
            'MDME(277,1)=0  ! Higgs(h) decay                            ', 
            'MDME(278,1)=0  ! Higgs(h) decay                            ', 
            'MDME(279,1)=0  ! Higgs(h) decay                            ', 
            'MDME(280,1)=0  ! Higgs(h) decay                            ', 
            'MDME(281,1)=0  ! Higgs(h) decay                            ', 
            'MDME(282,1)=0  ! Higgs(h) decay                            ', 
            'MDME(283,1)=0  ! Higgs(h) decay                            ', 
            'MDME(284,1)=0  ! Higgs(h) decay                            ', 
            'MDME(285,1)=0  ! Higgs(h) decay                            ', 
            'MDME(286,1)=0  ! Higgs(h) decay                            ', 
            'MDME(287,1)=0  ! Higgs(h) decay                            ', 
            'MDME(288,1)=0  ! Higgs(h) decay                            '),
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
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from Configuration.GenProductions.randomizeSeeds
from Configuration.GenProductions.randomizeSeeds import randomizeSeeds 

#call to customisation function randomizeSeeds imported from Configuration.GenProductions.randomizeSeeds
process = randomizeSeeds(process)

# End of customisation functions

# Customisation from command line
process.source.skipEvents = cms.untracked.uint32(0)
