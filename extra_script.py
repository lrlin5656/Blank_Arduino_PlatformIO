Import("env")

# General options that are passed to the C and C++ compilers
# General options that are passed to the C++ compiler
# -Wl,-u,vfprintf -lprintf_flt -lm
env.Append(CXXFLAGS=["-Wc++14-compat"])
env.Append(
    CCFLAGS=[
        "-u",
        "vfprintf",
        "-lprintf_flt",
        "-lm"
    ],
    LINKFLAGS=[
        "-u",
        "vfprintf",
        "-lprintf_flt",
        "-lm"
    ]
)
