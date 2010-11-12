Summary:	dos2unix - DOS/MAC to UNIX text file format converter
Summary(fr.UTF-8):	Convertisseur de format de fichier texte
Summary(pl.UTF-8):	dos2unix - konwerter plików tekstowych z formatów DOS/MAC na UNIX
Summary(pt_BR.UTF-8):	Conversor de formatos de arquivos texto
Summary(ru.UTF-8):	dos2unix - конвертор текстовых файлов DOS в формат UNIX
Summary(uk.UTF-8):	dos2unix - конвертор текстових файлів DOS в формат UNIX
Summary(zh_CN.UTF-8):	转换DOS或MAC文本文件到UNIX格式
Name:		dos2unix
Version:	5.1.1
Release:	1
License:	Freer than LGPL
Group:		Applications/Text
Source0:	http://www.xs4all.nl/~waterlan/dos2unix/%{name}-%{version}.tar.gz
# Source0-md5:	b8f6d8109fc6decf412bc1e3959450c0
URL:		http://www.xs4all.nl/~waterlan/dos2unix.html
Patch2:		%{name}-includes.patch
Patch3:		%{name}-manpage-update.patch
Patch6:		%{name}-workaround-rename-EXDEV.patch
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
%patch2 -p1
#%patch3 -p1
#%patch6 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

find $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYING.txt ChangeLog.txt NEWS.txt README.txt TODO.txt
%attr(755,root,root) %{_bindir}/dos2unix
%attr(755,root,root) %{_bindir}/mac2unix
%attr(755,root,root) %{_bindir}/unix2dos
%attr(755,root,root) %{_bindir}/unix2mac
%{_mandir}/man1/*
