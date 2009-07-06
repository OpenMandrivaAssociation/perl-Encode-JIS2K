%define upstream_name    Encode-JIS2K
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    JIS X 0212 (aka JIS 2000) Encodings
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Encode/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Encode)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Provides: perl(Encode::JIS2K::2022JP3)

%description
To find out how to use this module in detail, see the Encode manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%perl_vendorlib/*
/usr/lib/debug/usr/lib/perl5/vendor_perl/*
/usr/src/debug/%{upstream_name}-%{upstream_version}/*



