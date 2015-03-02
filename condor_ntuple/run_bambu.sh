#!/bin/bash
#this script is run on condor; all paths must be absolute, preferably on /scratch or

indir=/mnt/hscratch/snarayan/mc/softl_signal/
scramdir=/scratch/snarayan/CMSSW_5_3_11/ 

nproc=$1
#careful to check that nbatch * (number of jobs submitted in condor.submit - 1) < maxEvents
nbatch=300
let val=$nproc*$nbatch+1
RECOPath = "/mnt/hscratch/snarayan/mc/monov_mg/constructive_-1/ChiChibarHadronicW_mChi100_D5_constructive/RECO_"${val}".root"
indir=${indir}${val}"/"
workdir=/condor/execute/dir_$PPID/
echo `hostname`
echo "workdir: $workdir"
echo "scramdir: $scramdir"
echo "val: $val"
echo "indir: $indir"
#echo "args:    $*"

cd ${scramdir}/src
eval `scramv1 runtime -sh`
cd $workdir
pwd
cp ${scramdir}/src/MitProd/Configuration/python/BAMBUProd_AODSIM.py .

sed -i -e 's?[\t\ ]*[^#]fileNames.*?\tfileNames = cms.untracked.vstring("file:'${RECOPath}'")?' BAMBUProd_AODSIM.py
# sed -i -e "33s/.*/   fileNames=cms.untracked.vstring('file:\/mnt\/hscratch\/snarayan\/mc\/monov_mg\/constructive_-1\/ChiChibarHadronicW_mChi100_D5_constructive\/RECO_"${val}".root')/" BAMBUProd_AODSIM.py

grep $val BAMBUProd_AODSIM.py

cmsRun BAMBUProd_AODSIM.py

status=`echo $?`
echo "Status - $status"

#mkdir ${outputDir}_${val}
# cp hpp_mad_${val}.root   ${outputDir}_${val}
mv XX*root ${indir}/Bambu_${val}.root
exit $status
