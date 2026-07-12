module pc_plus4 (
    input  logic [31:0] pc_i,
    output logic [31:0] next_pc
);

    assign next_pc = pc_i + 32'd4;

endmodule