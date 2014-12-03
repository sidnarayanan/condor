#!/bin/bash
#this script is run on condor; all paths must be absolute
nproc=$1
mname=$2
outputDir=/mnt/hscratch/snarayan/mc/monoJet_Simplified/Fall14_DR53X/${mname}/AODSIM/Summer12-PU_START53_V19_v2/
scramdir=/scratch1/snarayan/condor/condor_fullsim/CMSSW_5_3_14/ 
pythondir=${scramdir}../python/
workdir=/condor/execute/dir_$PPID/ # this should work - the directory created is specified by the condor job PID
#workdir=${PWD}/tmp # local testing
lhePath=/mnt/hscratch/snarayan/mc/monoJet_Simplified/Fall14_DR53X/${mname}/events.lhe
hostname
minbias=MinBias_8TeV_cfi_GEN_SIM.py
hadronizer=Hadronizer_JetPlusChiChi_TuneZ2Star_8TeV_pythia6_cff_py_GEN_SIM.py
gen=GEN-Fragment_DIGI_L1_DIGI2RAW_HLT_PU.py
reco=STEP2_RAW2DIGI_L1Reco_RECO.py


#careful to check that nevts * (number of jobs submitted in condor.submit - 1) < maxEvents
#also check that nevts matches that in Hadronizer*py and MinBias*py
nevts=300
let val=$nproc*$nevts+1
echo `hostname`
echo "workdir: $workdir"
echo "scramdir: $scramdir"
#echo "args:    $*"
echo "val: $val"

echo $scramdir
cd ${scramdir}/src
eval `scramv1 runtime -sh`
cd $workdir

cp ${pythondir}/$minbias  .
cp ${pythondir}/$hadronizer  .
sed -i -e 's?[\t\ ]*[^#]fileNames.*?\tfileNames = cms.untracked.vstring("file:'${lhePath}'")?' $hadronizer 
sed -i -e 's?process\.source\.skipEvents.*?process.source.skipEvents = cms.untracked.uint32('$val')?' $hadronizer
sed -i -e 's?process\.source\.firstLuminosityBlock.*?process.source.firstLuminosityBlock = cms.untracked.uint32('$val')?' $hadronizer
cp ${pythondir}/$gen .
cp ${pythondir}/$reco  .


# grep $val Hadronizer_TuneZ2star_8TeV_madgraph_tauola_cff_py_GEN_SIM.py

cmsRun $minbias
cmsRun $hadronizer
cmsRun $gen
cmsRun $reco

status=`echo $?`
echo "Status - $status"

mkdir -p ${outputDir}
mv STEP2_RAW2DIGI_L1Reco_RECO.root AODSIM_${nproc}.root
cp AODSIM_${nproc}.root  ${outputDir}
exit $status
