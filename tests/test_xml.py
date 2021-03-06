# -*- coding: utf-8 -*-

"""Tests for the xml module."""

from __future__ import unicode_literals

from soco import xml


def test_register_namespace():
    assert xml.register_namespace


def test_ns_tag():
    """Test the ns_tag function."""
    namespaces = ['http://purl.org/dc/elements/1.1/',
                  'urn:schemas-upnp-org:metadata-1-0/upnp/',
                  'urn:schemas-upnp-org:metadata-1-0/DIDL-Lite/']
    for ns_in, namespace in zip(['dc', 'upnp', ''], namespaces):
        res = xml.ns_tag(ns_in, 'testtag')
        correct = '{{{0}}}{1}'.format(namespace, 'testtag')
        assert res == correct
