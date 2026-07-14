import cpu_pkg::*;

module alu (
    input  logic [31:0] operand_a,
    input  logic [31:0] operand_b,
    input  alu_op_t alu_op,

    output logic [31:0] result,
    output logic        zero
);

    always_comb begin
        // Default assignment
        result = 32'd0;

        unique case (alu_op)
            ALU_ADD: result = operand_a + operand_b;
            ALU_SUB: result = operand_a - operand_b;
            ALU_AND: result = operand_a & operand_b;
            ALU_OR : result = operand_a | operand_b;
            default: result = 32'd0;
        endcase

        // Zero flag
        zero = (result == 32'd0);
    end

endmodule
