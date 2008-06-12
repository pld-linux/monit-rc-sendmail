Summary:	monitrc file for monitoring Sendmail mail server
Summary(pl.UTF-8):	Plik monitrc do monitorowania serwera poczty Sendmail
Name:		monit-rc-sendmail
Version:	1.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	sendmail.monitrc
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,postun):	monit
Requires:	monit
Requires:	sendmail >= 8.14.3-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
monitrc file for monitoring Sendmail mail server.

%description -l pl.UTF-8
Plik monitrc do monitorowania serwera poczty Sendmail.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/monit
install %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/monit

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q monit restart

%postun
%service -q monit restart

%files
%defattr(644,root,root,755)
%{_sysconfdir}/monit/*.monitrc
