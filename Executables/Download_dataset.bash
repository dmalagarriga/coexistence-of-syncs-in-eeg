#!/bin/bash

for number in $(seq 1 1 109)
	do
	printf -v Num "%03i" $number
	mkdir -p Eyes_opened/S${Num}
	mkdir -p Eyes_closed/S${Num}
	mkdir -p Task_1/S${Num}
	mkdir -p Task_2/S${Num}
	mkdir -p Task_3/S${Num}
	mkdir -p Task_4/S${Num}
	mkdir -p Task_5/S${Num}
	mkdir -p Task_6/S${Num}
	mkdir -p Task_7/S${Num}
	mkdir -p Task_8/S${Num}
	mkdir -p Task_9/S${Num}
	mkdir -p Task_10/S${Num}
	mkdir -p Task_11/S${Num}
	mkdir -p Task_12/S${Num}
	wget -P Eyes_opened/S${Num} https://www.physionet.org/physiobank/database/eegmmidb/S${Num}/S${Num}R01.edf
	wget -P Eyes_closed/S${Num} https://www.physionet.org/physiobank/database/eegmmidb/S${Num}/S${Num}R02.edf
	wget -P Task_1/S${Num} https://www.physionet.org/physiobank/database/eegmmidb/S${Num}/S${Num}R03.edf
	wget -P Task_2/S${Num} https://www.physionet.org/physiobank/database/eegmmidb/S${Num}/S${Num}R04.edf
	wget -P Task_3/S${Num} https://www.physionet.org/physiobank/database/eegmmidb/S${Num}/S${Num}R05.edf
	wget -P Task_4/S${Num} https://www.physionet.org/physiobank/database/eegmmidb/S${Num}/S${Num}R06.edf
	wget -P Task_5/S${Num} https://www.physionet.org/physiobank/database/eegmmidb/S${Num}/S${Num}R07.edf
	wget -P Task_6/S${Num} https://www.physionet.org/physiobank/database/eegmmidb/S${Num}/S${Num}R08.edf
	wget -P Task_7/S${Num} https://www.physionet.org/physiobank/database/eegmmidb/S${Num}/S${Num}R09.edf
	wget -P Task_8/S${Num} https://www.physionet.org/physiobank/database/eegmmidb/S${Num}/S${Num}R10.edf
	wget -P Task_9/S${Num} https://www.physionet.org/physiobank/database/eegmmidb/S${Num}/S${Num}R11.edf
	wget -P Task_10/S${Num} https://www.physionet.org/physiobank/database/eegmmidb/S${Num}/S${Num}R12.edf
	wget -P Task_11/S${Num} https://www.physionet.org/physiobank/database/eegmmidb/S${Num}/S${Num}R13.edf
	wget -P Task_12/S${Num} https://www.physionet.org/physiobank/database/eegmmidb/S${Num}/S${Num}R14.edf
done
