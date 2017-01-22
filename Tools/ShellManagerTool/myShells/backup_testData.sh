cd /home/yangzheng/
date=`date +%Y-%m-%d_%H-%M-%S`
targetName='myTestDataBackup_'$date'.tar.gz'
tar -zcvf $targetName myProgram/test
sudo mv $targetName myShare
