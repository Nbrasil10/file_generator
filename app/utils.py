def to_bytes(value, unit):
    unit = unit.lower()
    if unit == "kb":
        return value * 1024
    if unit == "mb":
        return value * 1024 * 1024
    if unit == "gb":
        return value * 1024 * 1024 * 1024
    return value