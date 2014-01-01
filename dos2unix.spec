Summary:	dos2unix - DOS/MAC to UNIX text file format converter
Summary(fr.UTF-8):	Convertisseur de format de fichier texte
Summary(pl.UTF-8):	dos2unix - konwerter plików tekstowych z formatów DOS/MAC na UNIX
Summary(pt_BR.UTF-8):	Conversor de formatos de arquivos texto
Summary(ru.UTF-8):	dos2unix - конвертор текстовых файлов DOS в формат UNIX
Summary(uk.UTF-8):	dos2unix - конвертор текстових файлів DOS в формат UNIX
Summary(zh_CN.UTF-8):	转换DOS或MAC文本文件到UNIX格式
Name:		dos2unix
Version:	6.0.4
Release:	1
License:	BSD
Group:		Applications/Text
Source0:	http://waterlan.home.xs4all.nl/dos2unix/%{name}-%{version}.tar.gz
# Source0-md5:	f1fff9d70f9ba644c038677ba1d94ac0
URL:		http://waterlan.home.xs4all.nl/dos2unix.html
BuildRequires:	gettext-devel
BuildRequires:	perl-tools-pod
Provides:	unix2dos
Obsoletes:	unix2dos
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A utility that converts plain text files in DOS/MAC format to UNIX
format.

%description -l fr.UTF-8
Dos2unix converti des fichier texte DOS ou MAC au format UNIX.

%description -l pl.UTF-8
Zestaw narzędzi do konwersji plików tekstowych z formatów DOS/MAC na
format używany przez UNIX-a.

%description -l pt_BR.UTF-8
O dos2unix converte arquivos texto do DOS e MAC para o formato texto
do Unix.

%description -l ru.UTF-8
dos2unix - конвертор текстовых файлов DOS в формат UNIX.

%description -l uk.UTF-8
dos2unix - конвертор текстових файлів DOS в формат UNIX.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcflags} %{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# clean docdir
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

# dos2unix and unix2dos domains
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc BUGS.txt COPYING.txt ChangeLog.txt NEWS.txt README.txt TODO.txt
%attr(755,root,root) %{_bindir}/dos2unix
%attr(755,root,root) %{_bindir}/mac2unix
%attr(755,root,root) %{_bindir}/unix2dos
%attr(755,root,root) %{_bindir}/unix2mac
%{_mandir}/man1/dos2unix.1*
%{_mandir}/man1/mac2unix.1*
%{_mandir}/man1/unix2dos.1*
%{_mandir}/man1/unix2mac.1*
%lang(es) %{_mandir}/es/man1/dos2unix.1*
%lang(es) %{_mandir}/es/man1/mac2unix.1*
%lang(es) %{_mandir}/es/man1/unix2dos.1*
%lang(es) %{_mandir}/es/man1/unix2mac.1*
%lang(nl) %{_mandir}/nl/man1/dos2unix.1*
%lang(nl) %{_mandir}/nl/man1/mac2unix.1*
%lang(nl) %{_mandir}/nl/man1/unix2dos.1*
%lang(nl) %{_mandir}/nl/man1/unix2mac.1*
