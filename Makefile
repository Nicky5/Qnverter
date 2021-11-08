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
	-mkdir -p $(BINDIR)
	-mkdir -p $(APPDIR)
	-mkdir -p $(SCRIPTDIR)
	-mkdir -p $(RESDIR)
	-mkdir -p $(SHAREAPPDIR)
	-mkdir -p $(SHAREICODIR)

	cp resources/*.png ${RESDIR}
	cp scripts/*.py ${SCRIPTDIR}
	cp qnverter/qnverter.py ${APPDIR}
	cp installpath.txt ${APPDIR}

	cp qnverter.desktop ${SHAREAPPDIR}/qnverter.desktop
	cp $(RESDIR)/qnverter.png ${SHAREICODIR}/qnverter.png

	chmod --recursive 755 ${APPDIR}
	ln -s -f ${APPDIR}/qnverter.py $(BINDIR)/qnverter
	@echo $(APPDIR) > $(APPDIR)installpath.txt

uninstall:
	-rm -f ${SHAREAPPDIR}/qnverter.desktop
	-rm -f ${SHAREICODIR}/qnverter.png
	-rm -f ${BINDIR}/qnverter
	-rm -f -r ${APPDIR}/*
	-rmdir ${APPDIR}

