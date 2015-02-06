%define oname CodeWorker
%define tarballver %(echo %version |sed -e 's#\\.#_#g')

Summary:	A universal parsing tool and a source code generator
Name:		codeworker
Version:	4.5.4
Release:	3
Source0:	http://codeworker.free.fr/downloads/%{oname}_SRC%{tarballver}.zip
Patch0:		codeworker-4.5.1-enable-readline.patch
Patch1:		codeworker-4.5.1-gcc4.3.patch
License:	LGPLv2+
Group:		Development/Other
URL:		http://codeworker.free.fr/
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	readline-devel

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
Group:		System/Libraries
Summary:	Codeworker static library

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
%setup -q -n %{oname}%{tarballver}
%patch0 -p0
%patch1 -p0

%build
%make CFLAGS="%{optflags}" LDFLAGS="%{?ldflags} -L%_libdir"

%install
%{__install} -m 755 -D codeworker %{buildroot}%{_bindir}/codeworker
%{__install} -m 644 -D libcodeworker.a %{buildroot}%{_libdir}/libcodeworker.a
for i in ./*.h; do
	%{__install} -m 644 -D $i %{buildroot}%{_includedir}/%{name}/$i
done

%files
%doc Documentation/ Scripts/ WebSite/
%{_bindir}/codeworker

%files devel
%{_libdir}/libcodeworker.a
%{_includedir}/*

