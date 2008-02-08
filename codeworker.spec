%define oname CodeWorker

Summary:	A universal parsing tool and a source code generator
Name:		codeworker
Version:	4.4
Release:	%mkrel 1
Source0:	http://codeworker.free.fr/downloads/%{oname}_SRC4_4.zip
License:	LGPLv2+
Group:		Development/Other
URL:		http://codeworker.free.fr/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gcc-c++

%description
CodeWorker is a versatile parsing tool and a source code generator
devoted to generative programming. Generative programming is a
software engineering approach interested in automating the production
of reusable, tailor-made, adaptable and reliable IT systems.
In layman's terms, CodeWorker lets you generate code by parsing
existing languages, or by creating and parsing your own language. Once
a language file has been parsed, CodeWorker provides several
techniques for generating code.

%package devel
Group: System/Libraries
Summary: Codeworker static library

%description devel
CodeWorker is a versatile parsing tool and a source code generator
devoted to generative programming. Generative programming is a
software engineering approach interested in automating the production
of reusable, tailor-made, adaptable and reliable IT systems.
In layman's terms, CodeWorker lets you generate code by parsing
existing languages, or by creating and parsing your own language. Once
a language file has been parsed, CodeWorker provides several
techniques for generating code.

This package include the static library.

%prep
%setup -q -n %{oname}4_4

%build
%{_make_bin} all

%install
%{__rm} -rf %{buildroot}
%{__install} -m 755 -D codeworker %{buildroot}%{_bindir}/codeworker
%{__install} -m 644 -D libcodeworker.a %{buildroot}%{_libdir}/libcodeworker.a
for i in ./*.h; do
	%{__install} -m 644 -D $i %{buildroot}%{_includedir}/%{name}/$i
done

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Documentation/ Scripts/ WebSite/
%{_bindir}/codeworker

%files devel
%defattr(-,root,root)
%{_libdir}/libcodeworker.a
%{_includedir}/*

