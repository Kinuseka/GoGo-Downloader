#!/bin/bash
exists()
{
  command -v goanime
}

if exists bash; then
  echo "COMMAND ALREADY EXISTS"
else
  echo >$PREFIX/bin/goanime
  chmod +x $PREFIX/bin/goanime
  echo "cd $HOME/storage/shared/GoGo-Downloader && python RuNime.py" >> $PREFIX/bin/goanime
fi