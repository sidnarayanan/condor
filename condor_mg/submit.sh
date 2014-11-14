#!/bin/bash

mass=$1
op=$2
interference=$3
mgname="DMChiChibar_MonoW_mChi${mass}_${op}_${interference}_8TeV_madgraph"

echo "Executable  = runjobs.sh" > submit.condor
echo "Universe  = vanilla" >> submit.condor
echo 'Error = /scratch/snarayan/condor/condor_mg/logs/'${mgname}'.err' >> submit.condor
echo 'Output  = /scratch/snarayan/condor/condor_mg/logs/'${mgname}'.out' >> submit.condor
echo 'Log = /scratch/snarayan/condor/condor_mg/logs/'${mgname}'.log' >> submit.condor
echo 'Input = /dev/null' >> submit.condor
echo 'GetEnv = True' >> submit.condor
echo 'Arguments = "$(Process) '${mgname}'"' >> submit.condor
echo 'should_transfer_files = YES' >> submit.condor
echo 'when_to_transfer_output = ON_EXIT_OR_EVICT' >> submit.condor
cp cards/proc_card_mg5_${op}.dat . ; cp cards/run_card.dat . ; cp cards/param_card_mDM${mass}_${interference}.dat .
echo "transfer_input_files = proc_card_mg5_${op}.dat,run_card.dat,param_card_mDM${mass}_${interference}.dat" >> submit.condor
echo '+AccountingGroup = "group_cmsuser.snarayan"' >> submit.condor
echo 'Queue 1' >> submit.condor

#condor_submit submit.condor
