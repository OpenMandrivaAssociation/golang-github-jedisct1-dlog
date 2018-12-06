# Run tests in check section
%bcond_without check

%global goipath         github.com/jedisct1/dlog
%global commit          f81e5af176e59fc11674b2777fe465fc506c27fe

%global common_description %{expand:
A super simple logger for Go. Supports stderr, logfiles, syslog and windows 
event log.}

%gometa

Name:           %{goname}
Version:        0.3
Release:        3%{?dist}
Summary:        A super simple logger for Go
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/hashicorp/go-syslog)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup

rm -rf vendor


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Tue Jul 17 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.3-3.20180717gitf81e5af
- Bump to commit f81e5af176e59fc11674b2777fe465fc506c27fe

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.3-1
- First package for Fedora

