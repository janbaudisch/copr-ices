Name: ices
Version: 2.0.3
Release: 1%{?dist}
Summary: Source client for the Icecast streaming server
License: GPL-2.0-only
URL: https://www.icecast.org/ices
Provides: ices
Source0: https://downloads.us.xiph.org/releases/ices/ices-%{version}.tar.gz
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(shout)
BuildRequires: pkgconfig(vorbis)
BuildRequires: /usr/bin/cc

%description
IceS is a source client for the Icecast streaming server. The purpose of this client is to provide an audio stream to Icecast, so that one or more listeners can access the stream. With this layout, the source client can be situated remotely from the Icecast server.

%prep
%autosetup

%build
%configure
make

%install
%make_install

%files
%license COPYING
%{_bindir}/ices
/usr/share/ices/*
