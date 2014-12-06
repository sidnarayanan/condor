#!/bin/bash

mass=$1
op=$2
interference=$3
process=$4
mgname="DMChiChibar_MonoW_mChi${mass}_${op}_${interference}_8TeV_madgraph"

echo "Executable  = runjobs.sh" > submit.condor
echo 'Requirements = OpSysAndVer == "SL5"' >>submit.condor
echo "Universe  = vanilla" >> submit.condor
echo 'Error = /scratch/snarayan/condor/condor_fullsim/logs/'${mass}'_'${op}'_'$process'.err' >> submit.condor
echo 'Output  = /scratch/snarayan/condor/condor_fullsim/logs/'${mass}'_'${op}'_'$process'.out' >> submit.condor
echo 'Log = /scratch/snarayan/condor/condor_fullsim/logs/'${mass}'_'${op}'_'$process'.log' >> submit.condor
echo 'Input = /dev/null' >> submit.condor
echo 'GetEnv = True' >> submit.condor
echo 'Arguments = "'$process' '${mgname}'"' >> submit.condor
echo 'Queue 1' >> submit.condor

condor_submit submit.condor
