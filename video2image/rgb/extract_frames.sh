#!/usr/bin/env bash

#############################################
#      What you need to do
#1.modify the {DIR} {new_avi_dir} data directory
#2.make sure ffmpeg is installed
#3.place this file at your data directory menu
#############################################

FFMPEGBIN=ffmpeg
DIR=KTH
for f in ${DIR}/*/*.avi; do
  avi_dir=${f#*/}
  new_avi_dir=KTH_RGB/${avi_dir::-4}
  echo -----
  echo Extracting frames from ${f} into ${new_avi_dir}...
  if [[ ! -d ${new_avi_dir} ]]; then
    echo Creating directory=${new_avi_dir}
    mkdir -p ${new_avi_dir}
  fi
  ${FFMPEGBIN} -i ${f} ${new_avi_dir}/image_%4d.jpg
done

echo -------------------------------------------
echo Done!
