Import( "env" )

flags = [
    "-mfpu=fpv5-d16",
    "-mfloat-abi=hard",
    "-mthumb",
    "-u _printf_float",
]
env.Append(CCFLAGS=flags, LINKFLAGS=flags, ASFLAGS=flags)
