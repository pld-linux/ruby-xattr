%define	ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
%define	ruby_version	%(ruby -r rbconfig -e 'print Config::CONFIG["ruby_version"]')
Summary:	Extended Attributes module for Ruby
Summary(pl):	Modu³ Extended Attributes dla Ruby
Name:		ruby-xattr
Version:	0.3.0
Release:	1
License:	Ruby License
Group:		Development/Languages
Source0:	http://www.theinternetco.net/projects/ruby/%{name}-%{version}.tar.gz
# Source0-md5:	a47d8f164d6c9d88f54f853d2bd7d50a
URL:	http://www.theinternetco.net/projects/ruby/ruby-xattr
BuildRequires:	ruby
BuildRequires:	ruby-devel
BuildRequires:	attr-devel
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ruby-xattr is an extension to access the xfs-compatible extended attribute
system calls.

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
%{ruby_ridir}/File/*
