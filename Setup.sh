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
  echo "cd $HOME/storage/shared/GoGo-Downloader && python RuNime.py" >> $PREFIX/bin/goanime
  echo >$PREFIX/bin/goupdate!
  chmod +x $PREFIX/bin/goupdate!
  echo "wget -O - 'https://raw.githubusercontent.com/Kinuseka/GoGo-Downloader/main/Setup.sh' | bash" >> $PREFIX/bin/goupdate!
  echo "You can now do 'goupdate! to update'"
fi
installer()
{
  cd "$HOME/storage/shared/"
  command wget 'https://github.com/Kinuseka/GoGo-Downloader/releases/download/V1.2-prerelease/GoGoDownloader.v1.2pre.zip'
  command unzip -o '$HOME/storage/shared/GoGoDownloader v1.2.pre.zip'
  command mv '$HOME/storage/shared/GoGoDownloader(v1.2 build2)/goEmbed.py' '$HOME/storage/shared/GoGo-Downloader'
  command mv '$HOME/storage/shared/GoGoDownloader(v1.2 build2)/RuNime.py' '$HOME/storage/shared/GoGo-Downloader'
  command mv '$HOME/storage/shared/GoGoDownloader(v1.2 build2)/NineScraper.py' '$HOME/storage/shared/GoGo-Downloader'
  command mv '$HOME/storage/shared/GoGoDownloader(v1.2 build2)/options.ini' '$HOME/storage/shared/GoGo-Downloader'
}
echo "Installing GoGoDownloader.."
installer