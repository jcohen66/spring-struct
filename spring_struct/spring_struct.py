#!/usr/bin/python
import argparse
import os
import sys


##
##  This app checks if common Spring component placeholders
##  exist and if not then creates them.
##

def touch_file(file_name):
    filehandle = open(file_name, 'w')
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

    # Create application folders
    for folder in src_folders:
        component_folder_path = path + '/' + src_root + '/' + folder
        if not os.path.isdir(component_folder_path):
            try:
                os.makedirs(component_folder_path)
            except OSError:
                print("Creation of the directory %s failed" % component_folder_path)
            else:
                print("Successfully created the directory %s " % component_folder_path)
        else:
            print("Directory already exists: %s " % component_folder_path)

    # Create application.properties file
    resource_path = path + '/' + res_root
    if not os.path.isdir(resource_path):
        try:
            os.makedirs(resource_path)
        except OSError:
            print("Creation of the directory %s failed" % resource_path)
        else:
            print("Successfully created the directory %s " % resource_path)
            property_file = resource_path + '/' + 'application.properties'
            print(property_file)
            if not os.path.isfile(property_file):
                touch_file(property_file)
    else:
        print("Directory already exists: %s " % resource_path)

    # Create resource folders
    for folder in res_folders:
        resource_folder_path = path + '/' + res_root + '/' + folder
        if not os.path.isdir(resource_folder_path):
            try:
                os.makedirs(resource_folder_path)
            except OSError:
                print("Creation of the directory %s failed" % resource_folder_path)
            else:
                print("Successfully created the directory %s " % resource_folder_path)
        else:
            print("Directory already exists: %s " % resource_folder_path)


if __name__ == '__main__':
    main(sys.argv[1:])
