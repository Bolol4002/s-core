import cpu_pkg::*;

module alu_control (
    input  logic [6:0] opcode,
    input  logic [2:0] funct3,
    input  logic [6:0] funct7,

    output alu_op_t alu_op
);

    always_comb begin
        // Default: ADD
        alu_op = ALU_ADD;

        if (opcode == OPCODE_RTYPE) begin
            unique case ({funct7, funct3})

                10'b0000000_000: alu_op = ALU_ADD; // ADD
                10'b0100000_000: alu_op = ALU_SUB; // SUB
                10'b0000000_111: alu_op = ALU_AND; // AND
                10'b0000000_110: alu_op = ALU_OR;  // OR

                default: alu_op = ALU_ADD;

            endcase
        end
    end

endmodule