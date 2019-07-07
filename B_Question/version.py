from pkg_resources import parse_version

def compare_version(version1, version2):
    """
    Compare two version strings and return if the first one is greatet, less or equal to the second
    
    Params:
    - version1: A version string as input
    - version2: A version string as input 
    
     Returns:
    - Whether one is greater than, equal, or less than the other
    """
    ver1 = parse_version(version1) 
    ver2 = parse_version(version2) 

    if ver1 > ver2:
        return version1+' is greater than '+version2
    elif ver2 > ver1:
        return version1+' is less than '+version2
    else:
        return version1+' is equal to '+version2