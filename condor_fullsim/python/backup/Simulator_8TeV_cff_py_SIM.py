# Auto generated configuration file
# using: 
# Revision: 1.381.2.28 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProductions/python/EightTeV/Hadronizer_TuneZ2star_8TeV_madgraph_tauola_cff.py --step GEN,SIM --beamspot Realistic8TeVCollision --conditions START53_V7C::All --pileup NoPileUp --datamix NODATAMIXER --eventcontent RAWSIM --datatier GEN-SIM -n 10 --filein file:/afs/cern.ch/work/a/arapyan/public/DoublyChargedHiggsModel/mh800/Events/run_01/unweighted_events.lhe --customise Configuration/GenProductions/randomizeSeeds.randomizeSeeds --customise_commands process.source.skipEvents = cms.untracked.uint32(0)\nprocess.source.firstLuminosityBlock = cms.untracked.uint32(1) --fileout file:GEN_SIM_file.root
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
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    #fileNames = cms.untracked.vstring('file:/afs/cern.ch/work/a/arapyan/MCProd/MG5_aMC_v2_1_0/mhpp200/Events/run_02/unweighted_events.lhe')
#    fileNames = cms.untracked.vstring('file:/home/snarayan/scratch/2l_sample_manual/Events/unweighted_events.lhe')
    fileNames = cms.untracked.vstring('file:GEN_SIM_file_in.root')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.28 $'),
    annotation = cms.untracked.string('Configuration/GenProductions/python/EightTeV/Hadronizer_TuneZ2star_8TeV_madgraph_tauola_cff.py nevts:10'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('file:GEN_SIM_file.root'),
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
    comEnergy = cms.double(8000.0),
    UseExternalGenerators = cms.untracked.bool(True),
    PythiaParameters = cms.PSet(
        pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution'),
        processParameters = cms.vstring('MSEL=0         ! User defined processes', 
#            'IMSS(1) = 11    ! External SLHA file',
            'PMAS(5,1)=4.8   ! b quark mass', 
            'PMAS(6,1)=172.5 ! t quark mass', 
            'MSTJ(1)=0       ! Fragmentation/hadronization on or off', 
            'MSTP(61)=0      ! Parton showering on or off',
            'MSTP(71)=0      ! Parton showering on or off',
	    'MDME(190,1)=0      !W decay into dbar u',
	    'MDME(191,1)=0      !W decay into dbar c',
	    'MDME(192,1)=0      !W decay into dbar t',
	    'MDME(194,1)=0      !W decay into sbar u',
	    'MDME(195,1)=0      !W decay into sbar c',
	    'MDME(196,1)=0      !W decay into sbar t',
	    'MDME(198,1)=0      !W decay into bbar u',
	    'MDME(199,1)=0      !W decay into bbar c',
	    'MDME(200,1)=0      !W decay into bbar t',
	    'MDME(206,1)=0      !W decay into e+ nu_e',
	    'MDME(207,1)=0      !W decay into mu+ nu_mu',
	    'MDME(208,1)=0      !W decay into tau+ nu_tau'),
      #  SLHAParameters = cms.vstring('SLHAFILE = GeneratorInterface/Pythia6Interface/data/test.slha'),
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    ),
    jetMatching = cms.untracked.PSet(
       scheme = cms.string("Madgraph"),
       mode = cms.string("auto"),	# soup, or "inclusive" / "exclusive"
       MEMAIN_nqmatch = cms.int32(5),
       MEMAIN_etaclmax = cms.double(5.0),
       MEMAIN_minjets = cms.int32(0),
       MEMAIN_maxjets = cms.int32(3),
       MEMAIN_qcut = cms.double(30),
       MEMAIN_showerkt = cms.double(0),   
       MEMAIN_excres = cms.string(""),
       outTree_flag = cms.int32(0)    
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
process.source.firstLuminosityBlock = cms.untracked.uint32(1)
