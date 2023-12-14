def opener(day: int, sample: bool) -> list[str]:
    '''Openes and returns a parsed file according to params'''
    
    if sample:
        lines = [line.strip() for line in open("day-" + str(day) + "/sample.txt", "r")]
        return lines
    else:
        lines = [line.strip() for line in open("day-" + str(day) + "/data.txt", "r")]
        return lines
    
def opener_guided() -> list[int | bool]:
    '''Returns values for opening files to set'''
    
    day: int = int(input("Day? "))
    use_sample: bool = bool(input("Use the sample? "))
    
    return [day, use_sample]
