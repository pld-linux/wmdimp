#
# Conditional build:
%bcond_without	mad	# enable MP3 player using wrapper to mpg123
#
Summary:	Window Maker DIgital Music Player
Summary(pl):	Muzyczny Odtwarzacz Cyfrowy dla Window Makera
Name:		wmdimp
Version:	0.3
%define _beta   beta2
Release:	0.%{_beta}.1
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://www.dei.unipd.it/~datamino/%{name}-%{version}%{_beta}.tar.gz
# Source0-md5:	6667277bb7a69980cb1d9bb142183c16
Source1:	%{name}.desktop
URL:		http://wmdimp.cjb.net
%{?with_mad:BuildRequires:	libmad-devel}
%{?with_mad:BuildRequires:	libid3tag-devel}
%{!?with_mad:Requires:	mpg123}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wmdimp is a digital music palyer. It uses an internal player based on
libmad, or a wrapper to mpg123. Based on wmmp3 code, but almost
completely rewritten. It uses low memory and cpu power.

%description -l pl
Wmdimp jest muzycznym odtwarzaczem cyfrowym. U¿ywa wewnêtrznego
odtwarzacza opartego o libmad albo nak³adki na mpg123. Jest oparty na
kodzie wmmp3 ale prawie ca³kowicie przepisanego. U¿ywa ma³ych zasobów
pamiêci i mocy procesora.

%prep
%setup -q -n %{name}-%{version}%{_beta}

%build
# always - doesn't build without NDEBUG
CFLAGS="%{rpmcflags} -DNDEBUG=1"
%configure \
	%{!?with_mad:--without-mad}
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO sample.wmdimprc
%attr(755,root,root) %{_bindir}/*
