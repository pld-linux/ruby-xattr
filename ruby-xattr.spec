Summary:	Extended Attributes module for Ruby
Summary(pl):	Modu� Extended Attributes dla Ruby
Name:		ruby-xattr
Version:	0.3.0
Release:	1
License:	Ruby License
Group:		Development/Languages
Source0:	http://www.theinternetco.net/projects/ruby/%{name}-%{version}.tar.gz
# Source0-md5:	a47d8f164d6c9d88f54f853d2bd7d50a
URL:		http://www.theinternetco.net/projects/ruby/ruby-xattr
BuildRequires:	attr-devel
BuildRequires:	rpmbuild(macros) >= 1.263
BuildRequires:	ruby
BuildRequires:	ruby-devel
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ruby-xattr is an extension to access the XFS-compatible extended
attribute system calls.

%description -l pl
ruby-xattr to rozszerzenie pozwalaj�ce na dost�p do wywo�a�
systemowych zwi�zanych z rozszerzonymi atrybutami kompatybilnymi z
systemem plik�w XFS.

%prep
%setup -q

%build
ruby extconf.rb
%{__make}
rdoc --op rdoc ext
rdoc --ri --op ri ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

%{__make} install \
	archdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir}

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_archdir}/*
%{ruby_ridir}/File/get*
%{ruby_ridir}/File/list*
%{ruby_ridir}/File/remove*
%{ruby_ridir}/File/set*
