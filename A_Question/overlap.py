def check_overlap(line1, line2):
    """
    Checks if there is  an overlap between two lines
    
    Params:
    - line1: A tuple containing two poitns of a line on the X-axis (not necessarily sorted)
    - line2: A tuple containing two poitns of a line on the X-axis (not necessarily sorted)
    
     Returns:
    - True if there is an overlap otherwise False
    """
    start1 = min(line1)
    end1 = max(line1)
    start2 = min(line2)
    end2 = max(line2)

    return end1 >= start2 and end2 >= start1