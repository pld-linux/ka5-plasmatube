#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.5
%define		qtver		5.15.2
%define		kf5ver		5.71.0
%define		kaname		plasmatube
Summary:	YouTube video player
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	1
License:	GPL v2+/GPL v3+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	0fc3d46b39e3c2fa46ad1cb1742bd03e
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= 5.15.2
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel >= 5.15.10
BuildRequires:	Qt5Qml-devel >= 5.15.10
BuildRequires:	Qt5Quick-controls2-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.81.0
BuildRequires:	kf5-kconfig-devel >= 5.81.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.81.0
BuildRequires:	kf5-ki18n-devel >= 5.81.0
BuildRequires:	kf5-kirigami2-devel >= 5.81.0
BuildRequires:	mpv-client-devel
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YouTube video player based on libmpv and yt-dlp.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{sr,zh_CN}

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/plasmatube
%{_desktopdir}/org.kde.plasmatube.desktop
%{_iconsdir}/hicolor/scalable/apps/org.kde.plasmatube.svg
%{_datadir}/metainfo/org.kde.plasmatube.appdata.xml
