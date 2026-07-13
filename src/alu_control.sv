module alu_control (
    input  logic [6:0] opcode,
    input  logic [2:0] funct3,
    input  logic [6:0] funct7,

    output logic [2:0] alu_op
);

    // R-type opcode
    localparam logic [6:0] R_TYPE = 7'b0110011;

    always_comb begin
        // Default: ADD
        alu_op = 3'd0;

        if (opcode == R_TYPE) begin
            unique case ({funct7, funct3})

                10'b0000000_000: alu_op = 3'd0; // ADD
                10'b0100000_000: alu_op = 3'd1; // SUB
                10'b0000000_111: alu_op = 3'd2; // AND
                10'b0000000_110: alu_op = 3'd3; // OR

                default: alu_op = 3'd0;

            endcase
        end
    end

endmodule