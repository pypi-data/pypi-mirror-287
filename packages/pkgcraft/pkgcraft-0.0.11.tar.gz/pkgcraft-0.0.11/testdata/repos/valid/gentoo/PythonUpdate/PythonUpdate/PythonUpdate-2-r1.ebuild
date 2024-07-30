# Copyright 1999-2024 Gentoo Authors
# Distributed under the terms of the GNU General Public License v2

EAPI=8

PYTHON_COMPAT=( python3_8 )
inherit python-any-r1

DESCRIPTION="Ebuild with no available python updates due to deps"
HOMEPAGE="https://pkgcraft.pkgcraft"
LICENSE="MIT"
SLOT="0"

BDEPEND="stub/python-dep:1[${PYTHON_USEDEP}]"
DEPEND="${PYTHON_DEPS}"
