%define gitrel	git523cc4d6ab	


Summary:	noVNC is a HTML5 VNC client that runs well in any modern browser
Name:		novnc
Version:	%{gitrel}.1
Release:	1
License:	GPLv3
Group:		Networking/Remote access
URL:		https://github.com/kanaka/noVNC
Source0:	https://github.com/kanaka/noVNC/tarball/noVNC.tar.bz2

%description
noVNC is a HTML5 VNC client that runs well in any modern
browser including mobile browsers (iPhone/iPad and Android).

%prep
%setup -q -n noVNC

%build
cd utils/
%make


%install
mkdir -p %buildroot/%{_datadir}/noVNC/include
cp -r include/*  %{buildroot}/%{_datadir}/noVNC/include

mkdir -p %buildroot/%{_datadir}/noVNC/utils

cp -r utils/*  %{buildroot}/%{_datadir}/noVNC/utils
cp -r *.html  %{buildroot}/%{_datadir}/noVNC/
chmod +x %{buildroot}/%{_datadir}/noVNC/utils/launch.sh




%files
%{_datadir}/noVNC/include/*
%{_datadir}/noVNC/utils/*
%{_datadir}/noVNC/*.html
