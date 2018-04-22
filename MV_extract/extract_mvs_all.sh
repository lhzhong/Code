#!/usr/bin/bash 

tar xvf ffmpeg-2.7.2.tar
tra xvf MV-code-release.tar

DIR=KTH
for f in ${DIR}/*/*.avi; do
  avi_dir=${f#*/}
  new_avi_dir=KTH_MV/${avi_dir::-4}
  echo -----
  echo Extracting frames from ${f} into ${new_avi_dir}...
  if [[ ! -d ${new_avi_dir} ]]; then
    echo Creating directory=${new_avi_dir}
    mkdir -p ${new_avi_dir}
  fi
  ffmpeg-2.7.2/doc/examples/extract_mvs ${f} > dump.mvs0
	MV-code-release/Release/mpegflow -f dump.mvs0 -x ${new_avi_dir}/flow_x -y ${new_avi_dir}/flow_y -b 20
done

echo -------------------------------------------
echo Done!
