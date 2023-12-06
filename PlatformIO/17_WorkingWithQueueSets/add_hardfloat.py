Import( "env" )

flags = [
    "-mfloat-abi=hard",
    "-mfpu=fpv5-d16",
    "-mthumb",
    "-u _printf_float",
    "-mcpu=cortex-m7",
    "-DDEBUG -c -x assembler-with-cpp --specs=nano.specs"
]
env.Append(CCFLAGS=flags, LINKFLAGS=flags, ASFLAGS=flags)