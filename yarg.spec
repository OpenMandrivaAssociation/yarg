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
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xrandr)
BuildRequires: boost-devel = 1.53.0-2

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


%changelog
* Thu Dec 09 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.4-1mdv2011.0
+ Revision: 618312
- New version: 0.4

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Thu Apr 01 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.3-1mdv2010.1
+ Revision: 530745
- import yarg

