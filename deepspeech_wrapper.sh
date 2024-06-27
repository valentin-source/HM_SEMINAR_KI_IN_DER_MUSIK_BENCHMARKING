#!/bin/bash

S_T=$(date +%s)
if ["$#" -ne 1]; then
	echo "Usage: $0 <audio_file>"
	exit 1
fi
File=$1
echo "starting: "
deepspeech --model ./deepspeech-0.9.3-models.pbmm --audio "./$File" &
DPID=$!
echo "deepspeech PID: $DPID"
wait $DPID
E_D=$(date +%s)
DUR=$((E_D - S_T))
echo "Time taken: $DUR seconds"
