from __future__ import print_function

from xml.etree import ElementTree

import jss
import pytest


class TestObjectsPolicies(object):
    """Test Policy Object Methods"""

    def test_add_package(
        self, policy, package
    ):  # type: (jss.Policy, jss.Package) -> None
        package.save()
        policy.add_package(package)
        policy.save()

    def test_get_packages(self, policy):  # type: (jss.Policy) -> None
        packages = policy.get_packages()
        assert isinstance(packages, jss.QuerySet)
        print(packages)

    def test_add_script(self, policy):  # type: (jss.Policy) -> None
        policy.add_script("Script Name")
