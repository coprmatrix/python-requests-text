#
# spec file for package python-requests-text
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           python-requests-text
Version:        1.0.0
Release:        0
Summary:        File transport adapter for Requests
License:        Apache-2.0
URL:            https://github.com/huakim/python-requests-text
Source:         requests_text-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires: %{python_module pytest}

BuildRequires:  %{python_module requests >= 1.0.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-requests >= 1.0.0
BuildArch:      noarch
%python_subpackages

%description
Requests-Text
=============

Requests-Text is a transport adapter for use with the `Requests`_ Python
library to allow text under text:\/\/ URLs.

To use:

.. code-block:: python

    import requests
    from requests_text import TextAdapter

    s = requests.Session()
    s.mount('text://', TextAdapter())

    resp = s.get('text://sometext')

Features
--------

- Will open and read text
- Might set a Content-Length header
- That's about it

------------

Contributions welcome! Feel free to open a pull request against
https://github.com/huakim/python-requests-text

License
-------

To maximise compatibility with Requests, this code is licensed under the Apache
license. See LICENSE for more details.

.. _`Requests`: https://github.com/kennethreitz/requests


%prep
%autosetup -p1 -n requests_text-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/requests_text.py
%pycache_only %{python_sitelib}/__pycache__/requests_text.*.py*
%license LICENSE
%doc README.rst
%{python_sitelib}/requests_text-%{version}.dist-info

%changelog
