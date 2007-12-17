%define name codeworker
%define version 4.2
%define release %mkrel 1

Summary: A universal parsing tool and a source code generator
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Development/Other
Url: http://codeworker.free.fr/
BuildRequires: gcc-c++

%description
CodeWorker is a versatile Open Source  (GNU Lesser General Public License)
parsing tool and a source code generator devoted to generative programming.
Generative programming is a software engineering approach interested in
automating the production of reusable, tailor-made, adaptable and reliable
IT systems.
In layman's terms, CodeWorker lets you generate code by parsing existing
languages, or by creating and parsing your own language. Once a language
file has been parsed, CodeWorker provides several techniques for
generating code.

%package devel
Group: System/Libraries
Summary: Codeworker's static library

%description devel
CodeWorker is a versatile Open Source  (GNU Lesser General Public License)
parsing tool and a source code generator devoted to generative programming.
Generative programming is a software engineering approach interested in
automating the production of reusable, tailor-made, adaptable and reliable
IT systems.
In layman's terms, CodeWorker lets you generate code by parsing existing
languages, or by creating and parsing your own language. Once a language
file has been parsed, CodeWorker provides several techniques for
generating code.

This package include the codeworker static library

%prep
%setup -q

%build
%{_make_bin} all

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -m 755 -D codeworker $RPM_BUILD_ROOT%{_bindir}/codeworker
%{__install} -m 644 -D libcodeworker.a $RPM_BUILD_ROOT%{_libdir}/libcodeworker.a
for i in ./*.h; do
	%{__install} -m 644 -D $i $RPM_BUILD_ROOT%{_includedir}/%{name}/$i
done

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Documentation/ Scripts/ WebSite/
%{_bindir}/codeworker

%files devel
%defattr(-,root,root)
%{_libdir}/libcodeworker.a
%{_includedir}/*

