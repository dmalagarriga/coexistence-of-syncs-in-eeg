#!/bin/bash

for i in $(seq 2 12)
	do
	for j in $(seq --format '%03.0f' 1 109)
		do 
		mkdir -p "Task_$i/S$j/Coexistence_pairs/Thresh_2"
		mkdir -p "Task_$i/S$j/Lag_pairs/Thresh_2"
		mkdir -p "Task_$i/S$j/Complete_pairs/Thresh_2"
		mkdir -p "Task_$i/S$j/Phase_pairs/Thresh_2"
		mkdir -p "Tasks_consistence/Task_$i/S$j/Coexistence/Thresh_2/Sync_patterns"
		mkdir -p "Tasks_consistence/Task_$i/S$j/Coexistence/Thresh_2/Consistency"
	done
done
