%global commit f548abe8eae8
%global snapshot .hg20160125.%{commit}

Name:           libx265
Version:        80
Release:        1%{snapshot}%{?dist}
Summary:        x265 HEVC Encoder / H.265 Video Codec

License:        GPLv2
URL:            http://x265.org

# hg clone https://bitbucket.org/multicoreware/x265
# cd x265
# hg archive --prefix x265 -S x265.tar.bz2
Source0:        x265.tar.bz2

BuildRequires:  cmake
BuildRequires:  yasm

%description
x265 is a H.265 / HEVC video encoder application library, designed to encode
video or images into an H.265 / HEVC encoded bitstream.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        -n x265
Summary:        x265 cli encoder

%description    -n x265
This package contains the frontend.


%prep
%setup -q -n x265


%build
mkdir __build
pushd __build
%{cmake} ../source
make %{?_smp_mflags}
popd


%install
rm -rf %{buildroot}
pushd __build
%make_install
popd
rm -f %{buildroot}%{_libdir}/*.a


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc COPYING
%{_libdir}/*.so.%{version}

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/x265.pc

%files -n x265
%doc readme.rst
%{_bindir}/*


%changelog
* Wed Aug 10 2016 Jajauma's Packages <jajauma@yandex.ru> - 80-1.hg20160125.f548abe8eae8
- Public release
