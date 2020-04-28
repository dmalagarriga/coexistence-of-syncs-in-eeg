#!/bin/bash
RED='\033[0;31m'
NC='\033[0m' # No Color
GREEN='\e[92m'
#### Used to study eyes closed eyes opened ####

printf "${RED}Computing cross-correlations....\n"
python -W ignore ./Analysis/eyes_opened_closed/correlationbo.py # This is only for Eyes closed and Eyes opened
printf "${GREEN}... done\n\n"

printf "${RED}Computing Phase-Locking value (PLV)....\n"
python -W ignore ./Analysis/eyes_opened_closed/PLV.py # This is only for Eyes closed and Eyes opened
printf "${GREEN}... done\n\n"

printf "${RED}Classification of sychronizations....\n"
python -W ignore ./Analysis/eyes_opened_closed/Classification_Synchronization_XCORR_PHASE_LAG.py # This is only for Eyes closed and Eyes opened
printf "${GREEN}..done\n\n"

printf "${RED}Constructing sychronization networks....\n"
python -W ignore ./Analysis/eyes_opened_closed/Construct_Network_From_Phase_XCorr_and_Lag.py # This is only for Eyes closed and Eyes opened
printf "${GREEN}... done!\n\n"

printf "${RED}Computing power spectra...\n"
python -W ignore ./Analysis/eyes_opened_closed/power_spectrum_computations.py
printf "...${GREEN}done.\n\n"

printf "${RED}Plotting the heat map of power spectra..\n"
python -W ignore ./Analysis/eyes_opened_closed/Compute_PSD_colormap_head.py
printf "..${GREEN}done!\n\n\n"

printf "${NC} done ALL!!\n"



#### Used to study Task_1 and Task_2 ####

#python -W ignore ./Analysis/task_1_task_2/correlation_fractioned.py
#python -W ignore ./Analysis/task_1_task_2/PLV_fractioned.py
#python -W ignore ./Analysis/task_1_task_2/Coherence_fractioned.py
#python -W ignore ./Analysis/task_1_task_2/Classification_Synchronization_XCORR_PHASE_LAG_fractioned.py
#python -W ignore ./Analysis/task_1_task_2/Construct_Network_From_Phase_XCorr_and_Lag_Coexistence_fractioned.py
#python -W ignore./Analysis/task_1_task_2/Construct_Network_From_Phase_XCorr_and_Lag_AVERAGE_Coexistence_fractioned.py

##### OPTIONALS ####
#python -W ignore ./Analysis/Make_movie.py
#python -W ignore ./Analysis/Compute_PSD_colormap_head.py


##################################################################################################################################
##################################################################################################################################

##### NOT USED IN THE DEMO #####

#python ./Analysis/read.py
#python ./Analysis/Degree_vs_Similarity_and_Poincare_Sections_All_in_One.py
#python ./Analysis/Histogram_2D_IPI.py
#python ./Analysis/correlation_fractioned.py
#python ./Analysis/PLV_fractioned.py
#python ./Analysis/coherence.py
#python ./Analysis/Coherence_fractioned.py
#python ./Analysis/Classification_Synchronization_XCORR_PHASE_LAG_fractioned.py
#python ./Analysis/Construct_Network_From_Phase_XCorr_and_Lag_Coexistence_fractioned.py
#python ./Analysis/Construct_Network_From_Phase_XCorr_and_Lag_AVERAGE_Coexistence_fractioned.py
#python ./Analysis/Classification_Synchronization_Types_Histogram.py
#gnuplot ./Analysis/Plot_Polar_histogram.gnu	
#python ./Analysis/Correlation_PLV_and_Classification.py
#python ./Analysis/Make_movie.py
#python ./Analysis/Compute_PSD_colormap_head.py
#python ./Analysis/Compute_Logic_Gates_PLV.py
#python ./Analysis/Compute_Logic_Gates_Coherence.py

