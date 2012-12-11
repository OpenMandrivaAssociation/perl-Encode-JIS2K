%define upstream_name    Encode-JIS2K
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

Summary:    JIS X 0212 (aka JIS 2000) Encodings
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Encode/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Encode)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Provides: perl(Encode::JIS2K::2022JP3)

%description
To find out how to use this module in detail, see the Encode manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%perl_vendorlib/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.20.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-3mdv2011.0
+ Revision: 555802
- rebuild for perl 5.12

* Fri Mar 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-2mdv2010.1
+ Revision: 518454
- ship debug files in -debug

* Mon Jul 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 392893
- fixing buildrequires:
- adding missing provides:
- import perl-Encode-JIS2K


* Mon Jul 06 2009 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist
