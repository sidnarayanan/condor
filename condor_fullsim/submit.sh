#!/bin/bash

mass=$1
op=$2
# interference=$3
mgname="DMChiChibar_MonoJet_mChi10_mMed${mass}_${op}_13TeV_mcfm"

echo "Executable  = runjobs.sh" > submit.condor
echo 'Requirements = OpSysAndVer == "SL6" && ARCH == "X86_64"' >>submit.condor
echo "Universe  = vanilla" >> submit.condor
echo 'Error = '${PWD}'/logs/'${mass}'_'${op}'_$(Process).err' >> submit.condor
echo 'Output  = '${PWD}'/logs/'${mass}'_'${op}'_$(Process).out' >> submit.condor
echo 'Log = '${PWD}'/logs/'${mass}'_'${op}'_$(Process).log' >> submit.condor
echo 'Input = /dev/null' >> submit.condor
echo 'GetEnv = True' >> submit.condor
echo 'Arguments = "$(Process) '${mgname}'"' >> submit.condor
echo '+AccountingGroup= "group_cmsuser.snarayan"' >> submit.condor
echo 'Queue 35' >> submit.condor


#condor_submit submit.condor
