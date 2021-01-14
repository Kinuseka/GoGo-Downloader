#!/bin/bash
name='GoGoDownloader(v1.3 beta)'
zipname='GoGoDownloader.v1.3pre.zip'
link='https://github.com/Kinuseka/GoGo-Downloader/releases/download/V1.3-prerelease/GoGoDownloader.v1.3pre.zip'

initial()
{
  command pkg install python
  command pip install bs4
  command pip install requests
  command apt-get install aria2
}
initial
checker() 
{
  command -v goanime
}
checker_2()
{
  command -v goupdate!
}
checker_3()
{
  command -v gouninstall
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
  echo >$PREFIX/bin/goupdate!
  chmod +x $PREFIX/bin/goupdate!
  printf "#!/bin/bash\nwget -O - 'https://raw.githubusercontent.com/Kinuseka/GoGo-Downloader/main/Setup.sh' | bash" > $PREFIX/bin/goupdate!
  echo ">>You can now do 'goupdate!' to update"
}
if checker bash; then
  echo ">>Command 'goanime' already setup"
else
  rinnstaller
fi 

if checker_2 bash; then
  echo ">>Command 'goupdate!' already setup"
else
  rimeinstaller
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
    command mv -f "${name}"/* 'GoGo-Downloader'
    bool=true
    echo '1'
  else
    command mv "${name}" 'GoGo-Downloader'
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
echo '======================================'
echo 'Setup finished! do "goanime" to start!'
echo '======================================'