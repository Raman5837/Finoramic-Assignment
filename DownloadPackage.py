'''
    A Python Script To Download All Modules From A Given Package.json File
'''

import json as JSON
import sys
import subprocess
import pkg_resources
from pkg_resources import DistributionNotFound, VersionConflict

# A Utility Function To Extract All Packages From Package.json File
def GetPackage():
    PackagesToBeInstall = []
    with open("Enter Path Of Your Package.json File") as File:
        Data = JSON.load(File)
        for key, value in Data['Dependencies'].items():  
            ModuleName = key + '==' + str(value)
            PackagesToBeInstall.append(ModuleName)
    
    return PackagesToBeInstall


# A Utility Function To Check The Availablity & VersionConflict Of The Given Package
def ShouldInstallPackage(Package):
    ShouldInstall = False

    try:
        pkg_resources.require(Package)
    except (DistributionNotFound, VersionConflict):
        ShouldInstall = True
    
    return ShouldInstall

# Main Function To Download All Of The Packages
def DownloadDepencies(PackageList):
    
    try:
        Packages = [Package for Package in PackageList if ShouldInstallPackage(Package)]
        
        # If Packages Is Empty, Means All Packages Are Already Downloaded
        if not Packages: return 'Requirements Already Satisfied'
        
        subprocess.check_call([sys.executable, "-m", "pip", "install", *Packages])
        
        return 'Successfully Installed All Packages'
    
    except Exception as Error:
        print("Something Went Wrong")
        return Error

if __name__ == '__main__':
    
    PackageList = GetPackage()
    print(DownloadDepencies(PackageList))