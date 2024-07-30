# Copyright 1999-2024 Gentoo Authors
# Distributed under the terms of the GNU General Public License v2

EAPI=8

PYTHON_COMPAT=( python3_8 )
inherit python-r1

DESCRIPTION="stub ebuild with incomplete python support"
HOMEPAGE="https://pkgcraft.pkgcraft"
LICENSE="MIT"
SLOT="1"
REQUIRED_USE="${PYTHON_REQUIRED_USE}"

RDEPEND="${PYTHON_DEPS}"
