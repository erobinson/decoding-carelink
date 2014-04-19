
sudo ./bin/mm-send-comm.py  --init --port /dev/ttyUSB0  --serial 584923  --prefix  ReadCurPageNumber --prefix ReadCurGlucosePageNumber  sleep 0

sleep 3
for ((i=1; i<=2; i++ ))
do
	sleep 3
	sudo ./bin/mm-send-comm.py -v --prefix-path logs/cgm-v-page-$i- --serial 584923 --port /dev/ttyUSB0 tweak ReadSensorHistoryData --page $i --save | tee analysis/page-$i-v-ReadSensorHistory.markdown
done


for ((i=1; i<=2; i++ ))
do
	sleep 3
	sudo ./bin/mm-send-comm.py -vv --prefix-path logs/cgm-page-$i- --serial 584923 --port /dev/ttyUSB0 tweak ReadSensorHistoryData --page $i --save | tee analysis/page-$i-vv-ReadSensorHistory.markdown
done

