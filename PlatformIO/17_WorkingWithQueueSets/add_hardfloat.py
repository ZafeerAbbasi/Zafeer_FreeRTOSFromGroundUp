Import( "env" )

flags = [
    "-mcpu=cortex-m7",
    "-std=gnu11",
    "-g3",
    "-ffunction-sections",
    "-fdata-sections",
    "-Wall",
    "-fstack-usage",
    "--specs=nano.specs",
    "-mfpu=fpv5-d16",
    "-mfloat-abi=softfp",
    "-mthumb",
    "-u _printf_float",
]
env.Append(CCFLAGS=flags, LINKFLAGS=flags, ASFLAGS=flags)
