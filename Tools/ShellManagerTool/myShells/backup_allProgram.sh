cd /home/yangzheng/
date=`date +%Y-%m-%d_%H-%M-%S`
targetName='myProgramBackup_'$date'.tar.gz'
tar -zcvf $targetName myProgram
sudo mv $targetName myShare
