def oxford_comma(arr):
    # lib/oxford_comma.py

   
    if len(arr) == 0:
        return ""
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return f"{arr[0]} and {arr[1]}"
    else:
        c_separated = ", ".join(arr[:-1])
        return f"{c_separated}, and {arr[-1]}"
