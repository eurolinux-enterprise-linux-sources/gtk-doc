version = "1.28"

# tools
dblatex = '/usr/bin/dblatex'
fop = ''
highlight = '/usr/bin/source-highlight'
highlight_options = '-t4 -s$SRC_LANG -cstyle.css --no-doc -i'
pkg_config = '/usr/bin/pkg-config'
xsltproc = '/usr/bin/xsltproc'

# configured directories
prefix = '/usr'
datarootdir = "${prefix}/share".replace('${prefix}', prefix)
datadir = "${datarootdir}".replace('${datarootdir}', datarootdir)

exeext = ''
