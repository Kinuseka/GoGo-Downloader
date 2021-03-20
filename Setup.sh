#!/bin/bash
importance=1
printf ' ____________  _______
|             |   _   \
|             | |  \   \
|             | |   |  |
|      _____  | |   |  |
|           | | |__/  /
|___________| |______/
v1.1
'
# Changeable Arguments
name='GoGoDownloader(v1.3p6)'

zipname='GoGoDownloader.v1.3p6.zip'

link='https://github.com/Kinuseka/GoGo-Downloader/releases/download/V1.3-patch(6)/GoGoDownloader.v1.3p6.zip'

# For the uninstall command
unistall='#!/bin/bash
printf "==============================
Uninstalling GoGoDownloader
==============================\n
"
dependent()
{ 
  echo "Uninstalling dependencies"
  yes | pkg uninstall python 
  yes | pkg uninstall rsync 
  yes | pkg uninstall aria2
}
uninstall() 
{
  command cd $HOME
  command rm -r "$HOME/storage/shared/GoGo-Downloader"
  command cd $PREFIX
  command rm "$PREFIX/bin/goanime"
  command rm "$PREFIX/bin/goupdate"
  command rm "$PREFIX/bin/gouninstall"
  command rm "$PREFIX/bin/goupdate!"
  echo "Done!"
} 
canelor()
{
  echo "Cancelled"
}
formatvar=0
read -p $"This will cause deletion of the folder contents and the implemented commands, continue? (y/n)" formatvar
if [ "$formatvar" == "y" ]; then
  condition1=1
  read -p $"Would you like to delete all packages/dependencies installed with the program? e.g. python,aria2,etc (y/n)" formatvar 
  if [ "$formatvar" = "y" ]; then
    condition2=1 
  elif [ "$formatvar" = "n" ]; then 
    condition2=0
  else
    echo "Invalid/No answer (Set to No by default)"
    condition2=0
  fi
elif [ "$formatvar" = "n" ]; then
  canelor
else
  canelor
fi 

if [ "$condition1" == 1 ]; then
  uninstall 
  echo "Removed Program"
  if [ "$condition2" == 1 ]; then
    dependent
    echo "Removed Dependencies"
  fi
fi 
'

update='''
#!/bin/bash
printf "=============================
Update GoGoDownloader
=============================\n"
read -p $"Would you like to update all dependencies installed with the program? e.g. python,aria2,etc.. (y/n)" formatvar 
update()
{
  curl -L https://raw.githubusercontent.com/Kinuseka/GoGo-Downloader/main/Setup.sh | bash -s -- update
} 
noupdate()
{
  curl -L https://raw.githubusercontent.com/Kinuseka/GoGo-Downloader/main/Setup.sh | bash -s -- none
}
if [[ "$formatvar" == "y" ]]; then
  update
else
  noupdate
fi
'''

# Setup area
initial()
{
  echo "-------Installing Requirements-------"
  yes | apt-get install python 
  yes | apt-get install rsync
  command pip install bs4
  command pip install requests
  yes | apt-get install aria2
  echo "-------Requirements Installed-------"
}


status="${1}"
printf "$status\n"
if [[ $status == "update" ]]; then
  initial
elif [[ $status == "none"]]; then
  echo "skip"
else
  initial
fi
#initial
checker() 
{
  command -v goanime
}
checker_2()
{
  command -v goupdate
}
checker_3()
{
  command -v gouninstall
}
uninstaller()
{
  echo >$PREFIX/bin/gouninstall
  chmod +x $PREFIX/bin/gouninstall
  printf "${unistall}" > $PREFIX/bin/gouninstall
}
rinnstaller()
{
  echo >$PREFIX/bin/goanime
  chmod +x $PREFIX/bin/goanime
  printf "#!/bin/bash\ncd $HOME/storage/shared/GoGo-Downloader\npython RuNime.py" > $PREFIX/bin/goanime
  echo ">>Setupped 001"
}
rimeinstaller()
{
  echo >$PREFIX/bin/goupdate
  chmod +x $PREFIX/bin/goupdate
  printf "${update}" > $PREFIX/bin/goupdate
  echo ">>You can now do 'goupdate' to update"
}



if checker bash; then
  echo ">>Command 'goanime' already setup"
  if [ $importance == 1 ]; then
    echo "Overwrite command detected no.1"
    rinnstaller
  fi
else
  rinnstaller
fi 

if checker_2 bash; then
  echo ">>Command 'goupdate' already setup"
  if [ $importance == 1 ]; then
    echo "Overwrite command detected no.2"
    rimeinstaller
  fi
else
  rimeinstaller
fi 

if checker_3 bash; then
  echo ">>Command 'gouninstall' already setup"
  if [ $importance == 1 ]; then
    echo "Overwrite command detected no.3"
    uninstaller
  fi
else
  uninstaller
fi 

installer()
{
  cd "$HOME/storage/shared/"
  command rm -r 'GoGo-Downloader/__pycache__'
  command wget "${link}"
  echo '>>Downloaded process 1'
  command unzip -o "${zipname}"
  echo '>>Action_complete process 2'
  DIR='GoGo-Downloader'
  if [ -d "$DIR" ]; then
    command rsync -a "${name}"/* 'GoGo-Downloader'
    bool=true
    echo '1'
  else
    command mv -f "${name}" 'GoGo-Downloader'
    echo '2'
  fi
  echo '>>Action_complete process 3'
}
cleaner()
{
  cd "$HOME/storage/shared/"
  command rm "${zipname}"
  echo '>>Cleaned process 1'
  if [ "$bool" = true ]; then
    command rm -r "${name}"
    echo '>>Cleaned process 2'
  else
    echo '>>skipped process 2'
  fi
}
echo "Installing GoGoDownloader.." 
installer
cleaner
printf 'Do "gouninstall" to uninstall\n'
printf 'Do "goupdate" to update!\n'
printf '======================================
Setup finished! do "goanime" to start!
======================================
'
