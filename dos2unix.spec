Summary:	dos2unix - DOS/MAC to UNIX text file format converter
Summary(pl):	dos2unix - konwerter plików tekstowych z formatu DOS/MAC na UNIX
Name:		dos2unix
Version:	3.0
Release:	2
Copyright:	Freer than LGPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst
Source0:	%{name}-%{version}.src.tar.gz
Source1:	unix2dos-2.2.src.tar.gz
Obsoletes:	unix2dos
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A utility that converts plain text files in DOS/MAC format to UNIX
format and back.

%description -l pl
Zestaw narzêdzi do konwersji pliki tekstowych w formacie DOS/MAC na
u¿ywany poprzez UNIXa oraz odwrotnie.

%prep
%setup -q -c -a1

%build
%{__cc} %{rpmcflags} -o dos2unix dos2unix.c
%{__cc} %{rpmcflags} -o unix2dos unix2dos.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -m 755 dos2unix $RPM_BUILD_ROOT%{_bindir}
install -m 755 unix2dos $RPM_BUILD_ROOT%{_bindir}
install dos2unix.1 $RPM_BUILD_ROOT%{_mandir}/man1
install unix2dos.1 $RPM_BUILD_ROOT%{_mandir}/man1

ln -sf dos2unix $RPM_BUILD_ROOT%{_bindir}/mac2unix

echo ".so dos2unix.1" > $RPM_BUILD_ROOT%{_mandir}/man1/mac2unix.1

gzip -9nf COPYRIGHT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT.gz
%attr(755, root, root) %{_bindir}/*
%{_mandir}/man1/*
