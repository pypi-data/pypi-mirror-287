# Copyright 1999-2024 Gentoo Authors
# Distributed under the terms of the GNU General Public License v2

EAPI=8

USE_RUBY="ruby31 ruby32"
inherit ruby-ng

DESCRIPTION="Ebuild with no available ruby updates due to deps"
HOMEPAGE="https://pkgcraft.pkgcraft"
LICENSE="MIT"
SLOT="0"

ruby_add_rdepend "
	stub/ruby-dep:1
"
