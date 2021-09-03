PREFIX        = /usr
BINDIR	      = $(PREFIX)/bin
APPDIR	      = /opt/Qnverter
SCRIPTDIR	  = $(APPDIR)/scripts
RESDIR 		  = $(APPDIR)/resources
SHAREAPPDIR   = $(PREFIX)/share/applications
SHAREICODIR   = $(PREFIX)/share/icons/hicolor/256x256/apps

ICON 		  = $(APPDIR)/resources/qnverter.png
EXEC		  = $(APPDIR)/qnverter.py

all:
	@echo "run \'make install' to install qnverter"

install:
	pip install -r requirements.txt
	-mkdir -p $(BINDIR)
	-mkdir -p $(APPDIR)
	-mkdir -p $(SCRIPTDIR)
	-mkdir -p $(RESDIR)
	-mkdir -p $(SHAREAPPDIR)
	-mkdir -p $(SHAREICODIR)

	cp resources/*.png                                    ${RESDIR}
	cp scripts/*.py                                     ${SCRIPTDIR}
	cp qnverter.py                                     ${APPDIR}

	cp qnverter.desktop               ${SHAREAPPDIR}/qnverter.desktop
	cp $(RESDIR)/qnverter.png				      ${SHAREICODIR}/qnverter.png

	chmod --recursive 755 ${APPDIR}
	ln -s ${APPDIR}/qnverter.py $(BINDIR)/qnverter

uninstall:
	-rm -f ${SHAREAPPDIR}/qnverter.desktop
	-rm -f ${SHAREICODIR}/qnverter.png
	-rm -f ${BINDIR}/qnverter
	-rm -f -r ${APPDIR}/*
	-rmdir ${APPDIR}

