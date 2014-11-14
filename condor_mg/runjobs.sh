#!/bin/bash
#this script is run on condor; all paths must be absolute, preferably on /scratch 
#some of the commands in this script depend on environment variables. set them on local machine (i.e. do cmsenv),
# condor_submit will copy them to the condor node
outdir="/mnt/hscratch/snarayan/mc/monov_mg/Fall14_DR53X/"
#mgPath=/home/snarayan/scratch/condor/condor_mg/mg5.tar
mgPath=/home/snarayan/MG5_aMC_v2_1_2/bin/mg5_aMC

mv proc*dat proc_card_mg5.dat # making everything defaults
mv param*dat param_card.dat
mv run*dat run_card.dat


# the following is to make sure the correct python + libraries is loaded everywhere
scramdir=/scratch/snarayan/CMSSW_5_3_14/
cd ${scramdir}/src
eval `scramv1 runtime -sh`
cd -

val=$1
mgname=$2
outdir=${outdir}/${mgname}
workdir=/condor/execute/dir_$PPID/ # this should work - the directory created is specified by the condor job PID
echo $PATH
echo `which python`
echo `hostname`
echo "workdir: $workdir"
echo "val: $val"
echo "indir: $indir"
echo "args:    $*"

cd $workdir
sed -i s/output.*/output\ $mgname/ proc_card_mg5.dat # make sure the right output name
#sed -i s/.*iseed.*/\t${val}\t=\ iseed\t!\ rnd\ seed/ run_card.dat # change random seed in run_card, needed if multiple jobs
mkdir $mgname
#cp $mgPath .
#tar -xf mg5.tar
pwd
#MG5_aMC_v2_1_2/bin/mg5_aMC proc_card_mg5.dat
${mgPath} proc_card_mg5.dat
ls
echo "ls $mgname"
ls $mgname
pwd
cp *dat $mgname/Cards/
./$mgname/bin/generate_events

status=`echo $?`
echo "Status - $status"

mkdir -p $outdir
rm -rf $outdir/Events_${val} $outdir/Cards_${val}
gunzip ${mgname}/Events/run01/unweighted_events.lhe.gz
cp -r ${mgname}/Events $outdir/Events_${val}
cp -r ${mgname}/Cards $outdir/Cards_${val}
rm -r ${mgname}
exit $status
