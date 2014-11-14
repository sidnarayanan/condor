#!/bin/bash
#this script is run on condor; all paths must be absolute, preferably on /scratch or /tmp
#some of the commands in this script depend on environment variables. set them on local machine,
# condor_submit will copy them to the condor node
indir=/mnt/hscratch/snarayan/mc/softl_signal/
scramdir=/scratch/snarayan/CMSSW_5_3_14/ #this location has the correct macros

nproc=$1
#careful to check that nbatch * (number of jobs submitted in condor.submit - 1) < maxEvents
nbatch=300
let val=$nproc*$nbatch+1
indir=${indir}${val}
workdir=/condor/execute/dir_$PPID/ # this should work - the directory created is specified by the condor job PID
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
cp /scratch/snarayan/root/.rootlogon.C  .
pwd
ls ${scramdir}/src/MitMonoJet/macros/
echo "root -b -l -q runBavantiBoostedV.C+\(\"${indir}/aod_${val}.root\"\)"
root -b -l -q runBavantiBoostedV.C+\("\"${indir}/aod_${val}.root\""\)

status=`echo $?`
echo "Status - $status"

#mkdir ${outputDir}_${val}
# cp hpp_mad_${val}.root   ${outputDir}_${val}
mv *root ${indir}
exit $status
