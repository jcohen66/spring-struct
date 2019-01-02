#!/usr/bin/python
import os
import sys
import argparse


def touch_file(fn):
    filehandle = open(fn, 'w')
    filehandle.write('')
    filehandle.close()

def path_from_package(pkg):
    path = pkg.replace('.', '/')
    return path

def main(args=None):
    src_folders = {'controllers', 'model', 'services', 'config', 'repositories'}
    res_folders = {'static', 'templates'}

    parser = argparse.ArgumentParser()
    parser.add_argument('pkg', help='root package')
    args = parser.parse_args()
    root_pkg = args.pkg

    print('Root package is %s' % root_pkg)

    src_root = 'src/main/java/' + path_from_package(root_pkg)
    res_root = 'src/main/resources'

    path = os.getcwd()

    for folder in src_folders:
        ps = path + '/' + src_root + '/' + folder
        if not os.path.isdir(ps):
            try:
                os.makedirs(ps)
            except OSError:
                print("Creation of the directory %s failed" % ps)
            else:
                print("Successfully created the directory %s " % ps)
        else:
            print("Directory already exists: %s " % ps)

        rp = path + '/' + res_root
        if not os.path.isdir(rp):
            try:
                os.makedirs(rp)
            except OSError:
                print("Creation of the directory %s failed" % rp)
            else:
                print("Successfully created the directory %s " % rp)
                rpf = rp + '/' + 'application.properties'
                print(rpf)
                if not os.path.isfile(rpf):
                    touch_file(rpf)
        else:
            print("Directory already exists: %s " % rp)

        for folder in res_folders:
            rs = path + '/' + res_root + '/' + folder
            if not os.path.isdir(rs):
                try:
                    os.makedirs(rs)
                except OSError:
                    print("Creation of the directory %s failed" % rs)
                else:
                    print("Successfully created the directory %s " % rs)
            else:
                print("Directory already exists: %s " % rs)


if __name__ == '__main__':
    main(sys.argv[1:])
