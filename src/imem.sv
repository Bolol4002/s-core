module imem (
    input  logic [31:0] addr,
    output logic [31:0] instruction
);

    // 256 x 32-bit instruction ROM
    logic [31:0] mem [0:255];

    // Load program at simulation start
    initial begin
        $readmemh("program.mem", mem);
    end

    // Asynchronous read
    assign instruction = mem[addr[31:2]];

endmodule