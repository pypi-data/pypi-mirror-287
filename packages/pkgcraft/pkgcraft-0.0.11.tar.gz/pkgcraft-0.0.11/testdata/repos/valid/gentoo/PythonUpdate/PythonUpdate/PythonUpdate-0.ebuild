# Copyright 1999-2024 Gentoo Authors
# Distributed under the terms of the GNU General Public License v2

EAPI=8

# unordered impls
PYTHON_COMPAT=( python3_{9,8,10})
inherit python-r1

DESCRIPTION="Ebuild with potential python updates"
HOMEPAGE="https://pkgcraft.pkgcraft"
LICENSE="MIT"
SLOT="0"
REQUIRED_USE="${PYTHON_REQUIRED_USE}"

RDEPEND="
	${PYTHON_DEPS}
	stub/python-dep:0[${PYTHON_USEDEP}]
"
