Summary:	Lithuanian dictionary for ispell
Name:		ispell-lt
Version:	1.2.1
Release:	1
License:	BSD-like
Group:		Applications/Text
Source0:	http://files.akl.lt/ispell-lt/%{name}-%{version}.tar.gz
# Source0-md5:	538b3e3d35a87397233f18027180eff8
URL:		ftp://ftp.akl.lt/ispell-lt/
BuildRequires:	ispell
BuildRequires:	python
Requires:	ispell
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lithuanian dictionary (i.e. word list) for ispell.

%prep
%setup -q
%{__sed} -i -e 's,\r$,,' INSTRUKCIJOS.txt

%build
%{__make} lietuviu.hash

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ispell
install lietuviu.aff $RPM_BUILD_ROOT%{_libdir}/ispell/lithuanian.aff
install lietuviu.hash $RPM_BUILD_ROOT%{_libdir}/ispell/lithuanian.hash

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.EN THANKS
%doc %lang(lt) INSTRUKCIJOS.txt README
%{_libdir}/ispell/*
