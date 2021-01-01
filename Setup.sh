#!/bin/bash
checker() 
{
  command -v goanime
}
if checker bash; then
  echo "Command already setup"
else
  echo >$PREFIX/bin/goanime
  chmod +x $PREFIX/bin/goanime
  echo "cd $HOME/storage/shared/GoGo-Downloader && python RuNime.py" 
installer()
{
  cd "$HOME/storage/shared/GoGo-Downloader"
  command wget ''
}