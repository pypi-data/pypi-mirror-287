const std = @import("std");
const py = @import("pydust");

pub fn hello() !py.PyString {
    return try py.PyString.create("Hello!");
}

comptime {
    py.rootmodule(@This());
}

test "hello test" {
    const result = hello();
    std.testing.expect(result == py.PyString.create("Hello"));
}
