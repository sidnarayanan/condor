#!/bin/bash

condor_rm snarayan

./submit.sh 100 D5 constructive

./submit.sh 50 D5 constructive

./submit.sh 50 D8 constructive

./submit.sh 100 D8 constructive


