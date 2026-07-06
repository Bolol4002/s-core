module alu (
    input  logic [31:0] operand_a,
    input  logic [31:0] operand_b,
    input  logic [2:0]  alu_op,

    output logic [31:0] result,
    output logic        zero
);

    // ALU operation encoding
    typedef enum logic [2:0] {
        ALU_ADD = 3'd0,
        ALU_SUB = 3'd1,
        ALU_AND = 3'd2,
        ALU_OR  = 3'd3
    } alu_op_t;

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
