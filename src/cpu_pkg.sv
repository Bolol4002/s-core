package cpu_pkg;

    localparam logic [6:0] OPCODE_RTYPE = 7'b0110011;

    typedef enum logic [2:0] {
        ALU_ADD,
        ALU_SUB,
        ALU_AND,
        ALU_OR
    } alu_op_t;

endpackage
