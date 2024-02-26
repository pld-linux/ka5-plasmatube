#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.01.95
%define		qtver		5.15.2
%define		kf5ver		5.71.0
%define		kaname		plasmatube
Summary:	YouTube video player
Name:		ka5-%{kaname}
Version:	24.01.95
Release:	0.1
License:	GPL v2+/GPL v3+
Group:		X11/Applications
Source0:	https://download.kde.org/unstable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	949259fc6332fb0adecf27c3cf7171ab
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= 5.15.2
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6Network-devel >= 5.15.10
BuildRequires:	Qt6Qml-devel >= 5.15.10
BuildRequires:	Qt6Quick-devel
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= 5.81.0
BuildRequires:	kf6-kconfig-devel >= 5.81.0
BuildRequires:	kf6-kcoreaddons-devel >= 5.81.0
BuildRequires:	kf6-ki18n-devel >= 5.81.0
BuildRequires:	kf6-kirigami-devel >= 5.81.0
BuildRequires:	mpv-client-devel
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	qt6-build >= %{qtver}
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
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=6
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
%{_iconsdir}/hicolor/scalable/actions/*.svg
%{_datadir}/metainfo/org.kde.plasmatube.appdata.xml
