@echo off
Rscript TimeSeparatelyLoaded.R 1>>./RunningTimeCmp/SeparatelyRunningTime.txt
Rscript TimeWholeLoaded.R 1>>./RunningTimeCmp/WholeRunningTime
