#!/bin/bash

Create_Files=0
Smooth_signal=0
Analysis=1



export situation
export number=0
export Coexistence=Coexistence
export Pairs=Coexistence_pairs
export Threshold=1
export Thresh_XCORR=0.90
export Thresh_PLV=0.90
export Thresh_Coherence=0.90

for situation in Eyes_opened #Eyes_closed #Task_1  Task_2  
	do
	for number in {1..1} # Subject number 
		do
		printf -v Num "%03i" $number
		mkdir -p ./Data/${situation}/S${Num}
		export P_Dir="./Data/${situation}/S${Num}"
		if [ $Create_Files -eq 1 ];then
			printf "Creating txt files...\n"
			if [ $situation = "Eyes_opened" ];then
				./edf2ascii ./Data/${situation}/S${Num}/S${Num}R01.edf
			fi
			if [ $situation = "Eyes_closed" ];then
				./edf2ascii ./Data/${situation}/S${Num}/S${Num}R02.edf
			fi
			if [ $situation = "Task_1" ];then
				./edf2ascii ./Data/${situation}/S${Num}/S${Num}R03.edf
			fi
		
			if [ $situation = "Task_2" ];then
				./edf2ascii ./Data/${situation}/S${Num}/S${Num}R04.edf
			fi
			if [ $situation = "Task_3" ];then
				./edf2ascii ./Data/${situation}/S${Num}/S${Num}R05.edf
			fi
		
			if [ $situation = "Task_4" ];then
				./edf2ascii ./Data/${situation}/S${Num}/S${Num}R06.edf
			fi

			if [ $situation = "Task_5" ];then
				./edf2ascii ./Data/${situation}/S${Num}/S${Num}R07.edf
			fi
		
			if [ $situation = "Task_6" ];then
				./edf2ascii ./Data/${situation}/S${Num}/S${Num}R08.edf
			fi
			if [ $situation = "Task_7" ];then
				./edf2ascii ./Data/${situation}/S${Num}/S${Num}R09.edf
			fi
		
			if [ $situation = "Task_8" ];then
				./edf2ascii ./Data/${situation}/S${Num}/S${Num}R010.edf
			fi
			
			if [ $situation = "Task_9" ];then
				./edf2ascii ./Data/${situation}/S${Num}/S${Num}R11.edf
			fi
		
			if [ $situation = "Task_10" ];then
				./edf2ascii ./Data/${situation}/S${Num}/S${Num}R12.edf
			fi
			if [ $situation = "Task_11" ];then
				./edf2ascii ./Data/${situation}/S${Num}/S${Num}R13.edf
			fi
		
			if [ $situation = "Task_12" ];then
				./edf2ascii ./Data/${situation}/S${Num}/S${Num}R14.edf
			fi
		fi
		
		if [ $Smooth_signal -eq 1 ];then
			
			printf "Smoothening signal....\n"
			python ./Preprocessing/Smooth_signal.py
			printf "...Smoothed signal!\n"
		
		fi


		
		if [ $Analysis -eq 1 ];then
		
			printf "Making folders for spectra and consistence....\n"
			printf -v Number "%01i" $Threshold
			#mkdir -p ./${P_Dir}/Coexistence_pairs/Thresh_${Number}/
			mkdir -p Results/Tasks_spectra/${situation}/S${Num}/
			mkdir -p Results/Tasks_consistence/${situation}/S${Num}/Coexistence/Thresh_${Number}/Sync_patterns/
			mkdir -p Results/Tasks_consistence/${situation}/S${Num}/Coexistence/Thresh_${Number}/Consistency/

			export Sync_patterns="Results/Tasks_consistence/${situation}/S${Num}/Coexistence/Thresh_${Number}/Sync_patterns/"
			export Task_spectra="Results/Tasks_spectra/${situation}/S${Num}/"
			
			printf "...folders made!\n\n"
			printf "Analysing....\n"
			bash ./Executables/Analysis.bash
			printf "\nAnalyzed!\n"
		fi

	done
done

