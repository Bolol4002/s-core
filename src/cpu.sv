import cpu_pkg::*;

module cpu (
    input logic clk,
    input logic rst,
    output logic [31:0] alu_result,
    output logic zero
);

    logic [31:0] pc;
    logic [31:0] next_pc;
    logic [31:0] instruction;

    logic [6:0] opcode;
    logic [4:0] rd;
    logic [2:0] funct3;
    logic [4:0] rs1;
    logic [4:0] rs2;
    logic [6:0] funct7;

    logic [31:0] rs1_data;
    logic [31:0] rs2_data;

    alu_op_t alu_op;

    logic reg_write;
    logic alu_src;
    logic mem_read;
    logic mem_write;
    logic mem_to_reg;
    logic branch;
    logic jump;

    pc u_pc (
        .clk(clk),
        .rst(rst),
        .next_pc(next_pc),
        .pc_o(pc)
    );

    pc_plus4 u_pc_plus4 (
        .pc_i(pc),
        .next_pc(next_pc)
    );

    imem u_imem (
        .addr(pc),
        .instruction(instruction)
    );

    idecoder u_idecoder (
        .instruction(instruction),
        .opcode(opcode),
        .rd(rd),
        .funct3(funct3),
        .rs1(rs1),
        .rs2(rs2),
        .funct7(funct7)
    );

    control_unit u_control_unit (
        .opcode(opcode),
        .reg_write(reg_write),
        .alu_src(alu_src),
        .mem_read(mem_read),
        .mem_write(mem_write),
        .mem_to_reg(mem_to_reg),
        .branch(branch),
        .jump(jump)
    );

    alu_control u_alu_control (
        .opcode(opcode),
        .funct3(funct3),
        .funct7(funct7),
        .alu_op(alu_op)
    );

    regfile u_regfile (
        .clk(clk),
        .we(reg_write),
        .rs1_addr(rs1),
        .rs2_addr(rs2),
        .rd_addr(rd),
        .rd_data(alu_result),
        .rs1_data(rs1_data),
        .rs2_data(rs2_data)
    );

    alu u_alu (
        .operand_a(rs1_data),
        .operand_b(rs2_data),
        .alu_op(alu_op),
        .result(alu_result),
        .zero(zero)
    );

endmodule
