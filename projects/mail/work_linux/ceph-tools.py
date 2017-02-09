#!/usr/bin/env python

import rados
import os

action = os.sys.argv[1]

cluster = rados.Rados(conffile='/etc/ceph/ceph.conf',
                      conf = dict(keyring = '/etc/ceph/ceph.client.avatarid.keyring'),
                      name = 'client.avatarid')
cluster.connect()

ioctx = cluster.open_ioctx('data')
object_iterator = ioctx.list_objects()

if action == 'list':
    while True:
        try:
            a = object_iterator.next()
            print a.key
        except StopIteration:
            break

if action == 'clear':
    while True:
        try:
            a = object_iterator.next()
            ioctx.remove_object(a.key)
        except StopIteration:
            break

ioctx.close()
