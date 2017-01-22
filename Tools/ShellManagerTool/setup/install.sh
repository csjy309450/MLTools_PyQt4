# create desktop file
title='#!/usr/bin/env xdg-open\n[Desktop Entry]\n'
Type='Type=Application\n'
Encoding='Encoding=UTF-8\n'
Name='Name=ShellManager\n'
Comment='Comment=ShellManager APP\n'
ShellManagerDirPath=$(cd $(dirname $0);cd ../;pwd)
exec_path=$ShellManagerDirPath'/SM.sh'
Exec='Exec=/bin/sh '$exec_path'\n'
Icon='Icon='$ShellManagerDirPath'/SM.ico\n'
Terminal='Terminal=true\n'
StartupNotify='StartupNotify=true\n'
Categories='Categories=Office;'
echo $title$Type$Encoding$Name$Comment$Exec$Icon$Terminal$StartupNotify$Categories>ShellManager.desktop
sudo chmod 777 ./ShellManager.desktop
# copy desktop file to 
sudo cp ShellManager.desktop /usr/share/applications
sudo cp ShellManager.desktop /home/$(whoami)/桌面

shellDirPath=$ShellManagerDirPath'/myShells'
#echo $shellDirPath
echo $shellDirPath>$ShellManagerDirPath'/'shellDirPath.txt
