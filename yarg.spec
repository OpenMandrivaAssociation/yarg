Name: yarg
Version: 0.4
Release: %mkrel 1
Summary: Yet Another Randr Gui
Group: System/X11
Source0: %{name}-%{version}.tar.bz2
Source1: %{name}.desktop
License: GPLv2+
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: qt4-devel
BuildRequires: libx11-devel
BuildRequires: libxrandr-devel
BuildRequires: libboost-devel

%description
Yet Another Randr Gui is a very simple Randr gui written in QT. Currently, it
only supports basic functionality and can be minimized to tray.

%prep
%setup -q

%build
qmake PREFIX=/usr

%make

%install
rm -rf %{buildroot}
make install INSTALL_ROOT=%{buildroot}

mkdir -p %{buildroot}/%{_datadir}/applications/
cp -r %{SOURCE1} %{buildroot}/%{_datadir}/applications/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/yarg
%{_datadir}/yarg
%{_datadir}/applications/yarg.desktop
%{_mandir}/man1/yarg.1*
