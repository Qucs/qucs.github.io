#!/bin/bash

if [ $# -ne 2 ]
then
  echo Need REPOSITORY and TARGET paths as parameters
  echo 'e.g., $ sh build_copy_docs.sh ~/git/qucs `pwd`'
  exit
else
  REPO="$1"
  TARGET="$2"
  echo $REPO
  echo $TARGET
  echo ' -> Looking for documentation in :' $REPO
  echo ' -> Destination for documentation:' $TARGET
fi

cd $REPO/qucs-doc

./autogen.sh
cd tutorial
make tutorial
make book
cd ..
cd report
make report
make book
cd ..
cd technical
make technical
ps2pdf technical.ps

cd $REPO/qucs-doc

echo '\nCopy generated documentation\n'

DOC_SUBDIRS="report technical tutorial"
for DOC_SUBDIR in ${DOC_SUBDIRS} ; do
	cd $DOC_SUBDIR
	mkdir -p $TARGET/docs/$DOC_SUBDIR
	find . -name "*.pdf" |grep -v pics| xargs -I{} cp {} $TARGET/docs/$DOC_SUBDIR
	cd ..
done

