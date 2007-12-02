Summary:	CACAO Java Virtual Machine
Summary(pl.UTF-8):	CACAO JVM - wirtualna maszyna Javy
Name:		cacao
Version:	0.98
Release:	0.1
License:	GPL v2+
Group:		Development/Languages/Java
Source0:	http://www.complang.tuwien.ac.at/cacaojvm/download/cacao-%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	8b8907c8b925761c9410bcadb9705346
URL:		http://www.cacaojvm.org/
BuildRequires:	classpath-devel
Requires:	classpath
ExclusiveArch:	%{ix86} %{x8664} alpha arm hppa m68k mips ppc ppc64 s390 sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CACAO is a Java Virtual Machine with a JIT compiler for various
architectures. It includes the Boehm garbage collector and uses GNU
Classpath as core Java library.

%description -l pl.UTF-8
CACAO to maszyna wirtualna Javy (JVM) z kompilatorem JIT dla różnych
architektur. Zawiera odśmiecacz (garbage collector) Boehma, a jako
podstawową bibliotekę Javy wykorzystuje GNU Classpath.

%prep
%setup -q

%build
%configure \
	--with-classpath-prefix=%{_libdir}/classpath \
	--with-classpath-classes=%{_datadir}/glibj.zip \
	--with-classpath-includedir=%{_includedir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* NEWS README THIRDPARTY
%attr(755,root,root) %{_bindir}/cacao
%attr(755,root,root) %{_bindir}/cacaodbgserver
%attr(755,root,root) %{_bindir}/java
%attr(755,root,root) %{_libdir}/libjdwp.so.*.*.*
%attr(755,root,root) %{_libdir}/libjvm-*.so
%dir %{_datadir}/cacao
%{_datadir}/cacao/vm.zip
%{_mandir}/man1/cacao.1*
