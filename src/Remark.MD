Run Arduino with printf of float, modify platform.txt

## Combine gc-sections, archives, and objects
# -- standard setting with stripped-down printf
# recipe.c.combine.pattern="{compiler.path}{compiler.c.elf.cmd}" {compiler.c.elf.flags} -mmcu={build.mcu} {compiler.c.elf.extra_flags} -o "{build.path}/{build.project_name}.elf" {object_files} "{build.path}/{archive_file}" "-L{build.path}" -lm
# -- printf with floating point support
recipe.c.combine.pattern="{compiler.path}{compiler.c.elf.cmd}" {compiler.c.elf.flags} -mmcu={build.mcu} {compiler.c.elf.extra_flags} -o "{build.path}/{build.project_name}.elf" {object_files} "{build.path}/{archive_file}" "-L{build.path}" -Wl,-u,vfprintf -lprintf_flt -lm

https://forum.arduino.cc/index.php?topic=344206.new&fbclid=IwAR2i6qsHX648Uo3pSwQfYvczEX-VvNJN6ddQYjCVhi7_2VA_8HGcmSTeXH4#new


Or Leave platform.txt alone and add these lines to boards.txt instead.

menu.printf=AVR printf Version

mega.menu.printf.default=Default printf
mega.menu.printf.default.compiler.c.elf.extra_flags=
mega.menu.printf.full=Full printf
mega.menu.printf.full.compiler.c.elf.extra_flags=-Wl,-u,vfprintf -lprintf_flt
mega.menu.printf.minimal=Minimal printf
mega.menu.printf.minimal.compiler.c.elf.extra_flags=-Wl,-u,vfprintf -lprintf_min