#!/bin/sh

suite=$1
dir=`dirname $0`

PATH=`pwd`:$PATH PERL5LIB=`pwd`:$PERL5LIB && cd $dir/$suite/docs && gtkdoc-check

# xmllint --noout --nonet --schema ../devhelp2.xsd ./bugs/docs/html/tester.devhelp2
#
